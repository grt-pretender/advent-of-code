# --- Day 1: Sonar Sweep ---

# The overboard alarm goes off! One of the Elves tripped and accidentally sent the sleigh keys flying into the ocean
# Before you know it, you're inside a submarine the Elves keep ready for situations like this. 
# As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. 

# Input: Report that indicates that, scanning outward from the submarine, the sonar sweep found different depths: 
# each line is a measurement of the sea floor depth on the way.

# Task: Figure out how quickly the depth increases. Count the number of times a depth measurement increases from the previous measurement. 
# There is no measurement before the first measurement.


with open('INSERT YOUR FILE PATH', 'r') as source:
	input_data = source.readlines()

def depth_increase(input: list) -> int:
    
    count = 0

    for i in range(len(input) - 1):
    	if int(input[i + 1]) > int(input[i]):
   			count += 1
    return count

answer_1 = depth_increase(input_data) 
print(answer_1)



