import pathlib

day10_input = pathlib.Path(__file__).with_name('day10_input.txt')

def process_file(path: pathlib.WindowsPath):
    with open(path) as file:
        for line in file:
            yield [0, int(line.rsplit()[-1])] if line.strip()[-1].isdigit() else [0]

def crt_and_signal_strength(path: pathlib.WindowsPath) -> int:
    cycle, reg, signal_strength = 1, 1, 0
    crt_values = []
    for values in process_file(path):
        for val in values:
            signal_strength += reg * cycle if (cycle + 20) % 40 == 0  else 0
            crt_values.append('#' if cycle%40 - 1 in range(reg-1, reg+2) else ' ')
            print(reg, cycle)
            reg += val
            cycle += 1
    for i in range(0, len(crt_values), 40):
        print(''.join([char for char in crt_values[i:i+40]]))
    return signal_strength

if __name__ == '__main__':
    print('\nSignal strength is: ' + str(crt_and_signal_strength(day10_input)))