file = open("Day11RawData", "r")
lines = file.readlines()
import gmpy2
#try python lambda instead

def monkeying_around(rounds):
    current_round = 0
    monkey_checks = [0 for i in range(4)]
    monkey_items = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
    while current_round < rounds:
        for i in range(len(monkey_items)):
            if i == 0:
                for k in range(len(monkey_items[i])):
                    monkey_checks[i] = monkey_checks[i] + 1
                    monkey_items[i][k] = monkey_items[i][k]*19
                    monkey_items[i][k] = (monkey_items[i][k] / 3) // 1
                    if monkey_items[i][k] % 23 == 0:
                        monkey_items[2].append(monkey_items[i][k])
                    else:
                        monkey_items[3].append(monkey_items[i][k])
                monkey_items[i] = []
            elif i == 1:
                for k in range(len(monkey_items[i])):
                    monkey_checks[i] = monkey_checks[i] + 1
                    monkey_items[i][k] = monkey_items[i][k] + 6
                    monkey_items[i][k] = (monkey_items[i][k] / 3) // 1
                    if monkey_items[i][k] % 19 == 0:
                        monkey_items[2].append(monkey_items[i][k])
                    else:
                        monkey_items[0].append(monkey_items[i][k])
                monkey_items[i] = []
            elif i == 2:
                for k in range(len(monkey_items[i])):
                    monkey_checks[i] = monkey_checks[i] + 1
                    monkey_items[i][k] = monkey_items[i][k] * monkey_items[i][k]
                    monkey_items[i][k] = (monkey_items[i][k] / 3) // 1
                    if monkey_items[i][k] % 13 == 0:
                        monkey_items[1].append(monkey_items[i][k])
                    else:
                        monkey_items[3].append(monkey_items[i][k])
                monkey_items[i] = []
            elif i == 3:
                for k in range(len(monkey_items[i])):
                    monkey_checks[i] = monkey_checks[i] + 1
                    monkey_items[i][k] = monkey_items[i][k] + 3
                    monkey_items[i][k] = (monkey_items[i][k] / 3) // 1
                    if monkey_items[i][k] % 17 == 0:
                        monkey_items[0].append(monkey_items[i][k])
                    else:
                        monkey_items[1].append(monkey_items[i][k])
                monkey_items[i] = []
        current_round += 1
    return monkey_items, monkey_checks


def monkeying_around_v2(rounds):
    current_round = 0
    monkey_checks = [0 for i in range(8)]
    monkey_items = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
    monkey_operations = [[19, 0, 1], [1, 6, 1], [1, 0, 2], [1, 3, 1]]
    #multiplication, addition, exponentiation
    monkey_friends = [[23, 2, 3], [19, 2, 0], [13, 1, 3], [17, 0, 1]]
    while current_round < rounds:
        for i in range(len(monkey_items)):
            for k in range(len(monkey_items[i])):
                monkey_checks[i] = monkey_checks[i] + 1
                #print(monkey_items[i][k])
                monkey_items[i][k] *= monkey_operations[i][0]
                monkey_items[i][k] += monkey_operations[i][1]
                monkey_items[i][k] **= monkey_operations[i][2]
                monkey_items[i][k] = (monkey_items[i][k] / 3) // 1
                if monkey_items[i][k] % monkey_friends[i][0] == 0:
                    monkey_items[monkey_friends[i][1]].append(monkey_items[i][k])
                else:
                    monkey_items[monkey_friends[i][2]].append(monkey_items[i][k])
            monkey_items[i] = []
        current_round += 1
    return monkey_items, monkey_checks

def monkeying_around_v3(rounds):
    current_round = 0
    monkey_checks = [0 for i in range(8)]
    monkey_items = [[59, 65, 86, 56, 74, 57, 56], [63, 83, 50, 63, 56], [93, 79, 74, 55], [86, 61, 67, 88, 94, 69, 56, 91], [76, 50, 51], [77, 76], [74], [86, 85, 52, 86, 91, 95]]
    monkey_operations = [[17, 0, 1], [1, 2, 1], [1, 1, 1], [1, 7, 1], [1, 0, 2], [1, 8, 1], [2, 0, 1], [1, 6, 1]]
    #multiplication, addition, exponentiation
    monkey_friends = [[3, 3, 6], [13, 3, 0], [2, 0, 1], [11, 6, 7], [19, 2, 5], [17, 2, 1], [5, 4, 7], [7, 4, 5]]
    while current_round < rounds:
        for i in range(len(monkey_items)):
            for k in range(len(monkey_items[i])):
                monkey_checks[i] = monkey_checks[i] + 1
                monkey_items[i][k] *= monkey_operations[i][0]
                monkey_items[i][k] += monkey_operations[i][1]
                monkey_items[i][k] **= monkey_operations[i][2]
                #monkey_items[i][k] = (monkey_items[i][k] / 3) // 1
                monkey_items[i][k] = monkey_items[i][k] % 9699690
                #This line is added because it is the LCM of all our divisors, so anything written mod LCM will be divisble by any of the checks
                #while also staying a minimum size
                #print(monkey_items[i][k])
                if monkey_items[i][k] % monkey_friends[i][0] == 0:
                    monkey_items[monkey_friends[i][1]].append(monkey_items[i][k])
                else:
                    monkey_items[monkey_friends[i][2]].append(monkey_items[i][k])
            monkey_items[i] = []
        current_round += 1
        print(current_round)
    monkey_checks.sort()
    return monkey_checks

#print(monkeying_around((20)))
#part 1
#print(monkeying_around_v3((20)))
#print(monkeying_around_v3((20))[len(monkeying_around_v3((20)))-1]*monkeying_around_v3((20))[len(monkeying_around_v3((20)))-2])
#part 2
print(monkeying_around_v3((10000)))
#print(monkeying_around_v3((10000))[len(monkeying_around_v3((10000)))-1]*monkeying_around_v3((10000))[len(monkeying_around_v3((10000)))-2])