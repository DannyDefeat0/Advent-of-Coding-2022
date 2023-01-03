file = open("Day6rawData", "r")
lines = file.readlines()

for line in lines:
    for i in range(len(line)-13):
        check = [line[k] for k in range(i, i+14)]
        if len(check) == len(set(check)):
            print(i+14)
            break