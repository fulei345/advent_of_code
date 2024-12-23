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

    let mut triples = HashSet::new();
    for (n1, edges) in &connections {
        if n1.starts_with('t') {
            for n2 in edges {
                for n3 in connections[n2].intersection(edges) {
                    let mut set = [n1, n2, n3];
                    set.sort_unstable();
                    triples.insert(set);
                }
            }
        }
    }

    let result = triples.len();

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
        assert_eq!("7", process(input)?);
        Ok(())
    }
}
