# --- Day 1: Trebuchet?! ---

# Something is wrong with global snow production, and you've been selected to take a look. 
# Elves are already loading you into a trebuchet and sending you to the sky.

# But elves discover that their calibration document (your puzzle input) has been amended 
# by a very young Elf who was apparently just excited to show off her art skills. 
# Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; 
# each line originally contained a specific calibration value that the Elves now need to recover. 
# On each line, the calibration value can be found by combining the first digit and the last digit 
# (in that order) to form a single two-digit number.

# For example:
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. 
# Adding these together produces 142.

#Task: Consider your entire calibration document. What is the sum of all of the calibration values?

# ------------------------

import re
with open('INSERT SOURCE FILE', 'r') as source:
    input_data = source.read().split()

def extract_digits(data):

	digit_collection = 0
	find_digit = "".join(re.findall(r'\d+', data))
	left_digit = int(find_digit[0])*10
	right_digit = int(find_digit[-1])
	
	if len(find_digit) == 1:
		final_digit = int(find_digit*2)
	
	if len(find_digit) >= 2:
		final_digit = left_digit + right_digit

	digit_collection += final_digit
	return digit_collection

processed_data = [extract_digits(el) for el in input_data]
print(sum(processed_data))

