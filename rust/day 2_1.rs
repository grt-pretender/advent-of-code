// Input: The submarine can take a series of commands like forward 1, down 2, or up 3:

// - forward X increases the horizontal position by X units;
// - down X increases the depth by X units;
// - up X decreases the depth by X units.

// Horizontal position and depth both start at 0.

// Task : Calculate the horizontal position and depth after following the planned course (input). 
// Multiply them.


fn main() {
    let input = //INSERT SOURCE FILE;


    let mut horizontal_position = 0;
    let mut depth_position = 0;
    
    let input_data: Vec<String> = input
        .lines()
        .map(|string| string.parse().unwrap())
        .collect();
    
    for line in input_data {
        let commands: Vec<&str> = line.split(' ').collect();
        let amount: i32 = commands[1].parse().unwrap();

        match commands[0] {
            "forward" => horizontal_position+=amount,
            "up"      => depth_position-=amount,
            "down"    => depth_position+=amount,
            _         => println!("unknown")
        }
    }

    let  first_answer = horizontal_position*depth_position;
    println!("The first answer is {}", first_answer)
}
