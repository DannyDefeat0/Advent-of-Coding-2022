file = open("Day9rawData", "r")
lines = file.readlines()

length = 258
s = 153
points_visited = [s]
current_position = 153
tail_position = 153

#[+len-1] [+len] [+len+1]
#[-1]     [0]    [+1]
#[-len-1] [-len] [-len+1]

checks = [length-1, length, length+1, -1, 0, 1, -length - 1, -length, -length+1]

#HINT - Rewrite in terms of Euclidean Distance, All adjacent points are one of three values
#Use x,y coordinates
#tuples
#you can line by line check to see where the function fails


def move_right(start, num_to_move):
    position = start
    final = start + num_to_move
    while position < final:
        position += 1
    global current_position
    current_position = position
    global tail_position
    up_or_down = tail_position - current_position
    if (tail_position - current_position) not in checks and str(tail_position/length)[0] != str(current_position/length)[0]:
        if up_or_down > 0:
            tail_position += -length+1
        elif up_or_down < 0:
            tail_position += length+1
    if tail_position not in points_visited:
        points_visited.append(tail_position)
    while (current_position - tail_position) not in checks:
        tail_position += 1
        if tail_position not in points_visited:
            points_visited.append(tail_position)
def move_left(start, num_to_move):
    position = start
    final = start - num_to_move
    while position > final:
        position -= 1
    global current_position
    current_position = position
    global tail_position
    up_or_down = tail_position - current_position
    if (tail_position - current_position) not in checks and str(tail_position/length)[0] != str(current_position/length)[0]:
        if up_or_down > 0:
            tail_position += -length - 1
        elif up_or_down < 0:
            tail_position += length - 1
    if tail_position not in points_visited:
        points_visited.append(tail_position)
    while (current_position - tail_position) not in checks:
        tail_position -= 1
        if tail_position not in points_visited:
            points_visited.append(tail_position)
def move_up(start, num_to_move):
    position = start
    final = start + (num_to_move*length)
    while position < final:
        position += length
    global current_position
    current_position = position
    global tail_position
    left_or_right = (current_position % length)-(tail_position % length)
    if (current_position - tail_position) not in checks and left_or_right > 0:
        tail_position += +1
    if (current_position - tail_position) not in checks and left_or_right < 0:
        tail_position += -1
    while (current_position - tail_position) not in checks:
        tail_position += length
        if tail_position not in points_visited:
            points_visited.append(tail_position)
def move_down(start, num_to_move):
    position = start
    final = start - (num_to_move*length)
    while position > final:
        position -= length
    global current_position
    current_position = position
    global tail_position
    left_or_right = (current_position % length)-(tail_position % length)
    if (current_position - tail_position) not in checks and left_or_right > 0:
        tail_position += 1
    if (current_position - tail_position) not in checks and left_or_right < 0:
        tail_position += -1
    while (current_position - tail_position) not in checks:
        tail_position -= length
        if tail_position not in points_visited:
            points_visited.append(tail_position)
def move(position, direction, num_to_move):
    if direction == "R":
        move_right(position, num_to_move)
    elif direction == "L":
        move_left(position, num_to_move)
    elif direction == "U":
        move_up(position, num_to_move)
    elif direction == "D":
        move_down(position, num_to_move)
    else:
        pass

test = 0
hmm = 0
current_down_max = 0
current_max = 0
current_min = 0
for line in lines:
    print(line)
    input = line.split()
    ref = input[0]
    num = int(input[-1])
    if ref == "R":
        test += num
        if test > current_max:
            current_max = test
    if ref == "L":
        test -= num
        if test < current_min:
            current_min = test
    move(current_position, input[0], int(input[-1]))
print("answer is " + str(len(points_visited)))
print(points_visited)
#print(test)
#print(current_min)
#print(current_max)
#print(current_down_max)
