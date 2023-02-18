file = open("Day9rawData", "r")
lines = file.readlines()

length = 258
s = 0
points_visited = [s]
current_position = 0
tail_position = 0
# [+len-1] [+len] [+len+1]
# [-1]     [0]    [+1]
# [-len-1] [-len] [-len+1]

checks = [length - 1, length, length + 1, -1, 0, 1, -length - 1, -length, -length + 1]


# HINT - Rewrite in terms of Euclidean Distance, All adjacent points are one of three values
# Use x,y coordinates
# tuples
# you can line by line check to see where the function fails


def move_right(start, num_to_move):
    position = start
    final = start + num_to_move
    global tail_position
    global current_position
    while position < final:
        position += 1
        current_position = position
        up_or_down = tail_position - current_position
        if (tail_position - current_position) not in checks and str(tail_position / length)[0] != str(current_position / length)[0]:
            if up_or_down > 0:
                tail_position += -length + 1
            elif up_or_down < 0:
                tail_position += length + 1
        if (tail_position - current_position) not in checks and (tail_position % length) == 0:
            if up_or_down > 0:
                tail_position += -length + 1
            elif up_or_down < 0:
                tail_position += length + 1
        if tail_position not in points_visited:
            points_visited.append(tail_position)
        elif (current_position - tail_position) not in checks:
            tail_position += 1
            if tail_position not in points_visited:
                points_visited.append(tail_position)

def move_left(start, num_to_move):
    position = start
    final = start - num_to_move
    global tail_position
    global current_position
    while position > final:
        position -= 1
        current_position = position
        up_or_down = tail_position - current_position
        if (tail_position - current_position) not in checks and str(tail_position / length)[0] != str(current_position / length)[0]:
            if up_or_down > 0:
                tail_position += -length - 1
            elif up_or_down < 0:
                tail_position += length - 1
        if (tail_position - current_position) not in checks and (tail_position % length) == 0:
            if up_or_down > 0:
                tail_position += -length - 1
            elif up_or_down < 0:
                tail_position += length - 1
        if tail_position not in points_visited:
            points_visited.append(tail_position)
        elif (current_position - tail_position) not in checks:
            tail_position -= 1
            if tail_position not in points_visited:
                points_visited.append(tail_position)


def move_up(start, num_to_move):
    position = start
    final = start + (num_to_move * length)
    global tail_position
    global current_position
    while position < final:
        position += length
        current_position = position
        left_or_right = (current_position % length) - (tail_position % length)
        if (current_position - tail_position) not in checks and left_or_right > 0:
            tail_position += length + 1
        if (current_position - tail_position) not in checks and left_or_right < 0:
            tail_position += length - 1
        if tail_position not in points_visited:
            points_visited.append(tail_position)
        elif (current_position - tail_position) not in checks:
            tail_position += length
            if tail_position not in points_visited:
                points_visited.append(tail_position)


def move_down(start, num_to_move):
    position = start
    final = start - (num_to_move * length)
    global tail_position
    global current_position
    while position > final:
        position -= length
        current_position = position
        left_or_right = (current_position % length) - (tail_position % length)
        if (current_position - tail_position) not in checks and left_or_right > 0:
            tail_position += -length + 1
        if (current_position - tail_position) not in checks and left_or_right < 0:
            tail_position += -length - 1
        if tail_position not in points_visited:
            points_visited.append(tail_position)
        elif (current_position - tail_position) not in checks:
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
        print("error")
hmm = 0
current_min = 0
current_max = 0
for line in lines:
    input = line.split()
    ref = input[0]
    num = int(input[-1])
    if ref == "L":
        hmm -= num
        if hmm < current_min:
            current_min = hmm
    if ref == "R":
        hmm += num
        if hmm > current_max:
            current_max = hmm
    move(current_position, input[0], int(input[-1]))
print("answer is " + str(len(points_visited)))
print(points_visited)
print(current_max)
print(current_min)