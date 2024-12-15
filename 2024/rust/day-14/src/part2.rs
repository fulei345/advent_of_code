pub fn f2(s: &str, w: i64, h: i64) -> i64 {
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

    let mut res = 0;
    for steps in 1..10_000 {
        let mut g = [[' '; 101]; 103];
        for &(x, y, vx, vy) in robots.iter() {
            let x1 = (w + (x + vx * steps) % w) % w;
            let y1 = (h + (y + vy * steps) % h) % h;
            g[y1 as usize][x1 as usize] = '#';
        }
        let good =
            (0..w as usize).any(|x| (0..h as usize).filter(|&y| g[y][x] == '#').count() > 34);
        if !good {
            continue;
        }

        // println!("----{steps}----");
        // for y in 0..h as usize {
        //     for x in 0..w as usize {
        //         print!("{}", g[y][x]);
        //     }
        //     println!();
        // }

        if good {
            res = steps;
            break;
        }
    }
    res
}

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    Ok(f2(_input, 101, 103).to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        todo!("haven't built test yet");
        let input = "";
        assert_eq!("", process(input)?);
        Ok(())
    }
}
