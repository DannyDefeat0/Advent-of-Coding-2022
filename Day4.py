file = open("Day4rawData", "r")
lines = file.readlines()

debug = []
matches = 0
for line in lines:
    split_line = ' '.join(' '.join(line.split(',')).split('-')).split()
    fline = [int(x) for x in split_line]
    if (fline[0] >= fline[2] and fline[0]<= fline[3]) or (fline[2] >= fline[0] and fline[2] <= fline[1]):
        matches += 1
    #if int(split_line[0]) >= int(split_line[2]) and int(split_line[1]) <= int(split_line[3]):
        #matches += 1
        #debug.append(line)
    #elif int(split_line[2]) >= int(split_line[0]) and int(split_line[3]) <= int(split_line[1]):
        #debug.append(line)
        #matches += 1
print(matches)

