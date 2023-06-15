file = open("Day15RawData", "r")
lines = file.readlines()

#item = item.strip().split(' -> ')
#rock_coordinates = [[int(coordinate.split(',')[0]), int(coordinate.split(',')[1])] for coordinate in item]

#we need to eliminate all the places there cannot be beacons
#each time we should be checking fewer possible points
#first calculate the manhattan distance to determine the range of points we check
#


def manhattan_distance(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    assert isinstance(x1,int)
    distance = abs(x1 - x2)+abs(y1-y2)
    return distance

def calculate_points_within_manhattan_distance(point, distance, beacon, row):
    x, y = point
    points = set()
    if row not in range(y-distance, y+distance+1):
        return points
    for i in range(-distance, distance+1):
        if abs(i) + abs(row-y) <= distance and (x + i, row) != beacon:
            points.add((x + i, row))
    return points

def calculate_points_within_manhattan_distance_p2(point, distance, beacon):
    x, y = point
    check = distance + 1
    points = set()
    for i in range(-check, check):
        j = check - i
        if x + i > 4000000 or y + j > 4000000 or x + i < 0 or y + j < 0:
            pass
        if (x + i, y + j) != beacon:
            points.add((x + i, y + j))
    return points

def extract_numbers(string):
    current_number = ""
    numbers = []

    for char in string:
        if char.isdigit() or char == "-":
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ""

    if current_number:
        numbers.append(int(current_number))

    return numbers

def beacon_locator(source):
    groups = set()
    not_beacons = set()
    x_min = ""
    y_min = ""
    x_max = ""
    y_max = ""
    for pairs in source:
        nums = extract_numbers(pairs)
        sensor = tuple([nums[0],nums[1]])
        beacon = tuple([nums[2],nums[3]])
        sensor_beacon_pair = tuple([sensor,beacon])
        groups.add(sensor_beacon_pair)
        #print(sensor, beacon)
        if x_min == "":
            x_min = min(nums[0], nums[2])
            x_max = max(nums[0], nums[2])
            y_min = min(nums[1], nums[3])
            y_max = max(nums[1], nums[3])
        else:
            x_min = min(x_min, nums[0], nums[2])
            x_max = max(x_max, nums[0], nums[2])
            y_min = min(y_min, nums[1], nums[3])
            y_max = max(y_max, nums[1], nums[3])
    for points in groups:
        sensor = points[0]
        beacon = points[1]
        not_beacon = calculate_points_within_manhattan_distance(sensor, manhattan_distance(sensor, beacon),beacon,2000000)
        for dud in not_beacon:
            not_beacons.add(dud)
        #print(not_beacons)
    y10_count = 0
    print(len(not_beacons))
    return groups

#for part 2 we need to check points past our border. So if the beacon is at a manhattan distance of 3. The only answers are ones that are Manhattan distance of 4 or greater.


def beacon_locator_p2(source):
    groups = set()
    possible_answers = set()
    for pairs in source:
        nums = extract_numbers(pairs)
        if nums[0] > 4000000 and nums[2] > 4000000:
            pass
        if nums[1] >4000000 and nums[3] > 4000000:
            pass
        if nums[0] < 0 and nums[2] < 0:
            pass
        if nums[1] < 0 and nums[3] < 0:
            pass
        sensor = tuple([nums[0],nums[1]])
        beacon = tuple([nums[2],nums[3]])
        sensor_beacon_pair = tuple([sensor,beacon])
        groups.add(sensor_beacon_pair)
    for points in groups:
        sensor = points[0]
        beacon = points[1]
        possible_answer = calculate_points_within_manhattan_distance_p2(sensor, manhattan_distance(sensor, beacon), beacon)
        possible_answers.update(possible_answer)
    filtered_set = set()
    for guess in possible_answers:
        if guess[0] <= 4000000 and guess[1] <= 4000000:
            if guess[0] >= 0 and guess[1] >= 0:
                filtered_set.add(guess)
    my_answer = "Jim"
    groups = list(groups)
    for serious_guess in filtered_set:
        for i in range(len(groups)):
            #print(serious_guess, groups[i][0], groups[i][1])
            #print(manhattan_distance(serious_guess, groups[i][0]))
            #print(manhattan_distance(groups[i][0],groups[i][1]))
            if manhattan_distance(serious_guess, groups[i][0]) < manhattan_distance(groups[i][0],groups[i][1]):
                print("Jimmy")
                break
            elif i == len(groups)-1:
                my_answer = serious_guess
                return my_answer
    return my_answer
#slow but it gets there!!

print(beacon_locator_p2(lines))
def test_beacon_locator():
    #check we can identify our grid
    #assert beacon_locator(lines) == [-2, 25]
    #check we can compute manhattan distance correctly
    #check we know an upper bound on manhattan distance to check.
    pass

def test_manhattan_distance():
    assert manhattan_distance((1,6), (-1,5)) == 3
    assert manhattan_distance((3, 5), (-1, 5)) == 4
    assert manhattan_distance((2, 3), (-1, 5)) == 5

def test_points_within_manhattan_distance():
    #assert calculate_points_within_manhattan_distance((1, 1), 2, (1,3)) == {(0, 1), (1, 2), (2, 1), (0, 0), (3, 1), (-1, 1), (1, 1), (2, 0), (1, -1), (0, 2), (2, 2), (1, 0)}
    print(calculate_points_within_manhattan_distance((1, 1), 2, (1, 3),1))
    assert calculate_points_within_manhattan_distance((1, 1), 2, (1, 3),1) == {(0, 1),(2, 1), (3, 1),(-1, 1), (1, 1)}
