use std::collections::HashMap;

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let mut stones: HashMap<String, usize> = HashMap::default();
    let mut two: HashMap<String, (String, String)> = HashMap::default();
    let mut one: HashMap<String, String> = HashMap::default();

    one.insert(String::from("0"), String::from("1"));

    for num in _input.split_whitespace() {
        stones.insert(num.to_string(), 1);
    }
    for _ in 0..25 {
        let mut new = stones.clone();
        for (number, count) in &stones {
            if number.len() % 2 == 0 {
                if two.contains_key(number) {
                    let (first, second) = two.get(number).unwrap();
                    new.entry((*first.clone()).to_string())
                        .and_modify(|f| *f += count)
                        .or_insert(*count);
                    new.entry((*second.clone()).to_string())
                        .and_modify(|f| *f += count)
                        .or_insert(*count);
                } else {
                    let half = number.len() / 2;
                    let first = number[0..half].to_string();
                    let second = number[half..].to_string();
                    let second: String = second.parse::<u64>().unwrap().to_string();
                    two.insert((*number).clone(), (first.clone(), second.clone()));

                    new.entry(first)
                        .and_modify(|f| *f += count)
                        .or_insert(*count);
                    new.entry(second)
                        .and_modify(|f| *f += count)
                        .or_insert(*count);
                }
            } else {
                if one.contains_key(number) {
                    let num = one.get(number).unwrap();
                    new.entry((*num.clone()).to_string())
                        .and_modify(|f| *f += count)
                        .or_insert(*count);
                } else {
                    // Should be odd here
                    let num = number.parse::<u64>().unwrap();
                    one.insert((*number).clone(), (num * 2024).to_string());

                    new.entry((num * 2024).to_string())
                        .and_modify(|f| *f += count)
                        .or_insert(*count);
                }
            }
            new.entry((*number.clone()).to_string())
                .and_modify(|f| *f -= count);
        }

        stones.clear();
        stones = new.clone();
        // dbg!(&stones);
    }

    let result: usize = stones.values().sum();

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
