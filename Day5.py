file = open("Day5rawData", "r")
lines = file.readlines()

#Define dimensions length and height, use this to create lists of letters at certain x,y positions
length = 9
height = 8
#consider putting final variables in all caps

stacks = []
for i in range(0,length):
    char_on_line = []
    column_pos = 1+(i*4)
    for k in range(0,height):
        #line one is technically shorter than the other lines, we need to account for that
        #print(str(k)+" , "+str(column_pos))
        #print(lines[k][column_pos])
        if len(lines[k]) < column_pos:
            continue
        if k == height-1:
            stacks.append(char_on_line)
        if lines[k][column_pos].isalpha():
            char_on_line.append(lines[k][column_pos])
print(stacks)
instructions = []
for i in range(10,len(lines)):
    split_line = lines[i].replace("move ", "").replace("from ","").replace("to ","").replace("\n","")
    split_line = split_line.split(" ")
    instructions.append(split_line)
#print(instructions)


for i in range(len(instructions)):
    num_to_move = int(instructions[i][0])
    initial_column = int(instructions[i][1])-1
    final_column = int(instructions[i][2])-1
    for k in range(0,num_to_move):
        stacks[final_column].insert(k,stacks[initial_column][0])
        stacks[initial_column].remove(stacks[initial_column][0])
#print(stacks)
answer = []
for i in range(length):
    answer.append(stacks[i][0])
answer = "".join(answer)
print(answer)