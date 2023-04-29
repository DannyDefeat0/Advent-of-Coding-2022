file = open("Day12RawData", "r")
lines = file.readlines()

#for Dijkstra's algorithm we will treat this as if it were an undirected graph with weights 1 for all nodes
#every node has a row, height, and value which we define using ord
#from there we'll define a starting node and ending node

class Nodes:
    instances = {}
    def __init__(self, Node=0, row=0, column=0):
        key = (row, column)
        #self.__class__.instances.append(self)

        self.Node = Node
        self.__class__.instances[key] = self.Node
        #Node will be the ord value of the letter
        #row and column will indicate its position
        self.row = row
        self.column = column

for i in range(len(lines)):
    for k in range(len(lines[i])):
        value = lines[i][k]
        if lines[i][k] == "S":
            value = "`"
            #here I just force the starting point to be zero
        if lines[i][k] != "\n":
            #print(abs(ord(value)-96))
            #worth noting that (abs(ord("E")) is 27, making it the highest point after we reduce everything by 96.
            n = Nodes(abs(ord(value)-96), i, k)



peak = max(Nodes.instances.values())
lowest = min(Nodes.instances.values())

for key, value in Nodes.instances.items():
    if value == peak:
        final = key
    if value == lowest:
        start = key
print(start, final)
def traverse(start, final, coordinates):
    distances = {coordinate: float('inf') for coordinate in coordinates}
    distances[start] = 0
    previous = {coordinate: None for coordinate in coordinates}
    visited = set()
    current_path = [start]
    possible_solutions = []
    shortest_path_length = 500
    while final not in visited:
        #print(len(current_path))
        current_coordinate = min({coordinate: distance for coordinate, distance in distances.items() if coordinate not in visited}, key=distances.get)
        if distances[current_coordinate] == float('inf'):
            return None
        visited.add(current_coordinate)
        for neighbor in [(current_coordinate[0] + 1, current_coordinate[1]), (current_coordinate[0] - 1, current_coordinate[1]), (current_coordinate[0], current_coordinate[1] + 1), (current_coordinate[0], current_coordinate[1] - 1)]:
            if neighbor in coordinates and neighbor not in visited and coordinates[neighbor] <= coordinates[current_coordinate] + 1:
                new_distance = distances[current_coordinate] + 1
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_coordinate
    shortest_path = []
    current_coordinate = final
    while current_coordinate is not None:
        shortest_path.append(current_coordinate)
        current_coordinate = previous[current_coordinate]
    return len(shortest_path)-1
print(traverse(start, final, Nodes.instances))




#def traverse(Start, End, Graph):


