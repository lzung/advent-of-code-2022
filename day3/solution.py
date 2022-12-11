input = open("input.txt", "r")

# pt 1
score = 0
for line in input:
    rucksack_length = len(line)//2
    bag1 = set(line[:rucksack_length])
    bag2 = set(line[rucksack_length:])

    for char in bag1:
        if char in bag2:
            if char.isupper():
                score += ord(char) - 38
            else:
                score += ord(char) - 96

# pt 2
score2 = 0
lines = open("input.txt").readlines()
groups = [lines[l:l+3] for l in range(0, len(lines), 3)]

for elves in groups:
    bag1 = set(elves[0][:-1])
    bag2 = set(elves[1][:-1])
    bag3 = set(elves[2][:-1])

    for char in bag1:
        if char in bag2:
            if char in bag3:
                if char.isupper():
                    score2 += ord(char) - 38
                else:
                    score2 += ord(char) - 96
print(score2)
