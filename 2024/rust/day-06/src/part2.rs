use glam::IVec2;
use itertools::enumerate;
use std::collections::HashSet;

#[derive(PartialEq, Eq, Hash, Clone, Copy, Debug)]
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
    let mut visited_positions: HashSet<(IVec2, Direction)> = HashSet::new();
    let mut bottom_right: IVec2 = IVec2::new(0, 0);
    let mut player_position: IVec2 = IVec2::new(0, 0);
    let mut start_position: (IVec2, Direction) = (IVec2::new(0, 0), Direction::North);
    let mut count = 0;

    for (index, line) in enumerate(_input.lines()) {
        bottom_right.x = line.len() as i32;
        count += 1;
        for (i, char) in enumerate(line.chars()) {
            match char {
                '#' => {
                    obstacles.insert(IVec2::new(i as i32, index as i32));
                    ()
                }
                '^' => {
                    let pos = IVec2::new(i as i32, index as i32);
                    visited_positions.insert((pos, direction));
                    start_position = (pos, Direction::North);
                    player_position = pos;
                }
                _ => (),
            }
        }
    }
    bottom_right.y = count;

    while (0..bottom_right.x).contains(&player_position.x)
        && (0..bottom_right.y).contains(&player_position.y)
    {
        let next_position = player_position + direction.to_ivec2();
        if obstacles.get(&next_position).is_some() {
            direction = direction.turn_right();
        } else {
            player_position = next_position;
            visited_positions.insert((player_position, direction));
        }
    }
    let mut result = 0;
    visited_positions.remove(&start_position);
    for (start_pos, dir) in visited_positions.clone() {
        if check_loop(&obstacles, start_pos, dir, bottom_right) {
            result += 1;
        }
    }

    Ok((result).to_string())
}

fn check_loop(
    obstacles: &HashSet<IVec2>,
    mut player_position: IVec2,
    mut direction: Direction,
    bottom_right: IVec2,
) -> bool {
    let new_obstacle = player_position.clone() + direction.to_ivec2();

    let mut new_positions: HashSet<(IVec2, Direction)> = HashSet::new();

    while (0..bottom_right.x).contains(&player_position.x)
        && (0..bottom_right.y).contains(&player_position.y)
    {
        let next_position = player_position + direction.to_ivec2();

        if new_positions.contains(&(next_position, direction)) {
            return true;
        } else {
            new_positions.insert((next_position, direction));
        }

        if obstacles.get(&next_position).is_some() || next_position == new_obstacle {
            direction = direction.turn_right();
        } else {
            player_position = next_position;
        }
    }
    false
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
        assert_eq!("6", process(input)?);
        Ok(())
    }

    #[test]
    fn test_real_input() -> miette::Result<()> {
        let input = include_str!("../../../../aoc_inputs/2024/day06input.txt");
        let result = include_str!("../../../../aoc_inputs/2024/day06result.txt")
            .lines()
            .last()
            .unwrap();
        assert_eq!(result, process(input)?);
        Ok(())
    }
}
