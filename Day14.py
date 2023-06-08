file = open("Day14RawData", "r")
test_file = open("TestBatch", "r")
lines = file.readlines()
print(lines)



# we need a function that takes a given path and traces out rocks to fill it in straight lines (or at least something that behaves that way)

# we need to def a function to model a grain of sand falling on our grid

# we need a function that updates our grid based on how the sand would fall

# ideally we'd know the end points ahead of time to that any falling sand that would hit those coordinates is ruled invalid

#there's a way to get the answer without simulating sand falling
#try to write this out in psuedocode first

#sand will come to rest anywhere there is a path for sand to get to
#mutability/immutability - memory


def path_converter(source):
    rocks = []
    # takes a given path as a list and converts it into a list for ease of tracking rocks.
    for item in source:
        item = item.strip().split(' -> ')
        rock_coordinates = [[int(coordinate.split(',')[0]), int(coordinate.split(',')[1])] for coordinate in item]
        item = rock_coordinates
        for i in range(len(item) - 1):
            # paths need to be straight and without gaps
            if i != len(item) - 1:
                x1 = item[i][0]
                x2 = item[i + 1][0]
                y1 = item[i][1]
                y2 = item[i + 1][1]
                if abs(x2 - x1) >= 1:
                    new_x1 = x1
                    while abs(x2 - new_x1) > 1:
                        if x2 > x1:
                            new_x1 += 1
                            rocks.append([new_x1, y1])
                        if x2 < x1:
                            new_x1 -= 1
                            rocks.append([new_x1, y1])
                if abs(y2 - y1) >= 1:
                    new_y1 = y1
                    while abs(y2 - new_y1) > 1:
                        if y2 > y1:
                            new_y1 += 1
                            rocks.append([x1, new_y1])
                        if y2 < y1:
                            new_y1 -= 1
                            rocks.append([x1, new_y1])
        for rock in item:
            rocks.append(rock)
        #print(item)
        #print(rocks)
    return rocks


def test_path_converter():
    # assert path_converter(['498,4 -> 498,6 -> 496,6\n']) == [[498,4], [498,6], [496,6]]
    # first test was to make sure we could take a line and convert it into a list of coordinates as expected
    list1 = [[498, 4], [498, 5], [498, 6], [497, 6], [496, 6]]
    list2 = path_converter(['498,4 -> 498,6 -> 496,6\n'])

    assert all(item in list2 for item in list1)
    # second step is to fill in the gaps

def sandfall(rocks, drop_point):
    sand_count = 0
    #set boundaries
    safe = True
    #we can probably delete this part later if our boundary check is good enough
    #lol nvm we actually needed this for part 2
    max_row = 0
    for i in range(len(rocks)):
        if rocks[i][1] > max_row:
            max_row = rocks[i][1]
    max_row = max_row + 2
    cone_of_shame = [[i, max_row] for i in range(0,1000000000)]
    rocks.extend(cone_of_shame)
    assert isinstance(drop_point, object)
    sand_point = drop_point
    while safe:
        #sand always checks down first
        if sand_point in rocks:
            safe = False
        elif [sand_point[0],sand_point[1]+1] in rocks:
            #check one down and to the left
            if [sand_point[0]-1,sand_point[1]+1] not in rocks:
                sand_point = [sand_point[0]-1,sand_point[1]+1]
            #check one down and to the right
            elif [sand_point[0]+1,sand_point[1]+1] not in rocks:
                sand_point = [sand_point[0] + 1, sand_point[1] + 1]
            else:
            #rest if blocked
                sand_count += 1
                rocks.append(sand_point)
                sand_point = drop_point
            #sand is just a rock you haven't met yet
        elif sand_point[1]+1 > max_row:
            safe = False
            print("fell off")
        else:
            sand_point = [sand_point[0],sand_point[1]+1]
    return sand_count

def sandfall_p2(rocks, drop_point):
    sand_count = 0
    max_row = 0
    for i in range(len(rocks)):
        if rocks[i][1] > max_row:
            max_row = rocks[i][1]
    max_row = max_row + 2
    has_roof = []
    #cone_of_shame = [[i, max_row] for i in range(0,100000)]
    #rocks.extend(cone_of_shame)
    #sorted_rocks = sorted(rocks, key=lambda coord: coord[1])
    for i in range(max_row):
        #define a list of points to check in each row
        points_to_check = [[x,i] for x in range(drop_point[0]-i, drop_point[0]+i+1)]
        for point in points_to_check:
            roofs = [[point[0],point[1]+1], [point[0]-1,point[1]+1], [point[0]+1,point[1]+1]]
        #check if there's a rock there
            if point in rocks:
                #print("damn it Jim")
                pass
            # if there isn't a rock check if it has a roof
            elif all(roof in rocks for roof in roofs) or all(roof in has_roof for roof in roofs):
                has_roof.append(point)
                pass
            # notably, if a point has a roof, it follows that any point below
            # finally, if there are no obstructions increase the sandcount
            else:
                sand_count += 1
    return sand_count




def test_sandfall():
    #assert sandfall((path_converter(lines)),[500,0]) == 9
    #assert sandfall((path_converter(lines)), [0, 0]) == 0
    #early test to see if we can stack or if sand would fall into the depths
    assert sandfall((path_converter(lines)), [500, 0]) == 24

print(sandfall_p2(path_converter(lines),[500,0]))
#print(sandfall(path_converter(lines),[500,0]))
#test_path_converter()
#path_converter(lines)
#test_sandfall()