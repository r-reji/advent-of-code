import pathlib

day9_input = pathlib.Path(__file__).with_name('day9_input.txt')

def read_file(path: pathlib.WindowsPath):
        with open(path) as file:
            for line in file:
                yield line.rstrip().split()

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def move_tail(self, tail: 'Point') -> 'Point':
        xy_diff = (abs(self.x - tail.x), abs(self.y - tail.y))
        if xy_diff[0] == 2 or xy_diff[1] == 2:
            if xy_diff[0] == 2 and xy_diff[1] == 2:
                return Point(tail.x + (self.x - tail.x)//2, tail.y + (self.y - tail.y)//2)
            if sum(xy_diff) == 2:
                return Point(tail.x + (self.x - tail.x)//2, tail.y + (self.y - tail.y)//2)
            else:
                if xy_diff[0] == 2:
                    return Point(tail.x + (self.x - tail.x)//2, tail.y + (self.y - tail.y))
                else:
                    return Point(tail.x + (self.x - tail.x), tail.y + (self.y - tail.y)//2)
        else:
            return tail

def tail_visits(path: pathlib.WindowsPath) -> tuple[int]:
    head, tail = Point(), Point()
    knots = [Point() for _ in range(10)]
    moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    rope1_tail_visits, rope2_tail_visits = set(), set()
    for move in read_file(path):
        for _ in range(int(move[1])):
            head.x, head.y = head.x + moves[move[0]][0], head.y + moves[move[0]][1]
            knots[0] = head
            tail = head.move_tail(tail)
            for i in range(1, 10):
                knots[i] = knots[i-1].move_tail(knots[i])
            rope1_tail_visits.add((tail.x, tail.y))
            rope2_tail_visits.add((knots[-1].x, knots[-1].y))
    return len(rope1_tail_visits), len(rope2_tail_visits)

if __name__ == '__main__':
    print(tail_visits(day9_input))