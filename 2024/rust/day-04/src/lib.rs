pub fn procces_part1(input: &str) -> String {
    // If we take each row, each column (140 + 140)

    "lol".to_string()
}

pub fn procces_part2(input: &str) -> String {
    "lol".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = 
"MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX";

    #[test]
    fn part1_works() {
        assert_eq!(procces_part1(INPUT1), "609043");
    }

    #[test]
    fn part2_works() {
        assert_eq!(procces_part2(INPUT1), "6742839");
    }
}
