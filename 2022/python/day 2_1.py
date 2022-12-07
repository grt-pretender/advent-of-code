#  --- Day 2: Rock Paper Scissors ---
# The Elves begin to set up camp on the beach. To decide whose tent gets to be closest
# to the snack storage, a giant Rock Paper Scissors tournament is already in progress.
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.


# Input: 
# Encrypted strategy guide with two columns.

# The first column is what the opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# The second column must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
# Winning every time would be suspicious, so the responses must have been carefully chosen.

# Task:
# The winner of the whole tournament is the player with the highest score. 
# Your total score is the sum of your scores for each round. 
# The score for a single round = the score for the selected shape + the score for the outcome of the round 
# (1 for Rock, 2 for Paper, and 3 for Scissors) 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# What would your total score be if everything goes exactly according to your strategy guide?


path = open('INSERT SOURCE FILE PATH')
input_data = [line.strip() for line in path]

final_score = 0
won, draw, loss = 6, 3, 0
rock, paper, scissors = 1, 2, 3

for i in input_data:
    opponent_moves, my_possible_moves = i.split()

    final_score += {"X" : rock, "Y" : paper, "Z" : scissors} [my_possible_moves]
    final_score += {("A", "X") : draw, ("A", "Y") : won, ("A", "Z") : loss, 
    ("B", "X") : loss, ("B", "Y") : draw, ("B", "Z") : won, 
    ("C", "X") : won, ("C", "Y") : loss, ("C", "Z") : draw,
    } [opponent_moves, my_possible_moves]

print(final_score)


