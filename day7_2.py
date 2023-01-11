def parser():
    with open("inputday7.txt", "r") as f:
        commands = ['cd','ls']
        lines = [line.replace('$', '').split() for line in f.readlines()]
        for line in lines:
            if line[0] == 'dir':
                line.pop(0)
            elif line[0].isnumeric():
                line.pop(1)
        result = []
        for i in lines:
            if i[0] in commands:
                result.append([' '.join(i),[]])
            else:
                result[-1][1].append(i[0])
    return result

class Directory:
    def __init__(self, name, parent, children, files_size):
        self.name = name
        self.parent = parent
        self.children = children
        self.files_size = files_size
        self.total_size = 0

def get_directory(commands):
    top_directory = Directory('/', None, [], 0)
    current_Directory = top_directory
    for command in commands:
        cmd, out = command
        if cmd == 'cd /':
            current_Directory = top_directory
        elif cmd == 'cd ..':
            current_Directory = current_Directory.parent
        elif 'cd' in cmd:
            current_Directory = [child for child in current_Directory.children if child.name == cmd.split()[1]][0]
        elif cmd == 'ls':
            current_Directory.children = [Directory(i, current_Directory, [], 0) for i in out if i.isalpha()]
            current_Directory.files_size = sum([int(i) for i in out if i.isnumeric()])
    return top_directory

def set_sizes(directory):
    directory.total_size = directory.files_size + sum([set_sizes(child) for child in directory.children])
    return directory.total_size

def setup():
    parsed = parser()
    directory = get_directory(parsed)
    set_sizes(directory)
    return directory

def process(directory, maximum):
    return (directory.total_size if directory.total_size <= maximum else 0) + sum ([process(child, maximum) for child in directory.children])

top = setup()
maximum = 100000
#print(process(top, maximum))

def process2(directory, size_needed, system_size, used_size):
    return min([directory.total_size if used_size - directory.total_size + size_needed <= system_size else system_size, *[process2(child, size_needed, system_size, used_size) for child in directory.children]])

total = 70000000
needed = 30000000
print(process2(top, needed, total, top.total_size))