use std::{
    collections::{BTreeSet, HashMap},
    fmt::Display,
};

#[derive(Copy, Clone, Eq, PartialEq, Debug)]
enum Operator {
    And,
    Or,
    Xor,
}

impl Operator {
    fn evaluate(&self, left: bool, right: bool) -> bool {
        match self {
            Operator::And => left && right,
            Operator::Or => left || right,
            Operator::Xor => left ^ right,
        }
    }

    fn from_str(op: &str) -> Self {
        match op {
            "AND" => Operator::And,
            "OR" => Operator::Or,
            "XOR" => Operator::Xor,
            _ => panic!("unknown operator {op}"),
        }
    }
}

impl Display for Operator {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "{}",
            match self {
                Operator::And => "AND",
                Operator::Or => "OR",
                Operator::Xor => "XOR",
            }
        )
    }
}

#[derive(Eq, PartialEq, Debug)]
struct Expression<'a> {
    left: &'a str,
    operator: Operator,
    right: &'a str,
    output: &'a str,
    evaluated: bool,
}

impl<'a> Expression<'a> {
    fn new(left: &'a str, operator: Operator, right: &'a str, output: &'a str) -> Self {
        let (left, right) = if left < right {
            (left, right)
        } else {
            (right, left)
        };
        Expression {
            left,
            operator,
            right,
            output,
            evaluated: false,
        }
    }

    fn evaluate(&mut self, store: &mut HashMap<&'a str, Option<bool>>) {
        if !self.evaluated {
            if let Some(left) = store[self.left] {
                if let Some(right) = store[self.right] {
                    if store[self.output].is_none() {
                        store.insert(self.output, Some(self.operator.evaluate(left, right)));
                    }
                    self.evaluated = true;
                }
            }
        }
    }

    fn is_input(&self, input: &str) -> bool {
        self.left == input || self.right == input
    }

    fn is_output(&self, output: &str) -> bool {
        self.output == output
    }
}

impl<'a> TryFrom<&'a str> for Expression<'a> {
    type Error = String;

    fn try_from(value: &'a str) -> Result<Self, Self::Error> {
        let tokens: Vec<&str> = value.split_whitespace().collect();
        if tokens.len() == 5 {
            let op = Operator::from_str(tokens[1]);
            Ok(Self::new(tokens[0], op, tokens[2], tokens[4]))
        } else {
            Err(format!("cannot parse {value}"))
        }
    }
}

impl Display for Expression<'_> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "{} {} {} -> {}",
            self.left, self.operator, self.right, self.output
        )
    }
}

// dumb works well enough
fn part1(input: &str) -> u64 {
    let mut store: HashMap<&str, Option<bool>> = HashMap::new();
    let parts: Vec<&str> = input.split("\n\n").collect();

    for line in parts[0].lines() {
        let init: Vec<&str> = line.split(": ").collect();
        store.insert(init[0], Some(init[1] == "1"));
    }

    let mut expressions: Vec<Expression> = parts[1]
        .lines()
        .map(|line| {
            let e = Expression::try_from(line).unwrap();
            store.entry(e.left).or_insert(None);
            store.entry(e.right).or_insert(None);
            store.entry(e.output).or_insert(None);

            e
        })
        .collect();

    while !expressions.is_empty() {
        for e in &mut expressions {
            e.evaluate(&mut store);
        }
        // should check instead whether all z stores are evaluated
        expressions.retain(|e| !e.evaluated);

        if store
            .iter()
            .filter(|(k, _)| k.starts_with('z'))
            .all(|(_, v)| v.is_some())
        {
            break;
        }
    }

    let mut zs: Vec<(&str, Option<bool>)> = store
        .into_iter()
        .filter(|(k, _)| k.starts_with('z'))
        .collect();
    zs.sort();
    zs.reverse();

    zs.into_iter()
        .fold(0, |acc, (_, v)| acc * 2 + if v.unwrap() { 1 } else { 0 })
}

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let input = input.trim();
    let result = part1(input);

    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02";
        assert_eq!("4", process(input)?);
        Ok(())
    }

    #[test]
    fn test_bigger() -> miette::Result<()> {
        let input = "
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj";
        assert_eq!("2024", process(input)?);
        Ok(())
    }
}
