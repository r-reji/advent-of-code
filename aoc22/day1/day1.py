import details

def read_file(file_path):
    '''
    lazy Generator
    '''
    while True:
        try:
            data = file_path.readline()
            if not data:
                break
            yield data
        except:
            raise FileNotFoundError("File not found")

calories = []

with open(details.calorie_file_path) as file:
    for line in read_file(file):
        if line == '\n':
            calories.append(0)
        else:
            calories.append(int(line))

# PART 1

def max_elf(calories):
    '''
    sub-array w/ max sum and w/o zero elements
    '''    
    max_cal, curr_sum = 0, 0
    for l in range(len(calories)):
        if calories[l] == 0:
            max_cal = max(max_cal, curr_sum)
            curr_sum = 0
        else:
            curr_sum += calories[l]  
    return max(max_cal, curr_sum)

# PART 2

def max_3elf(calories):
    curr_sum = 0
    elf_sum = []
    for r in range(len(calories)):
        if calories[r] == 0:
            elf_sum.append(curr_sum)
            curr_sum = 0
        else:
            curr_sum += calories[r]
    return sum(i for i in sorted(elf_sum)[-3:])

def main():
    print(max_elf(calories))
    print(max_3elf(calories))

if __name__ == '__main__':
    main()