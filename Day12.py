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
#print(starters)
visited = []
queue = []
def traverse(visited, coordinates, test):
    visited.append(test)
    queue.append(test)

    while queue:
        #print(queue)
        node = queue.pop(0)
        current = node
        if len(node) > 2:
            current = node[-1]
        current_height = coordinates[current]
        for neighbor in [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]:
            if neighbor not in visited and neighbor in coordinates and coordinates[neighbor] <= current_height + 1:
                current_path = list(node)
                current_path.append(neighbor)
                visited.append(neighbor)
                queue.append(current_path)
                if neighbor == final:
                    return len(current_path)-2

#print((traverse(visited, Nodes.instances, start)))
small = 391

starters = [key for key, value in Nodes.instances.items() if value < 2]
#takes a few minutes but eventually we get 386
for starter in starters:
    #print(starter)
    visited = []
    queue = []
    result = traverse(visited, Nodes.instances, starter)
    if result is not None:
        if result < small:
            small = result
            print(small)
            print(result)
            visited = []
            queue = []
print(small)





#def traverse(Start, End, Graph):


