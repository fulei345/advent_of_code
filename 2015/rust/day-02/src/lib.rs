pub fn procces_part1(input: &str) -> String {
    let result: u32 = input
        .lines()
        .map(|line| {
            let sides: Vec<_> = line.split("x").map(|s| s.parse::<u32>().unwrap()).collect();
            let summation: Vec<u32> = vec![
                2 * sides[0] * sides[1],
                2 * sides[1] * sides[2],
                2 * sides[2] * sides[0],
            ];
            summation.clone().into_iter().sum::<u32>() + summation.into_iter().min().unwrap() / 2
        })
        .sum();
    result.to_string()
}

pub fn procces_part2(input: &str) -> String {
    let result: u32 = input
        .lines()
        .map(|line| {
            let mut sides: Vec<_> = line.split("x").map(|s| s.parse::<u32>().unwrap()).collect();
            sides.sort();
            let mul = sides[0] * sides[1] * sides[2];
            mul + 2 * sides[0] + 2 * sides[1]
        })
        .sum();
    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "2x3x4
1x1x10";

    #[test]
    fn part1_works() {
        let result = procces_part1(INPUT);
        assert_eq!(result, "101");
    }

    #[test]
    fn part2_works() {
        let result = procces_part2(INPUT);
        assert_eq!(result, "48");
    }
}
