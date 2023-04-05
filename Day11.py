file = open("Day11RawData", "r")
lines = file.readlines()


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

print(monkeying_around((20)))