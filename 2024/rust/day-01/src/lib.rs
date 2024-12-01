pub fn procces_part1(input: &str) -> String {
    let mut firstcol: Vec<u32> = vec![];
    let mut secondcol: Vec<u32> = vec![];
    let _ = input.lines()
    .map(|l| {
        let both: Vec<u32> = l.split("   ")
        .map(|item| item.parse::<u32>().unwrap()).collect();
        firstcol.push(both[0]);
        secondcol.push(both[1]);
        dbg!(both);
    });
    firstcol.sort();
    secondcol.sort();

    let result: u32 = firstcol.iter().zip(secondcol.iter()).map(|(&f, &s)| f.abs_diff(s)).sum();
        
    result.to_string()
}

pub fn procces_part2(input: &str) -> String {
    let mut result = input
        .split("\n\n")
        .map(|elf_load| {
            elf_load
                .lines()
                .map(|item| item.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect::<Vec<_>>();
    result.sort_by(|a, b| b.cmp(a));
    let sum: u32 = result.iter().take(3).sum();
    sum.to_string()
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
        assert_eq!(result, "45000");
    }
}
