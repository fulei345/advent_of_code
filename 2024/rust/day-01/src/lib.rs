use std::collections::HashMap;

pub fn procces_part1(input: &str) -> String {
    let mut left = vec![];
    let mut right = vec![];


    for line in input.lines() {
        let mut items = line.split_whitespace();
        left.push(
            items.next().unwrap().parse::<i32>().unwrap(),
        );
        right.push(
            items.next().unwrap().parse::<i32>().unwrap(),
        );
    }

    left.sort();
    right.sort();

    let result: i32 = std::iter::zip(left, right)
        .map(|(l, r)| (l - r).abs())
        .sum();
        
    result.to_string()
}

pub fn procces_part2(input: &str) -> String {
    let mut left = vec![];
    let mut right: HashMap<usize, usize> = HashMap::new();

    for line in input.lines() {
        let mut items = line.split_whitespace();
        left.push(
            items.next().unwrap().parse::<usize>().unwrap(),
        );
        right
            .entry(
                items
                    .next()
                    .unwrap()
                    .parse::<usize>()
                    .unwrap(),
            )
            .and_modify(|v| {
                *v += 1;
            })
            .or_insert(1);
    }

    let result: usize = left
        .iter()
        .map(|number| {
            number * right.get(number).unwrap_or(&0)
        })
        .sum();

    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "3   4
4   3
2   5
1   3
3   9
3   3";

    #[test]
    fn part1_works() {
        let result = procces_part1(INPUT);
        assert_eq!(result, "11");
    }

    #[test]
    fn part2_works() {
        let result = procces_part2(INPUT);
        assert_eq!(result, "31");
    }
}
