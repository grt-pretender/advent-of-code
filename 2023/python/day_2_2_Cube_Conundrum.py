#  --- Part Two ---
# The Elf says they've stopped producing snow because they aren't getting any water! 
# He isn't sure why the water stopped; however, he can show you how to get to the water source 
# to check it out for yourself. As you continue your walk, the Elf poses a second question: 
# in each game you played, what is the fewest number of cubes of each color 
# that could have been in the bag to make the game possible?

# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 
# For each game, find the minimum set of cubes that must have been present. 
# What is the sum of the power of these sets?

# ------------------------

source = open('INSERT SOURCE FILE.txt', 'r')

set_power = 0
for index, data in enumerate(source):
	fewest_cubes = { 'red' : 0, 'green' : 0, 'blue' : 0 }
	input_data = data.split(": ")[1].split("; ")

	for game_set in input_data:
		store = { 'red' : 0, 'green' : 0, 'blue' : 0 }

		for _set in game_set.split(", "):
			num, color = _set.split()
			store[color] = int(num)
		
		for col in fewest_cubes:
			fewest_cubes[col] = max(fewest_cubes[col], store[col])
				
	set_power += fewest_cubes['red'] * fewest_cubes['green'] * fewest_cubes['blue']

print(set_power)
