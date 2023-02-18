file = open("Day9rawData", "r")
lines = file.readlines()


checks = [2**0.5, 0, 1]

s = [0, 0]
tail_set = {tuple(s)}

tail = [0,0]
head = [0,0]

position = [head, tail]

def dist(pos1, pos2):
    euclidean_distance = (((pos2[0]-pos1[0])**2)+((pos2[1]-pos1[1])**2))**0.5
    return euclidean_distance


# (-1, 2) (0, 2) (1  2)
# (-1, 1) (0, 1) (1, 1)
# (-1, 0) (0, 0) (1, 0)
# (-1,-1) (0, -1) (1, -1)


def move(head_position, tail_position, direction, num_to_move):
    if direction == "R":
        end = head_position[0] + num_to_move
        while head_position[0] != end:
            head_position[0] += 1
            check = dist(head_position, tail_position)
            if check in checks:
                continue
            else:
                tail_position[0] += 1
                check = dist(head_position, tail_position)
                if head_position[1] - tail_position[1] > 0:
                    tail_position[1] += 1
                elif head_position[1] - tail_position[1] < 0:
                    tail_position[1] -= 1
            tail_set.add(tuple(tail_position))
    elif direction == "L":
        end = head_position[0] - num_to_move
        while head_position[0] != end:
            head_position[0] -= 1
            check = dist(head_position, tail_position)
            if check in checks:
                continue
            else:
                tail_position[0] -= 1
                check = dist(head_position, tail_position)
                if head_position[1] - tail_position[1] > 0:
                    tail_position[1] += 1
                if head_position[1] - tail_position[1] < 0:
                    tail_position[1] -= 1
            tail_set.add(tuple(tail_position))
    elif direction == "U":
        end = head_position[1] + num_to_move
        while head_position[1] != end:
            head_position[1] += 1
            check = dist(head_position, tail_position)
            if check in checks:
                continue
            else:
                tail_position[1] += 1
                check = dist(head_position, tail_position)
                if head_position[0] - tail_position[0] > 0:
                    tail_position[0] += 1
                elif head_position[0] - tail_position[0] < 0:
                    tail_position[0] -= 1
            tail_set.add(tuple(tail_position))
    elif direction == "D":
        end = head_position[1] - num_to_move
        while head_position[1] != end:
            head_position[1] -= 1
            check = dist(head_position, tail_position)
            if check in checks:
                continue
            else:
                tail_position[1] -= 1
                check = dist(head_position, tail_position)
                if head_position[0] - tail_position[0] > 0:
                    tail_position[0] += 1
                elif head_position[0] - tail_position[0] < 0:
                    tail_position[0] -= 1
            tail_set.add(tuple(tail_position))
    return [head_position, tail_position]

for line in lines:
    input = line.split()
    ref = input[0]
    num = int(input[-1])
    position = move(position[0], position[1], ref, num)
    print(position)
    #FIRST MOVE IS GETTING COUNTED FUCK YOU GAME
print(tail_set)
print(len(tail_set))
