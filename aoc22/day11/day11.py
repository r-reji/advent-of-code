import pathlib
import collections
import re
import copy

day11_input = pathlib.Path(__file__).with_name('day11_input.txt')

class Monkey:
    def __init__(self, operation: str, test = 0, throw = (0,0)):
        self.items = collections.deque() # FIFO
        self.operation = lambda x: eval(str(x) + operation)
        self.test = test
        self.throw = throw # (true, false)
        self.inspect_count = 0

    def turn(self, reset = True):
        while self.items:
            item = self.operation(self.items.popleft())
            new_worry = item // 3 if reset == True else item % 9699690
            yield (new_worry, self.throw[int(new_worry % self.test != 0)])   

def process_file(path: pathlib.WindowsPath) -> list[Monkey]:
    monkey_list = []
    with open(path) as file:
        all_monkeys = file.read().split('\n\n')
        for monkey_details in all_monkeys:
            attributes = monkey_details.splitlines()
            items = list(map(int, re.findall(r'\d+', attributes[1])))
            op = attributes[2].split(' ', 6)[-1]
            if not op[-1].isdigit():
                operation = '* x'
            else:
                operation = attributes[2].split(' ', 6)[-1]
            test, t1, t2 = map(int, re.findall(r'\d+', ''.join(attributes[3:])))
            monkey = Monkey(operation, test, (t1,t2))
            for i in items: monkey.items.append(i)
            monkey_list.append(monkey)
    return monkey_list

if __name__ == '__main__':
    monkeys = process_file(day11_input)
    monkeys2 = copy.deepcopy(monkeys)
    # Part 1
    for _ in range(20):
        for monkey in monkeys:
            for throw in monkey.turn():
                monkey.inspect_count += 1
                monkeys[throw[1]].items.append(throw[0])        
    inspect_counts = sorted([monkey.inspect_count for monkey in monkeys])
    print(inspect_counts[-1]*inspect_counts[-2])
    # Part 2
    for _ in range(10000):
        for monkey in monkeys2:
            for throw in monkey.turn(reset = False):
                monkey.inspect_count += 1
                monkeys2[throw[1]].items.append(throw[0])
    inspect_counts2 = sorted([monkey.inspect_count for monkey in monkeys2])
    print(inspect_counts2[-1]*inspect_counts2[-2])   