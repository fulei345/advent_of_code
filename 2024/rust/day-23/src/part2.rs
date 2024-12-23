use std::collections::{HashMap, HashSet};

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String> {
    let input = input.trim();
    let mut connections: HashMap<&str, HashSet<&str>> = HashMap::new();
    for line in input.lines() {
        let mut both = line.split("-");
        let a = both.next().unwrap();
        let b = both.next().unwrap();
        connections.entry(a).or_default().insert(b);
        connections.entry(b).or_default().insert(a);
    }

    let mut seen: HashSet<&str> = HashSet::new();
    let mut clique = Vec::new();
    let mut largest: Vec<&str> = Vec::new();

    for (n1, edges) in &connections {
        if !seen.contains(n1) {
            clique.clear();
            clique.push(*n1);

            for n2 in edges {
                let other = &connections[n2];

                if clique.iter().all(|&n3| other.contains(n3)) {
                    seen.insert(n2);
                    clique.push(*n2);
                }
            }

            if clique.len() > largest.len() {
                largest.clone_from(&clique);
            }
        }
    }

    largest.sort_unstable();
    let result = largest.join(",");

    Ok(result.to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
";
        assert_eq!("co,de,ka,ta", process(input)?);
        Ok(())
    }
}
