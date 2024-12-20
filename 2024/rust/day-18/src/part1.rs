use glam::{IVec2, UVec2};
use pathfinding::prelude::*;
use std::collections::HashSet;

const GRID_SIZE: IVec2 = if cfg!(test) {
    IVec2::splat(6)
} else {
    IVec2::splat(70)
};

const DIRECTIONS: [IVec2; 4] = [IVec2::X, IVec2::Y, IVec2::NEG_X, IVec2::NEG_Y];

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    // Trim the input
    let input = _input.trim();
    let mut obstacles: Vec<IVec2> = Vec::new();

    // Find obstacles, start and end
    for line in input.lines() {
        let parts: Vec<&str> = line.split(',').collect();
        let x = parts[0].parse::<i32>().unwrap();
        let y = parts[1].parse::<i32>().unwrap();
        let pos = IVec2::new(x, y);
        obstacles.push(pos);
    }

    let result = find_shortest_path(obstacles, 0, GRID_SIZE.x);

    Ok(result.to_string())
}

fn find_shortest_path(obstacles: Vec<IVec2>, bytes: u64, size: i32) -> u64 {
    let end = obstacles.len().min(if cfg!(test) { 12 } else { 1024 });

    let start = IVec2::new(0, 0);
    // let end = IVec2::new(size, size);
    let result = dijkstra(
        &start,
        |position| {
            DIRECTIONS
                .iter()
                .filter_map(|dir| {
                    let next_pos = position + dir;
                    if !((0..=GRID_SIZE.x).contains(&next_pos.x)
                        && (0..=GRID_SIZE.y).contains(&next_pos.y))
                    {
                        return None;
                    }
                    if !obstacles[0..end].contains(&next_pos) {
                        Some((next_pos, 1usize))
                    } else {
                        None
                    }
                })
                .collect::<Vec<_>>()
        },
        |&p| p == GRID_SIZE,
    );

    result.unwrap().1 as u64
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0


";
        assert_eq!("22", process(input)?);
        Ok(())
    }
}
