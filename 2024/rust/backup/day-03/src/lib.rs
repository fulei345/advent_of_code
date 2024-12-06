use regex::Regex;

pub fn procces_part1(input: &str) -> String {
    let re = Regex::new(r"mul\((\d+),\s*(\d+)\)").unwrap();
    let sum: i32 = re
        .captures_iter(input)
        .map(|caps| {
            let x: i32 = caps[1].parse().unwrap();
            let y: i32 = caps[2].parse().unwrap();
            x * y
        })
        .sum();

    sum.to_string()
}

pub fn procces_part2(input: &str) -> String {
    let all = find_all(input);
    let mut active = true;
    let mut sum = 0;
    for s in all {
        match s.as_str() {
            "do()" => active = true,
            "don't()" => active = false,
            _ => {
                if active {
                    let re = Regex::new(r"mul\((\d+),\s*(\d+)\)").unwrap();
                    let caps = re.captures(&s).unwrap();
                    let x: i32 = caps[1].parse().unwrap();
                    let y: i32 = caps[2].parse().unwrap();
                    sum += x * y;
                }
            }
        }
    }

    sum.to_string()
}

pub fn find_all(input: &str) -> Vec<String> {
    let re = Regex::new(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))").unwrap();

    re.captures_iter(input)
        .map(|caps| caps[0].to_string())
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
    const INPUT2: &str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";
    const INPUT3: &str = "(32,64]then(mul(11,8)mul(8,5))";

    #[test]
    fn part1_works() {
        assert_eq!(procces_part1(INPUT1), "161");
        assert_eq!(procces_part1(INPUT2), "161");
        assert_eq!(procces_part1(INPUT3), "128");
    }

    #[test]
    fn part2_works() {
        assert_eq!(procces_part2(INPUT1), "161");
        assert_eq!(procces_part2(INPUT2), "48");
        assert_eq!(procces_part2(INPUT3), "128");
    }
}
