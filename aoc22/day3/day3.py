import details

def read_file(file_path):
    while True:
        try:
            data = file_path.readline()
            if not data:
                break
            yield data
        except:
            raise FileNotFoundError('File not found')

def parse_lines(path):
    with open(path) as file:
        for line in read_file(file):
            yield line.strip()

def parse_3lines(path):
    lines = []
    with open(path) as file:
        for line in read_file(file):
            lines.append(line.strip())
            if len(lines) == 3:
                yield lines
                lines = []

def str_intersect(a, *b):
    return str(set(a).intersection(*b))[2]

def part1(path):
    prio = ''
    for line in parse_lines(path):
        h = len(line)//2
        prio += str_intersect(line[:h], line[h:])
    return sum((ord(i) - 96) if i.islower() else (ord(i) - 38) for i in prio)

def part2(path):
    prio = ''
    for lines in parse_3lines(path):
        prio += str_intersect(lines[0], lines[1], lines[2])
    return sum((ord(i) - 96) if i.islower() else (ord(i) - 38) for i in prio)

if __name__ == '__main__':
    def main():
        print(part1(details.day3_path))
        print(part2(details.day3_path))
    main()