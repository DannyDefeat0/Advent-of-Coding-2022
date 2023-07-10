file = open("Day16RawData", "r")
lines = file.readlines()
from collections import deque


class Pipe:
    instances = []
    def __init__(self, name, flow_rate, connected_pipes):
        self.__class__.instances.append(self)
        self.name = name
        self.flow_rate = flow_rate
        self.connected_pipes = connected_pipes
    def __repr__(self):
        return self.name


def pipe_layout(source):
    for pipe in source:
        pipe_name = pipe.split()[1]  # Extracts "AA"
        flow_rate = int(pipe.split("rate=")[1].split(";")[0].strip())  # Extracts 0
        if "valves" in pipe:
            connected_pipes = pipe.split("valves ",1)[1]
        else:
            connected_pipes = pipe.split("valve ",1)[1]
        connected_pipes_list = [p.strip() for p in connected_pipes.split(",")]
        #print(connected_pipes)
        pipe_instance = Pipe(pipe_name, flow_rate, connected_pipes_list)
    return Pipe.instances
from collections import deque


def pipe_distance(pipe1_name, pipe2_name, layout):
    distance = 0
    distance_known = False

    for pipe in layout:
        if pipe.name == pipe1_name:
            pipe1 = pipe
        if pipe.name == pipe2_name:
            pipe2 = pipe

    if pipe2_name in pipe1.connected_pipes:
        distance = 1
        distance_known = True
    while not distance_known:
        new_connected_pipes = []
        explored_pipes = set()
        for connected_pipe_name in pipe1.connected_pipes:
            #print(pipe1.connected_pipes)
            print(connected_pipe_name)
            if connected_pipe_name not in explored_pipes:
                distance += 1
                for pipe in layout:
                    if pipe.name == connected_pipe_name:
                        connected_pipe = pipe
                        new_connected_pipes.extend(connected_pipe.connected_pipes)
                        if pipe2_name in connected_pipe.connected_pipes:
                            distance_known = True
                            break
                explored_pipes.add(connected_pipe_name)
        if not distance_known:
            distance += 1
            pipe1_name = pipe2_name  # Move to the next connected pipe
            pipe1 = pipe2
    return distance


def pipe_opener(layout, current_pipe, max_time):
    current_time = 0
    total_flow = 0
    while current_time < max_time:
        time_fence = max_time - current_time
        #time fences are cool
        best_flow = 0
        flow_index = 0
        for i in range(len(layout)):
            #go by index so we can decide which pipe to adjust by later
            if layout[i] == current_pipe:
                pass
            #check only reachable pipes with positive flow. If it would take too long to get to a pipe we can ignore it.
            elif layout[i].flow_rate != 0 and pipe_distance(current_pipe, layout[i],layout) <= time_fence:
                distance = pipe_distance(current_pipe, layout[i],layout)
                flow_rate = (layout[i].flow_rate * (max_time - current_time - distance))/distance
                if flow_rate > best_flow:
                    best_flow = flow_rate
                    flow_index = i
                if i == len(layout):
                    total_flow += best_flow
                    layout[flow_index].flow_rate = 0
                    pipe1 = layout[flow_index]
            elif best_flow == 0:
                break
                #should only happen if we run out of eligible targets before the time runs out
    return total_flow




    #define the flow rate we will use this to determine which Pipe is the best choice at a given time t
    #release that pipe and set it's new value to 0, we can't open it twice so it is effectively 0 for future times
    #if all pipes are at 0 flow rate or there is not enough time left to open another pipe, hault the program


def test_pipe_layout():
    assert pipe_layout(lines) == ["AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ"]
    #assert pipe distance("AA","AA") == 0
    #assert pipe_distance("AA","BB") == 1
    #assert pipe_distance("AA", "FF") == 3
def test_pipe_distance():
    assert pipe_distance("AA","BB",pipe_layout(lines)) == 1
    assert pipe_distance("AA","HH",pipe_layout(lines)) == 5
#test_pipe_distance()
#print(pipe_layout(lines))
#print(pipe_distance("AA","CC",pipe_layout(lines)))
print(pipe_opener(pipe_layout(lines),pipe_layout(lines)[0],30))

