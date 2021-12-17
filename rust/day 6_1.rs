TEMPLATE

fn main() {
    let data = part_1("3,4,3,1,2");
    println!("The answer is {}", data);
    
}

pub fn part_1(input: &str) -> usize {
	let mut fish: Vec<i64> = input
	.trim()
	.split(",")
	.map(|n| n.parse().unwrap())
	.collect(); 

	for _l in 0..256 {
		let mut fish_to_add = Vec::new();
		for fish in &mut fish {
			*fish -= 1;
			if *fish ==-1 {
				*fish = 6;
				fish_to_add.push(8);
			}
		}
		fish.append(&mut fish_to_add);
	}
	
	fish.len()

}


//#[cfg(test)]
//mod tests {
//	 #[test]
//	 fn example_1() {
//		assert_eq!(super::part_1("3,4,3,1,2\n", 80), 5934);
//	}

//	 #[test]
//	 fn example_1() {
//		assert_eq!(super::part_1("input", 80), 5934);
//	}

//}
