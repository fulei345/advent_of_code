use itertools::Itertools;
use tracing::info;

#[derive(Debug)]
struct Registers {
    a: u32,
    b: u32,
    c: u32,
    pointer: usize,
}

impl Registers {
    fn move_to_next_instruction(&mut self) {
        self.pointer += 2;
    }
    fn combo(&self, operand: &Instruction) -> u32 {
        match *operand as u32 {
            n if (0..=3).contains(&n) => n as u32,
            4 => self.a,
            5 => self.b,
            6 => self.c,
            n => {
                unreachable!("something is wrong, {n}")
            }
        }
    }

    fn op(&mut self, instruction: &Instruction, operand: &Instruction) -> Option<u32> {
        match instruction {
            Instruction::Adv => {
                self.a /= 2u32.pow(self.combo(operand) as u32);
                self.move_to_next_instruction();
            }
            Instruction::Bxl => {
                self.b ^= *operand as u32;
                self.move_to_next_instruction();
            }
            Instruction::Bst => {
                self.b = (self.combo(operand) % 8) as u32;
                self.move_to_next_instruction();
            }
            Instruction::Jnz => {
                if self.a == 0 {
                    self.move_to_next_instruction();
                    return None;
                }
                self.pointer = *operand as usize;
            }
            Instruction::Bxc => {
                self.b ^= self.c;
                self.move_to_next_instruction();
            }
            Instruction::Out => {
                self.move_to_next_instruction();
                return Some((self.combo(operand) % 8) as u32);
            }
            Instruction::Bdv => {
                self.b = self.a / 2u32.pow(self.combo(operand) as u32);
                self.move_to_next_instruction();
            }
            Instruction::Cdv => {
                self.c = self.a / 2u32.pow(self.combo(operand) as u32);
                self.move_to_next_instruction();
            }
        }
        None
    }
}

#[derive(Debug, Clone, Copy)]
enum Instruction {
    // A /= 2^Combo
    Adv = 0,
    // B ^= Combo
    Bxl = 1,
    // B = Combo % 8
    Bst = 2,
    // if A == 0, jump to Combo
    Jnz = 3,
    // B ^= C
    Bxc = 4,
    // Output Combo % 8
    Out = 5,
    // B = A / 2^Combo
    Bdv = 6,
    // C = A / 2^Combo
    Cdv = 7,
}

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let (mut registers, instructions) = parse(_input);
    Ok(run(&mut registers, &instructions))
}

fn run(registers: &mut Registers, instructions: &[Instruction]) -> String {
    let mut outputs = vec![];

    while registers.pointer < instructions.len() {
        if let Some(output) = registers.op(
            &instructions[registers.pointer],
            &instructions[registers.pointer + 1],
        ) {
            outputs.push(output);
        }
        info!(?registers);
    }
    // Join with , and return
    outputs.iter().map(|x| x.to_string()).join(",")
}

fn parse(_input: &str) -> (Registers, Vec<Instruction>) {
    let input = _input.trim();
    // Parse the input to registers and instructions
    let mut both = input.split("\n\n");
    let registers: Vec<i32> = both
        .next()
        .unwrap()
        .lines()
        .map(|line| {
            let mut parts = line.split(": ");
            let _ = parts.next().unwrap();
            parts.next().unwrap().parse::<i32>().unwrap()
        })
        .collect::<Vec<_>>();
    let program: Vec<i32> = both
        .next()
        .unwrap()
        .lines()
        .flat_map(|line| {
            line.split(": ")
                .nth(1)
                .unwrap()
                .split(',')
                .map(|x| x.parse::<i32>().unwrap())
        })
        .collect::<Vec<_>>();

    let registers = Registers {
        a: registers[0] as u32,
        b: registers[1] as u32,
        c: registers[2] as u32,
        pointer: 0,
    };

    let instructions: Vec<Instruction> = program
        .iter()
        .map(|&x| match x {
            0 => Instruction::Adv,
            1 => Instruction::Bxl,
            2 => Instruction::Bst,
            3 => Instruction::Jnz,
            4 => Instruction::Bxc,
            5 => Instruction::Out,
            6 => Instruction::Bdv,
            7 => Instruction::Cdv,
            _ => unreachable!(),
        })
        .collect();

    (registers, instructions)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0";
        assert_eq!("4635635210", process(input)?);
        Ok(())
    }

    #[test]
    fn testn_01() -> miette::Result<()> {
        let input = "Register A: 0
Register B: 0
Register C: 9

Program: 2,6";

        let (mut registers, instructions) = parse(input);
        run(&mut registers, &instructions);
        assert_eq!(registers.b, 1);
        Ok(())
    }

    #[test]
    fn testn_02() -> miette::Result<()> {
        let input = "Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4";
        let (mut registers, instructions) = parse(input);
        let output = run(&mut registers, &instructions);

        assert_eq!("012", output);
        Ok(())
    }
    #[test_log::test]
    fn testn_03() -> miette::Result<()> {
        let input = "Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0";
        let (mut registers, instructions) = parse(input);
        let output = run(&mut registers, &instructions);

        assert_eq!(registers.a, 0);
        assert_eq!("42567777310", output);
        Ok(())
    }
    #[test_log::test]
    fn testn_04() -> miette::Result<()> {
        let input = "Register A: 0
Register B: 29
Register C: 0

Program: 1,7";
        let (mut registers, instructions) = parse(input);
        let output = run(&mut registers, &instructions);

        run(&mut registers, &instructions);

        assert_eq!(registers.b, 26);
        Ok(())
    }
    #[test_log::test]
    fn testn_05() -> miette::Result<()> {
        let input = "Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0";
        let (mut registers, instructions) = parse(input);
        let output = run(&mut registers, &instructions);

        run(&mut registers, &instructions);

        assert_eq!(registers.b, 44354);
        Ok(())
    }

    #[test]
    fn test_real_input() -> miette::Result<()> {
        let input = include_str!("../../../../aoc_inputs/2024/day17input.txt");
        let result = include_str!("../../../../aoc_inputs/2024/day17result.txt")
            .lines()
            .next()
            .unwrap();
        assert_eq!(result, process(input)?);
        Ok(())
    }
}
