fn simulate_secrets(mut secret: u128, iterations: u128) -> u128 {
    for _ in 0..iterations {
        let v1 = secret * 64;
        secret ^= v1;
        secret &= 16777216 - 1;

        let v2 = secret / 32;
        secret ^= v2;
        secret &= 16777216 - 1;

        let v3 = secret * 2048;
        secret = secret ^ v3;
        secret &= 16777216 - 1;
    }

    secret
}

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let input = input.trim();
    let secrets = input.lines().map(|num| num.parse::<u128>().unwrap());

    let result: u128 = secrets.map(|secret| simulate_secrets(secret, 2000)).sum();
    Ok(result.to_string())
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
        assert_eq!("37327623", process(input)?);
        Ok(())
    }
}
