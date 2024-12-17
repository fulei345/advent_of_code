use glam::IVec2;
use pathfinding::prelude::*;
use std::collections::HashSet;

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    // Trim the input
    let input = _input.trim();
    let mut walls: HashSet<IVec2> = HashSet::new();
    let mut start = IVec2::new(0, 0);
    let mut end = IVec2::new(0, 0);

    // Find walls, start and end
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            let pos = IVec2::new(x as i32, y as i32);
            match c {
                '#' => {
                    walls.insert(pos);
                }
                'S' => {
                    start = pos;
                }
                'E' => {
                    end = pos;
                }
                _ => {}
            }
        }
    }
    let (result, _cost) = astar_bag(
        &(start, IVec2::X),
        |(position, direction)| {
            let next_pos = position + direction;
            if walls.contains(&next_pos) {
                vec![
                    ((*position, direction.perp()), 1000),
                    ((*position, -direction.perp()), 1000),
                ]
            } else {
                vec![
                    ((next_pos, *direction), 1),
                    ((*position, direction.perp()), 1000),
                    ((*position, -direction.perp()), 1000),
                ]
            }
        },
        |_| 0,
        |&(pos, _)| pos == end,
    )
    .expect("a valid aoc result");

    let set = result
        .flat_map(|path| path.into_iter().map(|(position, _)| position))
        .collect::<HashSet<IVec2>>();

    Ok(set.len().to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############

";
        assert_eq!("45", process(input)?);
        Ok(())
    }
}
