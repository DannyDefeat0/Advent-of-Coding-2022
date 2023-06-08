file = open("Day13RawData", "r")
lines = file.readlines()
import copy

#good project for unit testing
#test driven development
#write a test knowing it will fail, then writing it to make it pass
#The clean coder robert c mart

#for example, add up all the numbers in array and make sure it matches index sum

# we have a set of rules that each
def rules_check(first, second):
    # print(first, second)
    # Check automatically fails if rightside runs out of items unless both are equal, so make that the first check
    while min(len(first),len(second)) > 0:
        firsty = first.pop(0)
        secondy = second.pop(0)
        #print(firsty, secondy)
        if isinstance(firsty, int) and isinstance(secondy, int):
            if secondy < firsty:
                return False
            elif firsty < secondy:
                return True
        elif isinstance(firsty, int):
            sub_check = rules_check(list([firsty]),secondy)
            if sub_check != "even":
                return sub_check
        elif isinstance(secondy, int):
            sub_check = rules_check(firsty,list([secondy]))
            if sub_check != "even":
                return sub_check
        elif isinstance(firsty, list) and isinstance(secondy, list):
            sub_check = rules_check(firsty,secondy)
            if sub_check != "even":
                return sub_check
    if len(first) < len(second):
        return True
    elif len(first) > len(second):
        return False
    else:
        return "even"


def stickler(source):
    index_sum = 0
    indexes = []
    current_index = 0
    for i in range(len(source) - 1):
        if source[i] == "\n" or source[i + 1] == "\n":
            pass
        else:
            current_index += 1

            top_pair = eval(source[i].replace("\n", ""))
            bottom_pair = eval(source[i + 1].replace("\n", ""))
            #print(top_pair)
            #print(bottom_pair)
            # print("\n")
            if rules_check(top_pair, bottom_pair):
                # print(top_pair, bottom_pair, current_index)
                index_sum += current_index
                indexes.append(current_index)
    return index_sum, indexes

def indexer(source):
    indexes = [[[2]], [[6]]]
    #step - 1 - organize all packets into list
    for i in range(len(source) - 1):
        if source[i] == "\n" or source[i + 1] == "\n":
            pass
        else:
            top_pair = eval(source[i].replace("\n", ""))
            bottom_pair = eval(source[i + 1].replace("\n", ""))
            indexes.append(top_pair)
            indexes.append(bottom_pair)
    #step 2 - sort the list by moving each item until everything behind it is less than it
    return indexes


def two_check(source):
    starting_index = 0
    for i in range(len(source)):
        if rules_check(source[i], [[2]]):
            starting_index += 1
    return starting_index


def six_check(source):
    starting_index = 0
    for i in range(len(source)):
        if rules_check(source[i], [[6]]):
            starting_index += 1
    return starting_index

def swap(list, first, second):
    list[first], list[second] = list[second], list[first]
    return list


# we need a function that takes a string and converts it into a list of lists.
#print(stickler(lines))
#print(sorter(removal(indexer(lines))))
print(two_check(indexer(lines)))
print(six_check(indexer(lines)))
print(six_check(indexer(lines))*two_check(indexer(lines)))


def test():
    test_final_result = 13
    test_final_array = [1, 2, 4, 6]
    assert sum(test_final_array) == test_final_result
    #this will throw an error and stop every line after if the check isn't true
    print("whatever")
    #print will only show if the assert passes
#test()
    #we want this test to verify that it can compare certain types
    #we want the indexes of pairs that return true to sum correct
