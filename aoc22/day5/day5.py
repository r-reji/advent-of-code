import pathlib
import re
from collections import namedtuple
from copy import deepcopy

input_path = pathlib.Path(__file__).with_name('day5_input.txt')
move = namedtuple('move', ['amount', 'take_from', 'take_to'])

def process_file(path: pathlib.WindowsPath) -> tuple[list[list[str]], list[move]]:
    try:
        with open(path) as file:
            stack_data, move_data = file.read().split('\n\n')
            return stack_list(stack_data.splitlines()), move_list(move_data.splitlines())
    except FileNotFoundError:
        raise FileNotFoundError('File not found')

def stack_list(stack_data: list[str]) -> list[list[str]]:
    # count number of stacks
    stack_count = len(re.split(r'\s+',stack_data[-1].strip()))
    stacks = [[] for _ in range(stack_count)]
    # stacks stored as [[A, B, C, ..][D, E, F, ..], ... ,[Stack n]] 
    # evenly separated - check every 4th char for a crate
    stack_separation = 4
    for line in stack_data[-2::-1]:
        for i in range(stack_count):
            crate = re.match(r'[A-Z]', line[i * stack_separation + 1])
            if crate:
                stacks[i].append(crate.group(0))
    return stacks

def move_list(move_data: list[str]) -> list[move]:
    moves = []
    for line in move_data:
        matches = list(map(int, re.findall(r'\d+', line)))
        if matches:
            moves.append(move(matches[0], matches[1], matches[2]))
    return moves

def part1(stacks: list[list[str]] , moves: list[move]) -> str:
    for move in moves:
        for _ in range(move.amount):
            stacks[move.take_to - 1].append(stacks[move.take_from - 1].pop())
    return ''.join(stack[-1] for stack in stacks)

def part2(stacks: list[list[str]] , moves: list[move]) -> str:
    for move in moves:
        stacks[move.take_to - 1].extend(stacks[move.take_from - 1][-1 * move.amount:])
        del stacks[move.take_from - 1][-1 * move.amount:]
    return ''.join(stack[-1] for stack in stacks)

if __name__ == '__main__':
    def main():
        stacks, moves = process_file(input_path)
        stacks2 = deepcopy(stacks)
        print(part1(stacks, moves))
        print(part2(stacks2, moves))
    main()