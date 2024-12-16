use glam::IVec2;
use std::collections::HashSet;

#[derive(Debug, Eq, PartialEq, Hash, Clone, Copy)]
enum Direction {
    North,
    South,
    East,
    West,
}

#[derive(Debug, Eq, PartialEq, Hash, Clone, Copy)]
enum Tile {
    Wall((IVec2, IVec2)),
    Robot(IVec2),
    Box((IVec2, IVec2)),
}

impl Tile {
    fn right(&self) -> IVec2 {
        match self {
            Tile::Wall((right, _)) => *right,
            Tile::Robot(right) => *right,
            Tile::Box((_, right)) => *right,
        }
    }

    fn left(&self) -> IVec2 {
        match self {
            Tile::Wall((left, _)) => *left,
            Tile::Robot(left) => *left,
            Tile::Box((left, _)) => *left,
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

    fn to_char(&self) -> char {
        match self {
            Direction::North => '^',
            Direction::South => 'v',
            Direction::East => '>',
            Direction::West => '<',
        }
    }

    fn orthogonal(&self) -> (Self, Self) {
        match self {
            Direction::North => (Direction::West, Direction::East),
            Direction::South => (Direction::West, Direction::East),
            Direction::East => (Direction::North, Direction::South),
            Direction::West => (Direction::North, Direction::South),
        }
    }
}

fn check_recursive(
    obstacles: &HashSet<Tile>,
    pos: IVec2,
    direction: Direction,
) -> Option<HashSet<Tile>> {
    // Returns the boxes which needs to be moved or None if there is a wall
    let mut result: HashSet<Tile> = HashSet::new();
    let mut search_vec: Vec<IVec2> = vec![pos];
    while let Some(mut next) = search_vec.pop() {
        next += direction.to_vec();
        let leftbox;
        let rigghtbox;
        let middle;
        match direction {
            Direction::North | Direction::South => {
                leftbox = (next + direction.orthogonal().0.to_vec(), next);
                rigghtbox = (next, next + direction.orthogonal().1.to_vec());

                if obstacles.contains(&Tile::Wall(leftbox))
                    || obstacles.contains(&Tile::Wall(rigghtbox))
                {
                    return None;
                }

                if obstacles.contains(&Tile::Box(leftbox)) {
                    let mut new_left_point = leftbox.0;
                    if !search_vec.contains(&new_left_point) {
                        search_vec.push(new_left_point);
                    }
                    new_left_point = leftbox.1;
                    if !search_vec.contains(&new_left_point) {
                        search_vec.push(new_left_point);
                    }
                    result.insert(Tile::Box(leftbox));
                }
                if obstacles.contains(&Tile::Box(rigghtbox)) {
                    let mut new_rigght_point = rigghtbox.0;
                    if !search_vec.contains(&new_rigght_point) {
                        search_vec.push(new_rigght_point);
                    }
                    new_rigght_point = rigghtbox.1;
                    if !search_vec.contains(&new_rigght_point) {
                        search_vec.push(new_rigght_point);
                    }
                    result.insert(Tile::Box(rigghtbox));
                }
            }
            Direction::West | Direction::East => {
                if direction == Direction::West {
                    middle = (next + direction.to_vec(), next);
                } else {
                    middle = (next, next + direction.to_vec());
                }

                if obstacles.contains(&Tile::Wall(middle)) {
                    return None;
                }

                if obstacles.contains(&Tile::Box(middle)) {
                    let mut new_middle_point = middle.0;
                    if !search_vec.contains(&new_middle_point) && new_middle_point != next {
                        search_vec.push(new_middle_point);
                    }
                    new_middle_point = middle.1;
                    if !search_vec.contains(&new_middle_point) && new_middle_point != next {
                        search_vec.push(new_middle_point);
                    }

                    result.insert(Tile::Box(middle));
                }
            }
        }
    }
    Some(result)
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
                line.chars().enumerate().filter_map(move |(x, c)| {
                    let new_x = x * 2;
                    match c {
                        'O' => Some(Tile::Box((
                            IVec2::new(new_x as i32, y as i32),
                            IVec2::new((new_x + 1) as i32, y as i32),
                        ))),
                        '#' => Some(Tile::Wall((
                            IVec2::new(new_x as i32, y as i32),
                            IVec2::new((new_x + 1) as i32, y as i32),
                        ))),
                        '@' => Some(Tile::Robot(IVec2::new(new_x as i32, y as i32))),
                        _ => None,
                    }
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
        let result = check_recursive(&obstacles, robot_pos.left(), dir);
        match result {
            Some(result) => {
                for tile in result.iter() {
                    obstacles.remove(tile);
                }
                for tile in result.iter() {
                    obstacles.insert(Tile::Box((
                        tile.left() + dir.to_vec(),
                        tile.right() + dir.to_vec(),
                    )));
                }
                robot_pos = Tile::Robot(robot_pos.right() + dir.to_vec());
            }
            None => {}
        }
        // Print each tile in obstacles for each Ivec2 in the tile
        // for i in 0..10 {
        //     for j in 0..20 {
        //         let left: IVec2 = IVec2::new(j, i);
        //         let right: IVec2 = IVec2::new(j + 1, i);
        //         match (left, right) {
        //             (left, right) if obstacles.contains(&Tile::Box((left, right))) => {
        //                 print!("[")
        //             }
        //             (left, right) if obstacles.contains(&Tile::Wall((left, right))) => {
        //                 print!("#")
        //             }
        //             (left, right)
        //                 if obstacles.contains(&Tile::Wall((
        //                     left + Direction::West.to_vec(),
        //                     right + Direction::West.to_vec(),
        //                 ))) =>
        //             {
        //                 print!("#")
        //             }
        //             (left, _) if robot_pos == Tile::Robot(left) => {
        //                 print!("@")
        //             }
        //             (left, right)
        //                 if obstacles.contains(&Tile::Box((
        //                     left + Direction::West.to_vec(),
        //                     right + Direction::West.to_vec(),
        //                 ))) =>
        //             {
        //                 print!("]")
        //             }
        //             _ => {
        //                 print!(".")
        //             }
        //         }
        //     }
        //     println!();
        // }
    }

    let result = obstacles
        .iter()
        .filter_map(|tile| match tile {
            Tile::Box((left, _)) => Some(left.x + (left.y * 100)),
            _ => None,
        })
        .sum::<i32>();

    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "
#######
#.....#
#.OO@.#
#.....#
#######

<<";

    const INPUT1: &str = "
#######
#.....#
#.O#..#
#.O...#
#.@...#
#######

^^";

    const INPUT2: &str = "
##########
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

    const INPUT3: &str = "
#######
#...#.#
#.....#
#.....#
#.....#
#.....#
#.OOO@#
#.OOO.#
#..O..#
#.....#
#.....#
#######

v<vv<<^^^^^";

    const INPUT4: &str = "
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^";

    #[test]
    fn test_process() -> miette::Result<()> {
        assert_eq!("9021", process(INPUT2)?);
        Ok(())
    }

    #[test]
    fn test_push() -> miette::Result<()> {
        assert_eq!("406", process(INPUT)?);
        Ok(())
    }

    #[test]
    fn test_wall() -> miette::Result<()> {
        assert_eq!("308", process(INPUT1)?);
        assert_eq!("2339", process(INPUT3)?);
        Ok(())
    }

    #[test]
    fn test_rest() -> miette::Result<()> {
        assert_eq!("618", process(INPUT4)?);
        Ok(())
    }
}
