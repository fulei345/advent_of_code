pub fn procces_part1(input: &str) -> String {
    let mut seen_places = vec![(0, 0)];
    let mut y: i32 = 0;
    let mut x: i32 = 0;
    for c in input.chars(){
        match c {
            '>' => x += 1,
            '<' => x -= 1,
            '^' => y += 1,
            'v' => y -= 1,
            _ => panic!("Invalid charachter {c}")
        }
        let new_point = (x, y);
        if !seen_places.contains(&new_point){
            seen_places.push(new_point);
        }
    }
    seen_places.len().to_string()
}

pub fn procces_part2(input: &str) -> String {
    let mut seen_places = vec![(0, 0)];
    let mut santa = (0, 0);
    let mut robot = (0, 0);

    let result = input.chars()
    .enumerate()
    .map(|(i, c)| {
        let current = if i % 2 == 0 {&mut santa} else {&mut robot};
        match c {
            '>' => current.0 += 1,
            '<' => current.0 -= 1,
            '^' => current.1 += 1,
            'v' => current.1 -= 1,
            _ => panic!("Invalid charachter {c}")
        }
        if !seen_places.contains(current){
            seen_places.push((current.0, current.1));
            1
        }
        else {
            0
        }
    }).sum::<u128>();

    (result + 1).to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = "^>";
    const INPUT2: &str = "^>v<";
    const INPUT3: &str = "^v^v^v^v^v";

    #[test]
    fn part1_works() {
        assert_eq!(procces_part1(INPUT1), "3");
        assert_eq!(procces_part1(INPUT2), "4");
        assert_eq!(procces_part1(INPUT3), "2");
    }

    #[test]
    fn part2_works() {
        assert_eq!(procces_part2(INPUT1), "3");
        assert_eq!(procces_part2(INPUT2), "3");
        assert_eq!(procces_part2(INPUT3), "11");
    }
}
