use itertools::Itertools;

pub fn procces_part1(input: &str) -> String {
    let result: u16 = input
        .lines()
        .map(|line| {
            let levels: Vec<i16> = line
                .split_whitespace()
                .map(|num| num.parse::<i16>().unwrap())
                .collect();

            procces_line(levels) as u16
        })
        .sum();
    result.to_string()
}

fn procces_line(nums: Vec<i16>) -> bool {
    let all_windows = nums.iter().tuple_windows();
    let not_for = all_windows
        .clone()
        .all(|(first, second)| (1 <= (first - second).abs()) && (first - second).abs() <= 3);

    let increasing = all_windows.clone().all(|(first, second)| first < second);
    let decreasing = all_windows.clone().all(|(first, second)| first > second);
    not_for && (increasing || decreasing)
}

pub fn procces_part2(input: &str) -> String {
    let result: u16 = input
        .lines()
        .map(|line| {
            let levels: Vec<i16> = line
                .split_whitespace()
                .map(|num| num.parse::<i16>().unwrap())
                .collect();

            let mut is_safe = procces_line(levels.clone());
            if !is_safe {
                // Try Every possible combination
                for i in 0..levels.clone().len(){
                    let new = [&levels[..i], &levels[i+1..]].concat();
                    is_safe = procces_line(new);
                    if is_safe {break}
                }
            }
            is_safe as u16
        })
        .sum();
    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = "7 6 4 2 1";
    const INPUT2: &str = "1 2 7 8 9";
    const INPUT3: &str = "9 7 6 2 1";
    const INPUT4: &str = "1 3 2 4 5";
    const INPUT5: &str = "8 6 4 4 1";
    const INPUT6: &str = "1 3 6 7 9";

    #[test]
    fn part1_works() {
        assert_eq!(procces_part1(INPUT1), "1");
        assert_eq!(procces_part1(INPUT2), "0");
        assert_eq!(procces_part1(INPUT3), "0");
        assert_eq!(procces_part1(INPUT4), "0");
        assert_eq!(procces_part1(INPUT5), "0");
        assert_eq!(procces_part1(INPUT6), "1");
    }

    #[test]
    fn part2_works() {
        assert_eq!(procces_part2(INPUT1), "1");
        assert_eq!(procces_part2(INPUT2), "0");
        assert_eq!(procces_part2(INPUT3), "0");
        assert_eq!(procces_part2(INPUT4), "1");
        assert_eq!(procces_part2(INPUT5), "1");
        assert_eq!(procces_part2(INPUT6), "1");
    }
}
