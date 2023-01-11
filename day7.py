

class TreeNode:
    def __init__(self, is_dir: bool, name, size=None):
        self.is_dir = is_dir
        self.name = name
        self.size = size
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_size(self):
        if self.is_dir:
            total_size = 0
            for child in self.children:
                total_size += child.get_size()
            return total_size
        else:
            return self.size
    def find_subdirectories_part1(self):
        dir_sizes = 0
        if self.is_dir:
            for child in self.children:
                if child.is_dir and child.get_size() <= 100000:
                    dir_sizes += child.get_size() + child.find_subdirectories_part1()
                else:
                    dir_sizes += child.find_subdirectories_part1()
        return dir_sizes

    def find_subdirectories_part2(self, min_size):
        dir_sizes = []
        if self.is_dir:
            for child in self.children:
                if child.is_dir and child.get_size() >= min_size:
                    dir_sizes += [child.get_size()] + child.find_subdirectories_part2(min_size)
                else:
                    dir_sizes += child.find_subdirectories_part2(min_size)
        return dir_sizes

    def print_children(self, level):
        if self.is_dir:
            print('--' * level + self.name + ' (total=' + str(self.get_size()) +')')
        else: 
            print('--' * level + self.name + ' (file=' + str(self.get_size()) +')')
        if len(self.children) > 0:
            for child in self.children:
                child.print_children(level+1)
    def print_children(self, level):
        if self.is_dir:
            print('--' * level + self.name + ' (total=' + str(self.get_size()) +')')
        else: 
            print('--' * level + self.name + ' (file=' + str(self.get_size()) +')')
        if len(self.children) > 0:
            for child in self.children:
                child.print_children(level+1)

class Tree:
    def __init__(self) -> None:
        self.root = TreeNode(is_dir=True, name="root")
        self.current = self.root 

    def reset_to_root(self):
        self.current = self.root

    def go_up_one_level(self):
        self.current = self.current.parent

    def go_to_child(self, name):
        self.current = list(filter(lambda child: child.name == name, self.current.children))[0]

    def add_new_child(self, child):
        self.current.add_child(child)

def input():
    with open('inputday7.txt', 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    tree = Tree()

    while len(lines) > 0:
        line = lines.pop(0)
        if line == '$ cd /': 
            tree.reset_to_root()
        elif line == '$ ls':
            while len(lines)>0 and '$' not in lines[0]:
                line = lines.pop(0)
                size, name = line.split(' ')
                if size.isdigit():
                    new_node = TreeNode(is_dir=False, name=name, size=int(size))
                else:
                    new_node = TreeNode(is_dir=True, name=name)
                tree.add_new_child(new_node)
        elif line == '$ cd ..':
            tree.go_up_one_level()
        elif '$ cd' in line:
            _, _, name = line.split(' ')
            tree.go_to_child(name)
    #tree.root.print_children(0)
    tree.root.find_subdirectories_part1()

input()