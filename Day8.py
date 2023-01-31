file = open("Day8rawData", "r")
lines = file.readlines()

# visibility means anywhere outside the grid (up, down, left, right)
# the first visible tree in a row or column determines the threshold for the next tree
# For example, if the perimeter were all 9s, we would not need to check anything on the inside

visible_trees = 0


def height_check(n, checks):
    for check in checks:
        if check >= n:
            return False
    return True


def lookout(n, checkers):
    for checker in checkers:
        if height_check(int(n), checker) == True:
            return True
    return False


# print(height_check(1,[0,0]))
max_viewing_distance = 0


def viewing_distance(n, checks):
    for i in range(len(checks)):
        if checks[i] >= int(n) or i == len(checks):
            view_distance = i+1
            break
        elif i == 0:
            view_distance = 1
        else:
            view_distance = i+1
    return view_distance


def ideal_spot_finder(n, checkers):
    total_viewing_distance = 1
    for checker in checkers:
        #print(str(n) + str(checker) + str(viewing_distance(n, checker)))
        total_viewing_distance = total_viewing_distance * viewing_distance(n, checker)
    return total_viewing_distance


for i in range(len(lines)):
    line = lines[i]
    # print(line)
    for k in range(len(line)):
        # check if outside
        match_found = False
        if ((k == 0 or k == len(line) - 2) or (line == lines[0] or line == lines[len(lines) - 1])) and line[
            k].isdigit():
            visible_trees += 1
            # print(visible_trees)
            # print(line[k])
            continue
        # check above trees
        elif line[k].isdigit():
            top_rows = lines[0:i]
            top_check = [int(top_row[k]) for top_row in top_rows]
            top_check.reverse()
            bottom_rows = lines[i + 1:len(lines)]
            bottom_check = [int(bottom_row[k]) for bottom_row in bottom_rows]
            lefties = line[0:k]
            left_check = [int(left) for left in lefties]
            left_check.reverse()
            righties = line[k + 1:len(line) - 1]
            right_check = [int(right) for right in righties]
            #ideal_spot_finder(line[k], [left_check, right_check, top_check, bottom_check])
            if lookout(line[k], [left_check, right_check, top_check, bottom_check]) == True:
                # print(line[k] + str([left_check, right_check, top_check, bottom_check]))
                visible_trees += 1

            if ideal_spot_finder(line[k], [left_check, right_check, top_check, bottom_check]) > max_viewing_distance:
                #print(max_viewing_distance)
                max_viewing_distance = ideal_spot_finder(line[k], [left_check, right_check, top_check, bottom_check])
        else:
            pass

print(visible_trees)
print(max_viewing_distance)

