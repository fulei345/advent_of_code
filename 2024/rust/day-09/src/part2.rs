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

    let sorted = chunks
        .clone()
        .into_keys()
        .sorted_by(|a, b| Ord::cmp(&b.parse::<u32>().unwrap(), &a.parse::<u32>().unwrap()));

    for chunk in sorted {
        let mut new_chunk: Vec<(u32, u32)> = vec![];
        let mut empy_index = 0;
        let (old_index, count) = chunks.get(&chunk).unwrap().first().unwrap();

        while empy_index < empty.len() {
            let (mut index, mut amount) = empty[empy_index];
            if *old_index < index {
                break;
            }

            if amount >= *count {
                new_chunk.push((index, *count));
                index = index + count;
                amount = amount - count;
                empty[empy_index] = (index, amount);
                break;
            }
            empy_index += 1;
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
        assert_eq!("2858", process(input)?);
        Ok(())
    }

    #[test]
    fn test_real_input() -> miette::Result<()> {
        let input = include_str!("../../../../aoc_inputs/2024/day09input");
        let result = include_str!("../../../../aoc_inputs/2024/day09result")
            .lines()
            .last()
            .unwrap();
        assert_eq!(result, process(input)?);
        Ok(())
    }
}
