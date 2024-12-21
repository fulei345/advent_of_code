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

    // run first pathfind
    let (original_path, original_cost) = dijkstra(
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

    let result = original_path
        .iter()
        .enumerate()
        .tuple_combinations()
        .filter_map(|((start_cost, start_pos), (end_cost, end_pos))| {
            let distance: usize = (start_pos - end_pos).abs().element_sum() as usize;
            if distance > 20 {
                return None;
            };
            let cheat_cost = start_cost + distance + original_cost - end_cost;
            Some(original_cost - cheat_cost)
        })
        .filter(|savings| savings >= &100)
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
