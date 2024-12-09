use glam::IVec2;
use itertools::enumerate;
use std::collections::HashSet;

enum Direction {
    North,
    East,
    South,
    West,
}

impl Direction {
    fn turn_right(&self) -> Direction {
        match self {
            Direction::North => Direction::East,
            Direction::East => Direction::South,
            Direction::South => Direction::West,
            Direction::West => Direction::North,
        }
    }
    fn to_ivec2(&self) -> IVec2 {
        match self {
            Direction::North => IVec2::NEG_Y,
            Direction::South => IVec2::Y,
            Direction::East => IVec2::X,
            Direction::West => IVec2::NEG_X,
        }
    }
}

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let mut direction = Direction::North;

    let mut obstacles: HashSet<IVec2> = HashSet::new();
    let mut visited_positions: HashSet<IVec2> = HashSet::new();
    let mut x_minmax: (i32, i32) = (0, 0);
    let mut y_minmax: (i32, i32) = (0, 0);
    let mut player_position: IVec2 = IVec2::new(0, 0);
    let mut count = 0;
    for (index, line) in enumerate(_input.lines()) {
        x_minmax.1 = line.len() as i32;
        count += 1;
        for (i, char) in enumerate(line.chars()) {
            match char {
                '#' => {
                    obstacles.insert(IVec2::new(i as i32, index as i32));
                    ()
                }
                '^' => {
                    visited_positions.insert(IVec2::new(i as i32, index as i32));
                    player_position = IVec2::new(i as i32, index as i32);
                }
                _ => (),
            }
        }
    }
    y_minmax.1 = count - 1;
    x_minmax.1 -= 1;

    while (x_minmax.0..=x_minmax.1).contains(&player_position.x)
        && (y_minmax.0..=y_minmax.1).contains(&player_position.y)
    {
        let next_position = player_position + direction.to_ivec2();
        if obstacles.get(&next_position).is_some() {
            direction = direction.turn_right();
        } else {
            player_position = next_position;
            visited_positions.insert(player_position);
        }
    }

    Ok((visited_positions.len() - 1).to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...";
        assert_eq!("41", process(input)?);
        Ok(())
    }

    #[test]
    fn test_real_input() -> miette::Result<()> {
        let input = include_str!("../../../../aoc_inputs/2024/day06input");
        let result = include_str!("../../../../aoc_inputs/2024/day06result")
            .lines()
            .next()
            .unwrap();
        assert_eq!(result, process(input)?);
        Ok(())
    }
}
