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

// pub fn procces_part2(input: &str) -> String {
//     let result: u32 = input
//         .lines()
//         .map(|line| {
//             let moves: Vec<&str> = line.split(" ").collect();
//             let opponent_move = moves[0].parse::<Move>().unwrap();
//             match moves[1] {
//                 "X" => {
//                     let our_move = match opponent_move {
//                         Move::Rock => Move::Scissors,
//                         Move::Paper => Move::Rock,
//                         Move::Scissors => Move::Paper,
//                     };
//                     our_move as u32
//                 }
//                 "Y" => 3 + opponent_move as u32,
//                 "Z" => {
//                     let our_move = match opponent_move {
//                         Move::Rock => Move::Paper,
//                         Move::Paper => Move::Scissors,
//                         Move::Scissors => Move::Rock,
//                     };
//                     6 + our_move as u32
//                 }
//                 _ => {
//                     panic!("Unexpected response");
//                 }
//             }
//         })
//         .sum();
//     result.to_string()
// }

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
    //
    // #[test]
    // fn part2_works() {
    //     let result = procces_part2(INPUT1);
    //     assert_eq!(result, "12");
    // }
}
