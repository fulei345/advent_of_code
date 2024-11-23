use ::day_01::procces_part1;

fn main() {
    let file = std::fs::read_to_string("../../inputs/day1input").expect("Invalid Path");
    println!("Part1: {}", procces_part1(&file));
}
