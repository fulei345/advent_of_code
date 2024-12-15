pub fn f1(s: &str, w: i64, h: i64) -> i64 {
    let robots: Vec<(i64, i64, i64, i64)> = s
        .lines()
        .map(|l| {
            let l: Vec<_> = l
                .split(['=', ',', ' ', 'v'])
                .skip(1)
                .filter(|&x| x != "")
                .map(|x| x.parse::<i64>().expect("must be a number"))
                .collect();
            (l[0], l[1], l[2], l[3])
        })
        .collect();

    let mut q = [0, 0, 0, 0];
    let rx = [0..w / 2, w / 2 + 1..w];
    let ry = [0..h / 2, h / 2 + 1..h];
    let steps = 100;
    for &(x, y, vx, vy) in robots.iter() {
        let x1 = (w + (x + vx * steps) % w) % w;
        let y1 = (h + (y + vy * steps) % h) % h;
        let (mut qx, mut qy) = (3, 3);
        for i in 0..=1 {
            if rx[i].contains(&x1) {
                qx = i
            }
            if ry[i].contains(&y1) {
                qy = i
            }
        }
        if qx < 3 && qy < 3 {
            q[qy * 2 + qx] += 1;
        }
    }
    q[0] * q[1] * q[2] * q[3]
}

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    Ok(f1(_input, 101, 103).to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "lol";
        assert_eq!("", process(input)?);
        Ok(())
    }
}
