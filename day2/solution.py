input = open("input.txt", "r")

# pt 1
my_dict = {'X' : 1, 'Y' : 2, 'Z' : 3}
score_dict = {'A X' : 3, 'B X' : 0, 'C X' : 6, 'A Y' : 6, 'B Y' : 3, 'C Y' : 0, 'A Z' : 0, 'B Z' : 6, 'C Z' : 3}

total = 0
for line in input:
    me = line.split(' ')[1]
    total += my_dict[me[:-1]] + score_dict[line[:-1]]
print(total)

# pt 2
outcome_dict = {'A X' : 'Z', 'B X' : 'X', 'C X' : 'Y', 'A Y' : 'X', 'B Y' : 'Y', 'C Y' : 'Z', 'A Z' : 'Y', 'B Z' : 'Z', 'C Z' : 'X'}
outcome_score_dict = {'A X' : 0, 'B X' : 0, 'C X' : 0, 'A Y' : 3, 'B Y' : 3, 'C Y' : 3, 'A Z' : 6, 'B Z' : 6, 'C Z' : 6}

total = 0
for line in input:
    total += my_dict[outcome_dict[line[:-1]]] + outcome_score_dict[line[:-1]]
print(total)