--- Part Two ---
// Input: the same.

// Based on your calculations, the planned course doesn't seem to make any sense. 
// In addition to horizontal position and depth, you'll also need to track a third value, aim (also starts at 0). 

// The commands also mean something entirely different:

// - down X increases your aim by X units.
// - up X decreases your aim by X units.

// - forward X does two things:
// -- It increases your horizontal position by X units.
// -- It increases your depth by your aim multiplied by X.

// Task: Using this new interpretation of the commands, calculate the final horizontal position and depth. 


fn main() {
    let input = //INSERT SOURCE FILE;

    let mut horizontal_position = 0;
    let mut depth_position = 0;
    let mut aim = 0;
    
    let input_data: Vec<String> = input
        .lines()
        .map(|string| string.parse().unwrap())
        .collect();
    
    for line in input_data {
        let commands: Vec<&str> = line.split(' ').collect();
        let amount: i32 = commands[1].parse().unwrap();

        match commands[0] {
            "forward" => {
            horizontal_position+=amount;
            depth_position+=aim*amount
            }
            "up"      => aim-=amount,
            "down"    => aim+=amount,
            _         => println!("unknown")
        }
    }

    let second_answer = horizontal_position*depth_position;
    println!("The second answer is {}", second_answer)
}
