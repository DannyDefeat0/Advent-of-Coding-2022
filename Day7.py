file = open("Day7rawData", "r")
lines = file.readlines()

class Directory:
    instances = []
    def __init__(self, name, subdirectories=None, parent=None, size=0):
        self.__class__.instances.append(self)
        self.parent = parent
        self.name = name
        self.subdirectories = []
        self.size = size
        if subdirectories is not None:
            for subdirectory in subdirectories:
                self.add_subdirectory(subdirectory)
    def __repr__(self):
        return self.name
    def add_subdirectory(self, folder):
        #assert isinstance(folder, Directory)
        self.subdirectories.append(folder)
        folder.parent = self
    def add_size(self,files):
        self.size += files
    def update_parents(self, files):
        if self.parent is None:
            self.add_size(files)
        else:
            self = self.parent
            self.add_size(files)
            self.update_parents(files)


subfolders = []
file_sizes = 0
answers = {}
directory = Directory("/", subfolders, None, file_sizes)
current_directory = directory





for line in lines:
    if "$ cd /" in line:
        pass
    elif "$ cd" in line and ".." not in line:
        # cd only lets us move within a folder
        # whatever it does we need to make sure it only moves down (or nowhere)
        for subdirectory in current_directory.subdirectories:
            z = (current_directory.name + "/" + line.split()[-1]).replace("//","/")
            #print(z)
            subdirectory.name
            if z == subdirectory.name:
                #print(subdirectory.name)
                current_directory = subdirectory
    elif "dir " in line:
        # dir means we need to append a subfolder to the current directory
            current_directory.add_subdirectory(Directory((current_directory.name+"/"+line.split()[-1]).replace("//","/")))
        # DRY the replace here is repeating, could likely avoid by setting a better starting variable
    elif "$ ls" in line:
        pass
    elif "$ cd .." in line:
        current_directory = current_directory.parent
    elif str(line[0]).isdigit():
        # if the line has no cd, ls, or dir mentions, update the file sizes of all relevant directories
        current_directory.add_size(int(line.split()[0]))
        current_directory.update_parents(int(line.split()[0]))
#print(Directory.instances)
#This is just a gut check that the directories we're creating look accurate.
total = 0
target = 8381165000000000
for thing in Directory.instances:
    #print([total, thing.size])
    if thing.size < 100001:
        total += thing.size
    if thing.size - 8381165 >= 0 and thing.size < target:
        target = thing.size
print(total)
print(target)