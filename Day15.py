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

def calculate_points_within_manhattan_distance(point, distance,beacon):
    x, y = point
    points = set()
    for i in range(-distance, distance+1):
        for j in range(-distance, distance+1):
            if abs(i) + abs(j) <= distance and (x + i, y + j) != beacon:
                points.add((x + i, y + j))
    print("Steve")
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
        not_beacon = calculate_points_within_manhattan_distance(sensor, manhattan_distance(sensor, beacon),beacon)
        for dud in not_beacon:
            not_beacons.add(dud)
        #print(not_beacons)
    y10_count = 0
    for item in not_beacons:
        if item[1] == 2000000:
            print("Jim")
            y10_count += 1
    print(y10_count)
    return groups


beacon_locator(lines)
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
    assert calculate_points_within_manhattan_distance((1, 1), 2, (1,3)) == {(0, 1), (1, 2), (2, 1), (0, 0), (3, 1), (-1, 1), (1, 1), (2, 0), (1, -1), (0, 2), (2, 2), (1, 0)}


test_beacon_locator()
test_manhattan_distance()
test_points_within_manhattan_distance()