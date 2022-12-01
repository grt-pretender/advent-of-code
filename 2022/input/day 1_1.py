# --- Day 1: Calorie Counting ---
# Input: 
# The list represents the number of items' Calories each Elf is carrying separated by a blank line.

# Task:
# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask.
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?


with open('INSERT SOURCE FILE', 'r') as source:
    input_data = source.read().split("\n\n")

elves_lines = [list(map(int, elf.strip().split("\n"))) for elf in input_data]
    
result= 0
for elves in elves_lines:
    if result <= sum(elves):
        result = sum(elves)
print(result)


