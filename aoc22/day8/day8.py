import pathlib
import numpy as np

day8_input = pathlib.Path(__file__).with_name('day8_input.txt')

def read_file(path: pathlib.WindowsPath):
    '''
    Convert input file to 2D numpy array
    '''
    with open(path) as file:
        while True:
            try:
                data = file.read().splitlines()
                return np.array([[int(x) for x in x.strip()] for x in data])
            except FileNotFoundError:
                raise FileNotFoundError('File not found')

def visibility(arr, scenic = False):
    '''
    Tree can be visible from one of 4 directions which satisfy the following conditions:
    '''
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # compare against all trees in a given direction : array[bool] - reversed lists are for part 2
            up = arr[i,j] > arr[:i, j][::-1] 
            down = arr[i,j] > arr[i+1:, j] 
            left = arr[i,j] > arr[i, :j][::-1]
            right = arr[i,j] > arr[i, j+1: ]
            res = (up, down, left, right)
            if not scenic:
                # if any such array is all True then tree is visible
                yield int(any(map(all, res)))
            else:
                # product of number of visible trees in each direction
                scores = []
                for dir in res:
                    if all(dir):
                        scores.append(sum(dir))
                    else:
                        scores.append(np.argmin(dir) + 1)
                yield np.product(scores)

if __name__ == '__main__':
    def main():
        tree_grid = read_file(day8_input)
        # part 1
        vis_ctr = 0
        for vis in visibility(tree_grid):
            vis_ctr += vis
        print(vis_ctr)
        # part 2
        print(max(score for score in visibility(tree_grid, scenic = True)))
    main()