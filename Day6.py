file = open("Day6rawData", "r")
lines = file.readlines()

for line in lines:
    for i in range(len(line)-13):
        check = [line[k] for k in range(i+1, i+14)]
        if line[i] in check or len(check) != len(set(check)):
            pass
        else:
            print(i+14)
            break