use std::collections::HashMap;

fn count(stone: u128, steps: u128, map: &mut HashMap<(u128, u128), u128>) -> u128 {
    if map.contains_key(&(stone, steps)) {
        return map[&(stone, steps)];
    }
    let result;
    let string = stone.to_string();
    let lenght: usize = string.len();
    if steps == 0 {
        result = 1;
    } else if stone == 0 {
        result = count(1, steps - 1, map);
    } else if lenght % 2 == 0 {
        let base: u128 = 10;
        let divisor = base.pow((lenght / 2) as u32);

        let first_half = stone / divisor; // First half
        let second_half = stone % divisor; // Second half
        result = count(first_half, steps - 1, map) + count(second_half, steps - 1, map);
    } else {
        result = count(stone * 2024, steps - 1, map);
    }
    map.insert((stone, steps), result);
    return result;
}

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let mut map: HashMap<(u128, u128), u128> = HashMap::new();
    const ITERATIONS: u128 = 25;

    let stones = input
        .trim()
        .split(" ")
        .map(|num| num.parse::<u128>().unwrap());

    let result: u128 = stones.map(|stone| count(stone, ITERATIONS, &mut map)).sum();
    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "125 17";
        assert_eq!("55312", process(input)?);
        Ok(())
    }
}
