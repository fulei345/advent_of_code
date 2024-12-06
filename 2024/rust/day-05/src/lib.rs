use std::cmp::Ordering;

#[derive(PartialEq, Eq, PartialOrd)]
struct Update{
    num: String,
    before: Vec<String>
}

impl Ord for Update{
    fn cmp(&self, other: &Self) -> Ordering {
        if self.num == other.num{
            Ordering::Equal
        }
        else if self.before.contains(&other.num){
            Ordering::Less
        }
        else if other.before.contains(&self.num) {
            Ordering::Greater
        }
        else {
            Ordering::Equal
        }
    }
    
}

pub fn procces_part1(input: &str) -> String {
    let mut all = input.split("\n\n");
    let rules = all.next().unwrap();
    let pages =all.next().unwrap();

    let updates: Vec<Update> = vec![];


    
    "lol".to_string()
}

pub fn procces_part2(input: &str) -> String {
    input.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47";

    #[test]
    fn part1_works() {
        assert_eq!(procces_part1(INPUT), "2");
    }

    #[test]
    fn part2_works() {
        assert_eq!(procces_part2(INPUT), "6742839");
    }
}
