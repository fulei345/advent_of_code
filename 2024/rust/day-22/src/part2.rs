use itertools::Itertools;
use std::collections::HashMap;

fn simulate_secrets(mut secret: i64, iterations: i64) -> (Vec<i64>, Vec<i64>) {
    let mut secrets = vec![];
    let mut differneces: Vec<i64> = vec![];
    for _ in 0..iterations {
        let previous = secret;
        secret ^= secret * 64;
        secret &= 16777216 - 1;

        secret ^= secret / 32;
        secret &= 16777216 - 1;

        secret ^= secret * 2048;
        secret &= 16777216 - 1;

        secrets.push(secret % 10);
        differneces.push((secret % 10) - (previous % 10));
    }

    (secrets, differneces)
}

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let input = input.trim();
    let secrets = input.lines().map(|num| num.parse::<i64>().unwrap());

    let mut sales = HashMap::new();

    secrets.for_each(|secret| {
        let (prices, changes) = simulate_secrets(secret, 2000);
        let mut bananas = HashMap::new();
        let n = prices.len();
        for i in 3..n {
            let sequence = &changes[i - 3..=i];
            let price = prices[i];
            if !bananas.contains_key(&sequence) {
                bananas.insert(sequence, price);
            }
        }
        for (k, v) in bananas {
            let key = k.iter().join(",");
            //sales.insert(key, v);
            *sales.entry(key).or_insert(0) += v;
        }
    });

    Ok(sales
        .iter()
        .max_by(|a, b| a.1.cmp(&b.1))
        .unwrap()
        .1
        .to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "
1
2
3
2024


";
        assert_eq!("23", process(input)?);
        Ok(())
    }
}
