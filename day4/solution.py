input = open("input.txt", "r")

# pt 1
contained = 0
for line in input:
    pairs = line[:-1].split(',')
    one = pairs[0].split('-')
    two = pairs[1].split('-')

    set1 = set(range(int(one[0]), int(one[1])+1))
    set2 = set(range(int(two[0]), int(two[1])+1))

    inters1 = set1.intersection(set2)
    inters2= set2.intersection(set1)

    if (len(inters1) == len(set1)) or (len(inters2) == len(set2)):
        contained += 1
print(contained)

# pt 2
overlap = 0
for line in input:
    pairs = line[:-1].split(',')
    one = pairs[0].split('-')
    two = pairs[1].split('-')

    set1 = set(range(int(one[0]), int(one[1])+1))
    set2 = set(range(int(two[0]), int(two[1])+1))

    inters1 = set1.intersection(set2)

    if (len(inters1) != 0):
        overlap += 1
print(overlap)
