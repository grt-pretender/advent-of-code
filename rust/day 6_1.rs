//--- Day 6 --- 
//--- Lanternfish ---

// A massive school of glowing lanternfish swims past. You should model their growth/birth rate. 
// You can model each fish as a single number that represents the number of days until it creates a new lanternfish.

// Each lanternfish creates a new lanternfish once every 7 days.
// This process isn't necessarily synchronized.
// And a new lanternfish would need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.

// A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value).
// The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.
// Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases // by 1 if it was present at the start of the day.

// Input: list of the ages of several hundred nearby lanternfish.
// Task: Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?


fn main() {
    let data = part_1(//INSERT INPUT DATA);
    println!("The answer is {}", data);
}

pub fn part_1(input: &str) -> usize {
	let mut fish: Vec<i64> = input
	.trim()
	.split(",")
	.map(|n| n.parse().unwrap())
	.collect(); 

	for _days in 0..80 {
		let mut new_fish = Vec::new();
		for fish in &mut fish {
			*fish -= 1;
			if *fish ==-1 {
				*fish = 6;
				new_fish.push(8);
			}
		}
		fish.append(&mut new_fish);
	}
	
	fish.len()

}
