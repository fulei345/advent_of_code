use ::day_01::procces_part2;

fn main() {
    let file = std::fs::read_to_string("../../inputs/day1input").expect("Invalid Path");
    println!("Part1: {}", procces_part2(&file));
}
