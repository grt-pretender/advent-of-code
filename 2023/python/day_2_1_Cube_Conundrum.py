# -- Day 2: Cube Conundrum ---

# You're launched high into the atmosphere! 
# The apex of your trajectory just barely reaches the surface of a large island floating in the sky. 
# An Elf runs over to greet you. As you walk, the Elf shows you a small bag and some cubes 
# which are either red, green, or blue.Each time you play this game, he will hide a secret number 
# of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

# To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, 
# grab a handful of random cubes, show them to you, and then put them back in the bag. 
# He'll do this a few times per game.

# You play several games and record the information from each game (your puzzle input). 
# Each game is listed with its ID number (like the 11 in Game 11: ...) 
# followed by a semicolon-separated list of subsets of cubes that were revealed from the bag 
# (like 3 red, 5 green, 4 blue).
# For example, the record of a few games might look like this:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

# Task: Determine which games would have been possible 
# if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
# ------------------------

source = open('INSERT SOURCE FILE', 'r')
ans = 0
for index, data in enumerate(source):
	input_data = data.split(": ")[1].split("; ")

	for game_set in input_data:
		
		limit = { 'red' : 12, 'green' : 13, 'blue' : 14 }
		store = { 'red' : 0, 'green' : 0, 'blue' : 0 }
		
		for _set in game_set.split(", "):
			num, color = _set.split()
			store[color] = int(num)
		if store['red'] > limit['red'] or store['green'] > limit['green'] or store['blue'] > limit['blue']:
			break
	else:
		id_number = index+1
		ans += id_number				

print(ans)





