# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "z3-solver",
# ]
# ///

from z3 import *
import dataclasses
import pathlib

DEBUG = False
def log(*args):
    if DEBUG:
        print(*args)

OPS = {
    0: 'adv',
    1: 'bxl',
    2: 'bst',
    3: 'jnz',
    4: 'bxc',
    5: 'out',
    6: 'bdv',
    7: 'cdv',
    2**64 - 1: 'halt'
}

@dataclasses.dataclass
class State:
    a: int
    b: int
    c: int

@dataclasses.dataclass
class Result:
    init: State
    final: State
    output: list[int]
    


def ingest(filestring):
    a, b, c, _, program = filestring.splitlines()
    a = int(a.removeprefix('Register A: '))
    b = int(b.removeprefix('Register B: '))
    c = int(c.removeprefix('Register C: '))
    program = [int(d) for d in program.removeprefix('Program: ').split(',')]
    return (a, b, c, program)


def make_array(name, length, sort):
    return [Const(f"{name}{i}", sort) for i in range(length)]


def seq_to_py(m, s):
    l = m.eval(Length(s)).as_long()
    for i in range(l):
        yield m.eval(s[i]).as_long()


def run_computer(a_init, b_init, c_init, program, output_spec, max_exec):
    Z = IntSort()
    BV = BitVecSort(64)

    a = make_array("a", max_exec, BV)
    b = make_array("b", max_exec, BV)
    c = make_array("c", max_exec, BV)
    ip = make_array("ip", max_exec, BV)
    combo = make_array("combo", max_exec, BV)

    # We could probably make this a single sequence, but this shape
    # made it a bit easier to write.
    output = make_array('output', max_exec, SeqSort(BV))

    # This might be more efficient as another python collection of
    # scalars, but indexing into that would require a big pile of
    # implications which would be Effort. So instead we'll go with the
    # array.
    mem = Array('mem', BV, BV)
    
    s = Solver()

    if a_init is not None:
        s.add(a[0] == a_init)
    if b_init is not None:
        s.add(b[0] == b_init)
    if c_init is not None:
        s.add(c[0] == c_init)

    s.add(ip[0] == 0)
    s.add(ip[-1] == len(program))

    for idx, p in enumerate(program):
        s.add(mem[idx] == p)

    idx = Const('idx', BV)
    s.add(ForAll([idx], Implies(idx >= len(program), mem[idx] == -1)))

    s.add(output[0] == Empty(SeqSort(BV)))
    if output_spec is not None:
        s.add(Length(output[-1]) == len(program))
        for idx, p in enumerate(output_spec):
            if p is not None:
                s.add(output[-1][idx] == p)

    for step in range(max_exec-1):
        opcode = mem[ip[step]]
        operand = mem[ip[step] + 1]

        combo_setup = [
            Implies(And(0 <= operand, operand <= 3), combo[step] == operand),
            Implies(operand == 4, combo[step] == a[step]),
            Implies(operand == 5, combo[step] == b[step]),
            Implies(operand == 6, combo[step] == c[step]),
            operand != 7,
        ]
        no_combo = [
            combo[step] == -1,
        ]

        s.add(ip[step] >= 0)

        s.add(Implies(ip[step] >= len(program), And(
            a[step+1] == a[step],
            b[step+1] == b[step],
            c[step+1] == c[step],
            ip[step+1] == ip[step],
            output[step+1] == output[step],
            *no_combo,
        )))
        
        s.add(Implies(opcode == 0, And(
            a[step+1] == a[step] >> combo[step],
            b[step+1] == b[step],
            c[step+1] == c[step],
            ip[step+1] == ip[step] + 2,
            output[step+1] == output[step],
            *combo_setup,
        )))
        s.add(Implies(opcode == 1, And(
            a[step+1] == a[step],
            b[step+1] == b[step] ^ operand,
            c[step+1] == c[step],
            ip[step+1] == ip[step] + 2,
            output[step+1] == output[step],
            *no_combo,
        )))
        s.add(Implies(opcode == 2, And(
            a[step+1] == a[step],
            b[step+1] == combo[step] % 8,
            c[step+1] == c[step],
            ip[step+1] == ip[step] + 2,
            output[step+1] == output[step],
            *combo_setup,
        )))
        s.add(Implies(opcode == 3, If(
            a[step] == 0,
            And(
                a[step+1] == a[step],
                b[step+1] == b[step],
                c[step+1] == c[step],
                ip[step+1] == ip[step] + 2,
                output[step+1] == output[step],
                *no_combo,
            ),
            And(
                a[step+1] == a[step],
                b[step+1] == b[step],
                c[step+1] == c[step],
                ip[step+1] == operand,
                output[step+1] == output[step],
                *no_combo,
            ),
        )))
        s.add(Implies(opcode == 4, And(
            a[step+1] == a[step],
            b[step+1] == b[step] ^ c[step],
            c[step+1] == c[step],
            ip[step+1] == ip[step] + 2,
            output[step+1] == output[step],
            *no_combo,
        )))
        s.add(Implies(opcode == 5, And(
            a[step+1] == a[step],
            b[step+1] == b[step],
            c[step+1] == c[step],
            ip[step+1] == ip[step] + 2,
            output[step+1] == Concat(output[step], Unit(combo[step] % 8)),
            *combo_setup,
        )))
        s.add(Implies(opcode == 6, And(
            a[step+1] == a[step],
            b[step+1] == a[step] >> combo[step],
            c[step+1] == c[step],
            ip[step+1] == ip[step] + 2,
            output[step+1] == output[step],
            *combo_setup,
        )))
        s.add(Implies(opcode == 7, And(
            a[step+1] == a[step],
            b[step+1] == b[step],
            c[step+1] == a[step] >> combo[step],
            ip[step+1] == ip[step] + 2,
            output[step+1] == output[step],
            *combo_setup,
        )))

    result = s.check()
    assert result == sat

    def get_result():
        m = s.model()
        return Result(
            init=State(
                a=m.eval(a[0]).as_long(),
                b=m.eval(b[0]).as_long(),
                c=m.eval(c[0]).as_long(),
            ),
            final=State(
                a=m.eval(a[-1]).as_long(),
                b=m.eval(b[-1]).as_long(),
                c=m.eval(c[-1]).as_long(),
            ),
            output=list(seq_to_py(m, output[-1])),
        )

    min_result = get_result()
    print("found initial result, checking minimality...")
    print(min_result)
    while True:
        s.add(a[0] < min_result.init.a)
        if s.check() == unsat:
            print("result is minimal!")
            return min_result
        min_result = get_result()
        print("found better result, minimizing...")
        print(min_result)


    # for i in range(len(program) + 3):
    #     log(f"mem [{i:2}] : {m.eval(mem[i])}")

    # for i in range(max_exec):
    #     def dbg(n, v):
    #         name = str(v)
    #         if is_seq(v):
    #             val = list(seq_to_py(m, v))
    #         elif is_int(v):
    #             val = m.eval(v).as_long()
    #         else:
    #             val = m.eval(v)
    #         log(f"  {n:8}: {name:14}  = {val}")


    #     log("step:  ", i)
    #     dbg('a', a[i])
    #     dbg('b', b[i])
    #     dbg('c', c[i])
    #     dbg('ip', ip[i])
    #     dbg('op', mem[ip[i]])
    #     dbg('operand', mem[ip[i] + 1])
    #     opidx = m.eval(mem[ip[i]]).as_long()
    #     op = OPS[opidx]
    #     log(f"      ({op})")
    #     dbg('combo', combo[i])
    #     dbg('output', output[i])


def main():
    a, b, c, program = ingest(pathlib.Path('/home/fulei/git/advent_of_code/aoc_inputs/2024/day17input.txt').read_text())
    print(a, b, c, program)

    r = run_computer(a, b, c, program, None, 100)
    print(r)

    r = run_computer(None, b, c, program, program, 200)
    print(r)


if __name__ == "__main__":
    main()