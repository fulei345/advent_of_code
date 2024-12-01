pub fn procces_part1(input: &str) -> String {
    let mut last: char = '\n';
    let vowels = vec!['a', 'e', 'i', 'o', 'u'];
    let result = input.lines()
    .map(|l| {
        let mut num: u8 = 0;
        let mut double = false;
        let _ = l.chars()
        .map(|c| {
            if vowels.contains(&c){
                num += 1;
            }
            if c == last{
                double = true;
            }
            last = c;
        });
        if num > 2 && double {
            1
        }
        else {
            0
        }
    }).sum::<u32>();
    result.to_string()
}

pub fn procces_part2(input: &str) -> String {
    input.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb";

    #[test]
    fn part1_works() {
        assert_eq!(procces_part1(INPUT), "2");
    }

    #[test]
    fn part2_works() {
        assert_eq!(procces_part2(INPUT), "6742839");
    }
}
