use ::day_02::procces_part1;

fn main() {
    let file = std::fs::read_to_string("../../inputs/day2input").expect("Invalid Path");
    println!("Part1: {}", procces_part1(&file));
}
