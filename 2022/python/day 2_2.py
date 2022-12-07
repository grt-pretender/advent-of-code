# --- Day 2: Rock Paper Scissors ---
# --- Part Two ---

# Input: 
# Encrypted strategy guide with two columns.
# The first column is what the opponent is going to play: A for Rock, B for Paper, and C for Scissors.

# In fact, the second column says how the round needs to end: 
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.split

# Task:
# The total score is still calculated in the same way, 
# but now you need to figure out what shape to choose so the round ends as indicated.

# What would your total score be if everything goes exactly according to your strategy guide?


path = open('INSERT SOURCE FILE PATH')
input_data = [line.strip() for line in path]

final_score = 0
won, draw, loss = 6, 3, 0
rock, paper, scissors = 1, 2, 3

for i in input_data:
    opponent_moves, outcomes = i.split()

    final_score += {"X" : loss, "Y" : draw, "Z" : won} [outcomes]
    final_score += {("A", "X") : scissors, ("A", "Y") : rock, ("A", "Z") : paper, 
    ("B", "X") : rock, ("B", "Y") : paper, ("B", "Z") : scissors, 
    ("C", "X") : paper, ("C", "Y") : scissors, ("C", "Z") : rock,
    } [opponent_moves, outcomes]

print(final_score)


