import pathlib
from collections import defaultdict

day7_input = pathlib.Path(__file__).with_name('day7_input.txt')

def read_file(path: pathlib.WindowsPath) -> list[str]:
    try:
        with open(path) as file:
            return process_lines(file.read().splitlines())
    except FileNotFoundError:
        raise FileNotFoundError('File not found')

def process_lines(commands: list[str]) -> list[str]:
    command_list = []
    for line in commands:
        line.strip('\n')
        # only need dir names, file sizes, file names and '..'
        if line.startswith('$ dir ') or line.startswith('$ cd '):
            command_list.append(line.rsplit(' ', 1)[1])
        elif line[0].isdigit():
            command_list.append(line)
    return command_list

'''
Solution implemented using a tree with a recursive DFS
'''
class Node:
    '''
    Each node in the tree represents a directory
    '''
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent    
        # sub-directories kept in a dict to avoid duplicates
        self.children = []
        # files of the form {file_name : file_size} - defaultdict(int) for key errors
        self.files = defaultdict(int)
    
    def add_dir(self, node: 'Node'):
        # duplicate entries are checked in the build_tree function
        node.parent = self
        self.children.append(node)

    def add_file(self, name: str, size: int):
        self.files[name] = size

    def dir_size(self) -> int:
        # sum of file sizes in the directory if no sub-directories
        if not self.children:
            return sum(self.files.values())
        # sum of file sizes in the directory and all sub-directories
        else:       
            return sum(self.files.values()) + sum(child.dir_size() for child in self.children)

def build_tree(commands: list[str]) -> Node:
    '''
    Build directory tree from the processed lines
    '''
    # root directory
    root = Node(commands[0])
    curr_node = root
    for i in range(1, len(commands)):
        # if cmd is a file add to current directory if it doesn't exist
        if commands[i].split()[0].isnumeric():
            size, name = commands[i].split(' ', 1)
            if name not in curr_node.files:
                curr_node.add_file(name, int(size))
        # elif cmd is '..' go up one directory
        elif commands[i] == '..':
            curr_node = curr_node.parent
        # else cmd must be directory name - add new child node if it does't exist
        else:
            if commands[i] not in curr_node.children:
                directory = Node(commands[i])
                curr_node.add_dir(directory)
                curr_node = directory
    return root

def dfs1(node: Node) -> int:
    '''
    Recursive ordered DFS to get sum of directories < 100000 in size
    '''
    # base case: no sub-directories
    if not node.children:
        return node.dir_size() if node.dir_size() < 100000 else 0
    # recursive case: sum of file sizes in current directory and all sub-directories
    else:
        if node.dir_size() < 100000:
            return node.dir_size() + sum(dfs1(child) for child in node.children)
        else:
            return sum(dfs1(child) for child in node.children)

def dfs2(node: Node, min_dir_size: int, minimum: int) -> int:
    '''
    Recursive ordered DFS to smallest directory larger than the minimum directory size
    '''
    # base case: no sub-directories
    if not node.children:
        return minimum
    # update minimum if needed
    if node.dir_size() > min_dir_size and node.dir_size() < minimum:
        minimum = node.dir_size()
    # recursive case: minimum size of all sub-directories with size > min_dir_size and > minimum
    return min(dfs2(child, min_dir_size, minimum) for child in node.children)

if __name__ == '__main__':
    commands = read_file(day7_input)
    tree = build_tree(commands)
    # solution to part 1
    print(dfs1(tree))
    # solution to part 2 
    min_size = 30000000 - (70000000 - tree.dir_size())
    print(dfs2(tree, min_size, tree.dir_size()))