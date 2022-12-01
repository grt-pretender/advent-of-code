# --- Day 1: Calorie Counting --- 
# --- Part Two ---
# Elves realized that the Elf carrying the most Calories of food might eventually run out of snacks.

# Input: 
# The list represents the number of items' Calories each Elf is carrying separated by a blank line

# Task:
# Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?


with open('INSERT SOURCE FILE', 'r') as source:
    input_data = source.read().split("\n\n")

elves_lines = [list(map(int, elf.strip().split("\n"))) for elf in input_data]
    

values = []

for calories in elves_lines:
    current_sum = sum(calories)
    values.append(current_sum)

result = sorted(values, reverse=True)
print(result[0] + result[1] + result[2])
# print(result)
