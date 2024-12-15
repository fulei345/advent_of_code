use itertools::Itertools;

fn solve(x1: i64, x2: i64, y1: i64, y2: i64, z1: i64, z2: i64) -> i64 {
    let b = (z2 * x1 - z1 * x2) / (y2 * x1 - y1 * x2);
    let a = (z1 - b * y1) / x1;
    if (x1 * a + y1 * b, x2 * a + y2 * b) != (z1, z2) {
        return 0;
    }
    a * 3 + b
}

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let xs = _input
        .split(|c: char| !c.is_ascii_digit())
        .filter(|w| !w.is_empty())
        .map(|w| w.parse().unwrap())
        .tuples();

    let mut p1: i64 = 0;
    for (x1, x2, y1, y2, z1, z2) in xs {
        p1 += solve(x1, x2, y1, y2, z1, z2);
    }

    Ok(p1.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279

";
        assert_eq!("480", process(input)?);
        Ok(())
    }
}
