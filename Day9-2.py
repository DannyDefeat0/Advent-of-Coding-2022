file = open("Day9rawData", "r")
lines = file.readlines()


checks = [2**0.5, 0, 1]
position = [[0,0] for i in range(10)]
s = [0, 0]
tail_set = {tuple(position[9])}

def subtract(tuple1, tuple2):
    dif = tuple(map(lambda i, j: i - j, tuple1, tuple2))
    return dif
def add(tuple1,tuple2):
    summation = tuple(map(lambda i, j: i + j, tuple1, tuple2))
    return summation

position = [[0,0] for i in range(10)]


def move_tail(head_position, tail_position):
    gap = subtract(head_position, tail_position)
    dist_lookup={
        (2, 2): (1, 1),
        (2, 1): (1, 1),
        (2, 0): (1, 0),
        (2, -1): (1, -1),
        (2, -2): (1, -1),
        (1, 2): (1, 1),
        (1, -2): (1, -1),
        (0, 2): (0, 1),
        (0, -2): (0, -1),
        (-1, 2): (-1, 1),
        (-1, -2): (-1,-1),
        (-2, -1): (-1, -1),
        (-2, 2): (-1, 1),
        (-2, 0): (-1, 0),
        (-2, 1): (-1, 1),
        (-2, -2): (-1, -1),
      }
    if gap in dist_lookup:
        tail_position = add(tail_position, dist_lookup[gap])
    return tail_position
def dist(pos1, pos2):
    euclidean_distance = (((pos2[0]-pos1[0])**2)+((pos2[1]-pos1[1])**2))**0.5
    return euclidean_distance


# (-1, 2) (0, 2) (1  2)
# (-1, 1) (0, 1) (1, 1)
# (-1, 0) (0, 0) (1, 0)
# (-1,-1) (0, -1) (1, -1)


def move_head(head_position, direction):
    if direction == "R":
        head_position[0] += 1
    elif direction == "L":
        head_position[0] -= 1
    elif direction == "U":
        head_position[1] += 1
    elif direction == "D":
        head_position[1] -= 1
    return head_position
def move(head_position, direction, num_to_move):
    while num_to_move > 0:
        position[0] = move_head(head_position, direction)
        num_to_move -= 1
        for i in range(1, len(position)):
            position[i] = move_tail(position[i-1], position[i])
        tail_set.add(tuple(position[9]))
    return position
for line in lines:
    input = line.split()
    ref = input[0]
    num = int(input[-1])
    position = move(position[0], ref, num)
    #print(position)
print(tail_set)
print(len(tail_set))
