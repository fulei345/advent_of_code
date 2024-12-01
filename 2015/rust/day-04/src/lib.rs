use md5;

pub fn procces_part1(input: &str) -> String {
    let mut i = 1;
    loop {
        let s = format!("{input}{i}");
        let result = md5::compute(s);
        if &format!("{:x}", result)[..5] == "00000"
        {
            break;
        }
        i += 1;
    }
    i.to_string()
}

pub fn procces_part2(input: &str) -> String {
    let mut i = 1;
    loop {
        let s = format!("{input}{i}");
        let result = md5::compute(s);
        if &format!("{:x}", result)[..6] == "000000"
        {
            break;
        }
        i += 1;
    }
    i.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = "abcdef";
    const INPUT2: &str = "pqrstuv";

    #[test]
    fn part1_works() {
        assert_eq!(procces_part1(INPUT1), "609043");
        assert_eq!(procces_part1(INPUT2), "1048970");
    }

    #[test]
    fn part2_works() {
        assert_eq!(procces_part2(INPUT1), "6742839");
        assert_eq!(procces_part2(INPUT2), "5714438");
    }
}
