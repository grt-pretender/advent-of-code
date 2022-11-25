//--- Day 6: Lanternfish ---
// --- Part Two ---
// Suppose the lanternfish live forever and have unlimited food and space. 
// Would they take over the entire ocean?

// Input: The same.
// Task: How many lanternfish would there be after 256 days?

fn main() {
    let data = part_2//(INSERT INPUT DATA);
    println!("The answer is {}", data);

}

fn part_2(input: &str) -> u64 {
    
    let mut count_fish = [0; 9];
    
    input
        .split(',')
        .map(|n| n.parse::<usize>().unwrap())
        .for_each(|n| count_fish[n] += 1);
        
    for _days in 0..256 {
        count_fish.rotate_left(1);
        count_fish[6] += count_fish[8];
            }
        
    count_fish
        .iter()
        .sum()
    }


