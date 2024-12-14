use std::{collections::HashMap, vec};

use itertools::Itertools;

#[tracing::instrument]
pub fn process(_input: &str) -> miette::Result<String> {
    let mut chunks: HashMap<String, Vec<(u32, u32)>> = HashMap::new();
    let mut empty: Vec<(u32, u32)> = vec![];
    let mut next_index_in_array = 0;
    let mut next_index = 0;
    for (index, char) in _input.chars().enumerate() {
        let count = char.to_digit(10).unwrap();
        if index % 2 == 0 {
            let new: (u32, u32) = (next_index_in_array, count);
            let new_vec = vec![new];
            chunks
                .entry(next_index.to_string())
                .and_modify(|vec| vec.push(new))
                .or_insert(new_vec);
            next_index += 1;
        } else {
            let new: (u32, u32) = (next_index_in_array, count);
            empty.push(new);
        }
        next_index_in_array += count;
    }
    empty.reverse();
    let sorted = chunks
        .clone()
        .into_keys()
        .sorted_by(|a, b| Ord::cmp(&b.parse::<u32>().unwrap(), &a.parse::<u32>().unwrap()));

    let mut empty_chunk = empty.pop().unwrap();
    for chunk in sorted {
        let mut new_chunk: Vec<(u32, u32)> = vec![];
        let (old_index, mut count) = chunks.get(&chunk).unwrap().first().unwrap();

        while count != 0 {
            let (mut index, mut amount) = empty_chunk;
            if *old_index < index {
                break;
            }
            if *old_index < index + count {
                new_chunk.push((*old_index, index + count - *old_index));
                count = old_index - index;
            }

            if amount >= count {
                // This means all the of the rest of the chunk can be in this empty spacce

                new_chunk.push((index, count));
                index = index + count;
                amount = amount - count;
                empty_chunk = (index, amount);

                count = 0;
            } else {
                // This means it cannot be all in the empty space
                new_chunk.push((index, amount));
                count = count - amount;
                amount = 0;
            }
            if amount == 0 {
                empty_chunk = empty.pop().unwrap();
            }
        }
        if new_chunk != vec![] {
            chunks.entry(chunk).and_modify(|vec| *vec = new_chunk);
        }
    }
    let mut result: u64 = 0;
    for (chunk_index, vec) in chunks.clone() {
        let num = chunk_index.parse::<u32>().unwrap();

        for (index, count) in vec {
            for i in 0..count {
                result += (num * (index + i)) as u64
            }
        }
    }
    // dbg!(chunks);
    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "2333133121414131402";
        assert_eq!("1928", process(input)?);
        Ok(())
    }

    #[test]
    fn test_real_input() -> miette::Result<()> {
        let input = include_str!("../../../../aoc_inputs/2024/day09input");
        let result = include_str!("../../../../aoc_inputs/2024/day09result")
            .lines()
            .next()
            .unwrap();
        assert_eq!(result, process(input)?);
        Ok(())
    }

    
}
