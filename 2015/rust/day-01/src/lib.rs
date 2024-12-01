pub fn procces_part1(input: &str) -> String {
    let result: i32 = input
        .chars()
        .map(|c| match c {
            '(' => 1,
            ')' => -1,
            '\n' => 0,
            _ => panic!("Lol {}", c),
        })
        .sum();
    result.to_string()
}

pub fn procces_part2(input: &str) -> String {
    let result: usize = input
    .chars()
    .scan(0, |floor,c |{
        *floor = match c {
            '(' => *floor + 1,
            ')' => *floor - 1,
            _ => panic!(),
        };
        Some(*floor)
    })
    .enumerate()
    .find(|&(_, floor)| floor < 0)
    .unwrap()
    .0 + 1;
    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = "(())";
    const INPUT2: &str = "(()(()(";
    const INPUT3: &str = "))(((((";
    const INPUT4: &str = ")())())";

    #[test]
    fn part1_works() {
        assert_eq!(procces_part1(INPUT1), "0");
        assert_eq!(procces_part1(INPUT2), "3");
        assert_eq!(procces_part1(INPUT3), "3");
        assert_eq!(procces_part1(INPUT4), "-3");
    }
    
    #[test]
    fn part2_works() {
        assert_eq!(procces_part2(")"), "1");
        assert_eq!(procces_part2("()())"), "5");
    }
}