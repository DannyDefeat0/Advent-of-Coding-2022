file = open("Day1RawData", "r")
lines = file.readlines()

Sum = 0
Max = 0
for line in lines:
    if line != "\n":
        Sum += int(line)
    else:
        if Sum > Max:
            Max = Sum
            Sum = 0
            print(Max)

