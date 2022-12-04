import re
from pathlib import Path 

day4_input = Path(__file__).with_name('input.txt')

def read_file(path):
    while True:
        try:
            data = path.readline()
            if not data:
                break
            yield data
        except:
            raise FileNotFoundError('File not found')

def parse_line(path):
    with open(path) as file:
        for line in read_file(file):
            yield line.strip()

def assignment_overlap(path, overlap = False):
    contain_ctr = 0
    overlap_ctr = 0
    for line in parse_line(path):
        x, y, a, b = map(int, re.findall(r'\d+', line))
        if x <= a and y >= b or x >= a and y <= b:
            contain_ctr += 1
        if y >= a and x <= b:
            overlap_ctr += 1
    return contain_ctr if overlap == False else overlap_ctr

if __name__ == '__main__':
    def main():
        print(assignment_overlap(day4_input))
        print(assignment_overlap(day4_input, True))
    main()