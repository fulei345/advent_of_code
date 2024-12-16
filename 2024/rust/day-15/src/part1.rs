use glam::IVec2;
use std::collections::HashSet;

enum Direction {
    North,
    South,
    East,
    West,
}

#[derive(Debug, Eq, PartialEq, Hash, Clone, Copy)]
enum Tile {
    Wall(IVec2),
    Robot(IVec2),
    Box(IVec2),
}

impl Tile {
    fn pos(&self) -> IVec2 {
        match self {
            Tile::Wall(pos) => *pos,
            Tile::Robot(pos) => *pos,
            Tile::Box(pos) => *pos,
        }
    }
}

impl Direction {
    fn to_vec(&self) -> IVec2 {
        match self {
            Direction::North => IVec2::new(0, -1),
            Direction::South => IVec2::new(0, 1),
            Direction::East => IVec2::new(1, 0),
            Direction::West => IVec2::new(-1, 0),
        }
    }

    fn from_char(c: char) -> Option<Self> {
        match c {
            '^' => Some(Direction::North),
            'v' => Some(Direction::South),
            '>' => Some(Direction::East),
            '<' => Some(Direction::West),
            _ => None,
        }
    }
}

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    // Trim the input
    let input = _input.trim();
    // Hashset with the walls
    let mut obstacles: HashSet<Tile> = HashSet::new();
    let mut both = input.split("\n\n");

    if let Some(map) = both.next() {
        obstacles = map
            .lines()
            .enumerate()
            .flat_map(|(y, line)| {
                line.chars().enumerate().filter_map(move |(x, c)| match c {
                    'O' => Some(Tile::Box(IVec2::new(x as i32, y as i32))),
                    '#' => Some(Tile::Wall(IVec2::new(x as i32, y as i32))),
                    '@' => Some(Tile::Robot(IVec2::new(x as i32, y as i32))),
                    _ => None,
                })
            })
            .collect();
    }
    let mut robot_pos = obstacles
        .iter()
        .find(|tile| matches!(tile, Tile::Robot(_)))
        .unwrap()
        .clone();
    // Remove the robot from the obstacles
    obstacles.remove(&robot_pos);

    let mut directions = Vec::new();
    if let Some(dirs) = both.next() {
        directions = dirs.chars().filter_map(Direction::from_char).collect();
    }

    for dir in directions {
        // Print the obstacles and the robot
        // for y in 0..10 {
        //     for x in 0..10 {
        //         let pos = IVec2::new(x, y);
        //         if obstacles.contains(&Tile::Wall(pos)) {
        //             print!("#");
        //         } else if robot_pos == Tile::Robot(pos) {
        //             print!("@");
        //         } else if obstacles.contains(&Tile::Box(pos)) {
        //             print!("O");
        //         } else {
        //             print!(".");
        //         }
        //     }
        //     println!();
        // }
        let new_pos = robot_pos.pos() + dir.to_vec();
        if obstacles.contains(&Tile::Wall(new_pos)) {
            continue;
        }
        let mut new_box_pos = new_pos;
        let mut we_pushed_box = false;
        let mut we_hit_wall = false;
        while obstacles.contains(&Tile::Box(new_box_pos)) {
            new_box_pos = new_box_pos + dir.to_vec();
            we_pushed_box = true;
            // If we hit a wall we cannot move the box
            if obstacles.contains(&Tile::Wall(new_box_pos)) {
                we_hit_wall = true;
                break;
            }
        }
        if we_hit_wall {
            continue;
        }
        if we_pushed_box {
            obstacles.remove(&Tile::Box(new_pos));
            obstacles.insert(Tile::Box(new_box_pos));
        }
        robot_pos = Tile::Robot(new_pos);
    }

    let result = obstacles
        .iter()
        .filter_map(|tile| match tile {
            Tile::Box(pos) => Some(pos.x + (pos.y * 100)),
            _ => None,
        })
        .sum::<i32>();

    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = "########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<

";

    const INPUT2: &str = "##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^

";

    #[test]
    fn test_process() -> miette::Result<()> {
        assert_eq!("2028", process(INPUT1)?);
        assert_eq!("10092", process(INPUT2)?);
        Ok(())
    }
}
