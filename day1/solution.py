input = open("input.txt", "r")

# pt 1
max_calories = 0
calories = 0
for line in input:
    if line != '\n':
        calories += int(line[:-1])
    else:
        if calories > max_calories:
            max_calories = calories
        calories = 0
print(max_calories)

# pt 2
calories_list = []
calories = 0
for line in input:
    if line != '\n':
        calories += int(line[:-1])
    else:
        calories_list.append(calories)
        calories = 0
calories_list.sort()
print(sum(calories_list[-3:]))


