// Using fold with an accumilator

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let result = itertools::fold(_input.lines(), 0, |a, line| {
        let mut parts = line.split(":");
        let total = parts.next().unwrap().parse::<usize>().unwrap();
        let numbers: Vec<usize> = parts
            .next()
            .unwrap()
            .trim()
            .split(" ")
            .map(|n| n.parse::<usize>().unwrap())
            .collect();

        if check_line(&numbers, total) {
            total + a
        } else {
            a
        }
    });
    Ok(result.to_string())
}

fn check_line(nums: &[usize], current_total: usize) -> bool {
    if nums.is_empty() {
        return current_total == 0;
    }
    let last = nums.last().unwrap();
    if current_total == *last {
        return true;
    }
    let last = nums.last().unwrap();
    let modulo = current_total % last;
    if modulo == 0 {
        return check_line(&nums[..nums.len() - 1], current_total / last);
    }
    if current_total > *last {
        return check_line(&nums[..nums.len() - 1], current_total - last);
    }
    return false;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20";
        assert_eq!("3749", process(input)?);
        Ok(())
    }
}
