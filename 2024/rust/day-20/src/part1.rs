use glam::IVec2;
use itertools::Itertools;
use miette::miette;
use nom_locate::LocatedSpan;
use pathfinding::prelude::*;
use std::{
    collections::{HashMap, HashSet},
    fmt::{self, Write},
    ops::Not,
};
use tracing::info;

pub struct Map {
    pub start: IVec2,
    pub end: IVec2,
    pub walls: HashSet<IVec2>,
}

const DIRECTIONS: [IVec2; 4] = [IVec2::X, IVec2::Y, IVec2::NEG_X, IVec2::NEG_Y];

#[tracing::instrument(skip(input))]
pub fn process(input: &str) -> miette::Result<String> {
    let input = input.trim();
    let mut walls = HashSet::new();
    let mut start = IVec2::ZERO;
    let mut end = IVec2::ZERO;
    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            match c {
                '#' => {
                    walls.insert(IVec2::new(x as i32, y as i32));
                }
                'S' => {
                    start = IVec2::new(x as i32, y as i32);
                }
                'E' => {
                    end = IVec2::new(x as i32, y as i32);
                }
                _ => {}
            }
        }
    }

    // let map: Map = Map { start, end, walls };

    let x_max = walls.iter().map(|pos| pos.x).max().unwrap();
    let y_max = walls.iter().map(|pos| pos.y).max().unwrap();
    // run first pathfind
    let first_run = dijkstra(
        &start,
        |position| {
            DIRECTIONS
                .iter()
                .filter_map(|direction| {
                    let next_pos = position + direction;
                    walls.contains(&next_pos).not().then_some((next_pos, 1))
                })
                .collect::<Vec<_>>()
        },
        |&pos| pos == end,
    )
    .expect("a valid aoc result");

    // dbg!(first_run.1);

    // run each pathfind with one missing wall
    // if that wall has at least two empty sides.
    let result = walls
        .iter()
        .filter(|wall| {
            DIRECTIONS
                .iter()
                .filter(|direction| {
                    let next_pos = **wall + **direction;
                    (0..x_max).contains(&next_pos.x)
                        && (0..y_max).contains(&next_pos.y)
                        && walls.contains(&next_pos).not()
                })
                .count()
                >= 2
        })
        .filter_map(|wall| {
            dijkstra(
                &start,
                |position| {
                    DIRECTIONS
                        .iter()
                        .filter_map(|direction| {
                            let next_pos = position + direction;
                            (next_pos == *wall || walls.contains(&next_pos).not())
                                .then_some((next_pos, 1))
                        })
                        .collect::<Vec<_>>()
                },
                |&pos| pos == end,
            )
            .map(|(path, cost)| (path, cost, wall))
        })
        .map(|(_path, cost, _wall)| first_run.1 - cost)
        .filter(|cost| cost >= &100)
        .count();

    Ok(result.to_string())
}

pub type Span<'a> = LocatedSpan<&'a str>;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "###############
#...#...12....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############";
        assert_eq!("", process(input)?);
        Ok(())
    }
}
