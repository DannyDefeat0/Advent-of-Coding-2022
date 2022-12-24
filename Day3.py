file = open("Day3RawData", "r")
lines = file.readlines()
priorities = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}
# priority_order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in range(len(priority_order)):
# Try to find algorithm
# print("'" + priority_order[i] + "'" + ":" + str(i+1) + ",")
# Each line is a Rucksack
# The first half of characters in a rucksack represent compartment 1, the second half compartment 2.

problems = 0
badges = 0
for line in lines:
    fline = len(line)
    #look up slice
    hfline = int(fline/2)
    for i in range(0,hfline):
        if line[i] in line[0:i]:
            next
        else:
            for k in range(hfline,fline-1):
                if line[i] == line[k]:
                    #print(line[i])
                    problems += priorities[line[i]]
                    break
possible_badges = []
badge_problems = 0
for line in lines:
    fline = len(line)
    for i in range(0,fline):
        if line[i] not in possible_badges:
            possible_badges.append(line[i])
        elif line[i] in possible_badges and line[i] not in line[0:i]:
            possible_badges.append(line[i])
        if possible_badges.count(line[i]) == 3:
            badge_problems += priorities[line[i]]
            possible_badges = []
            break
print(badge_problems)
#consider time complexity. We're checking every character in every line.






