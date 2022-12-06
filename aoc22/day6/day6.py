import pathlib

day6_input = pathlib.Path(__file__).with_name('day6_input.txt')

def read_file(path: pathlib.WindowsPath) -> list[str]:
    try:
        with open(path) as file:
            return file.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError('File not found')

def unique_substring_of_length(path: pathlib.WindowsPath, length: int) -> int:
    string = ''.join(read_file(path))
    # Standard 2-pointer solution
    l = 0
    index = -1
    chars = set()
    for r in range(len(string)):
        while string[r] in chars:
            chars.remove(string[l])
            l += 1
        chars.add(string[r])
        if r - l + 1 == length:
            index = r + 1
            break
    return index

if __name__ == '__main__':
    def main():
        print(unique_substring_of_length(day6_input, 4))
        print(unique_substring_of_length(day6_input, 14))
    main()