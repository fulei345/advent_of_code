use glam::IVec2;
use itertools::enumerate;
use std::collections::{HashMap, HashSet};

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let mut antinodes: HashSet<IVec2> = HashSet::new();
    let mut nodes: HashMap<char, Vec<IVec2>> = HashMap::new();

    let mut x_minmax: (i32, i32) = (0, 0);
    let mut y_minmax: (i32, i32) = (0, 0);
    let mut count = 0;

    for (index, line) in enumerate(_input.lines()) {
        x_minmax.1 = line.len() as i32;
        count += 1;
        for (i, char) in enumerate(line.chars()) {
            match char {
                '.' => (),
                _ => {
                    let new: IVec2 = IVec2::new(i as i32, index as i32);
                    let new_vec = vec![new];
                    nodes
                        .entry(char)
                        .and_modify(|vec| vec.push(new))
                        .or_insert(new_vec);
                }
            }
        }
    }
    y_minmax.1 = count;

    for (_, value) in nodes.clone().into_iter() {
        for first in value.clone() {
            for second in value.clone() {
                let dif = first - second;

                if dif != IVec2::ZERO {
                    let first_dif = first + dif;
                    let inside = (x_minmax.0..=x_minmax.1 - 1).contains(&first_dif.x)
                        && (y_minmax.0..=y_minmax.1 - 1).contains(&first_dif.y);
                    if inside {
                        antinodes.insert(first + dif);
                    }
                    let second_dif = second - dif;
                    let inside = (x_minmax.0..=x_minmax.1 - 1).contains(&second_dif.x)
                        && (y_minmax.0..=y_minmax.1 - 1).contains(&second_dif.y);
                    if inside {
                        antinodes.insert(second - dif);
                    }
                }
            }
        }
    }

    // for (index, line) in enumerate(_input.lines()) {
    //     for (i, char) in enumerate(line.chars()) {
    //         if antinodes.contains(&IVec2::new(i as i32, index as i32)) {
    //             print!("#");
    //         } else {
    //             print!("{}", char);
    //         }
    //     }
    //     println!("");
    // }
    Ok(antinodes.len().to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............";
        assert_eq!("14", process(input)?);
        Ok(())
    }
}
