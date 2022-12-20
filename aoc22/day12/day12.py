import pathlib
import collections

day12_input = pathlib.Path(__file__).with_name('day12_input.txt')
Point = collections.namedtuple('Point', ['x', 'y'])

def process_file(path: pathlib.WindowsPath) -> tuple[list[list[str]], list[Point]]:
    grid = []
    start_values = [Point(0,0)]
    with open(path) as file:
        for i, n in enumerate(file.read().splitlines()):
            grid.append([char for char in n])
            for j, n in enumerate(n):
                if n == 'S':
                    start_values[0] = Point(i, j)
                if n == 'a':
                    start_values.append(Point(i, j))
    return grid, start_values

def shortest_path(grid: list[list[str]], start_point: Point) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = collections.deque([(start_point, [])]) # track current path as well as point
    while queue:
        point, path = queue.popleft()
        if grid[point.x][point.y] == 'E':
            return len(path)
        path.append(point)
        curr_val = grid[point.x][point.y]
        for dx, dy in [[0,1], [0,-1], [-1,0], [1,0]]:
            new_point = Point(point.x + dx, point.y + dy)
            if new_point.x in range(rows) and new_point.y in range(cols) and new_point not in visited:
                # 'E' can only be reached from 'y' or 'z', 'a' is always reachable and other values can only be reached if they are at most one higher than the current value 
                if grid[new_point.x][new_point.y] == 'a' or (grid[new_point.x][new_point.y] != 'E' and ord(curr_val) + 1 >= ord(grid[new_point.x][new_point.y])) or (curr_val in {'y', 'z'} and grid[new_point.x][new_point.y] == 'E'):
                    queue.append((new_point, path[:]))
                    visited.add(new_point)
    return -1 # Result not found
            
if __name__ == '__main__':
    grid, start_values = process_file(day12_input)
    print(shortest_path(grid, start_values[0])) # Part 1
    print(min(shortest_path(grid, start_point) for start_point in start_values if shortest_path(grid, start_point) > 0)) # Part 2
