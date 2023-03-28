file = open("Day10RawData", "r")
lines = file.readlines()

#addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
#noop takes one cycle to complete. It has no other effect.

signal_strength = [0,1]
signals = {}
#part 2 notes
#our sprite is 3 pixels wide ###
#each time we update a cycle we're checking if the cycle numbers matches x + or - 1
output = ["." for i in range(240)]


def run_noop(cycle, x):
    if cycle % 40 in (x-1, x, x+1):
        output[cycle] = "#"
    cycle += 1
    if cycle % 20 == 0:
        signals[str(cycle)] = cycle * x
    return [cycle, x]
def run_addx(cycle, x, num):
    final = cycle + 2
    while cycle < final:
        if cycle % 40 in (x - 1, x, x + 1):
            output[cycle] = "#"
        cycle += 1
        if cycle % 20 == 0 and cycle != final:
            signals[str(cycle)] = cycle*x
    if cycle % 20 == 0:
        signals[str(cycle)] = cycle * x
    x = x + num
    if cycle % 40 in (x - 1, x, x + 1):
        output[cycle] = "#"
    return [cycle, x]
def instructions(command, cycle, x, num):
    if command == "noop":
        [cycle,x] = run_noop(cycle, x)
    else:
        [cycle, x] = run_addx(cycle, x, num)
    return [cycle, x]
for line in lines:
    input = line.split()
    command = input[0]
    if command == "noop":
        num = ""
    else:
        num = int(input[-1])
    signal_strength = instructions(command, signal_strength[0], signal_strength[1], num)
    #print(command, num, signal_strength)

asks = ['20', '60', '100', '140', '180', '220']
checks = [1,41,81,121,161,201]
total = 0
for i in asks:
    total += signals[i]
    #print(signals[i])
print(total)
for i in checks:
    print(output[i-1:i+39])
