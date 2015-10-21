import numpy as np
import sys

try:
    filename = sys.argv[1]
    inFile = open(filename, "r")
    outFile = open("output.txt", "w+")
except:
    print("Error: Must provide valid filename as a command line argument")
    raise

try:
    inArr = [int(x) for x in inFile.read().split()]
    rows = inArr[0]
    cols = inArr[1]
    arr = inArr[2:]
    arr = np.reshape(arr, (-1, cols))
except:
    print("Error: Invalid array")
    raise

print(arr)

# Main algorithm, takes a 2D numpy array as an argument
height = arr.shape[0] - 1
width = arr.shape[1] - 1

best_path_values = [[0 for x in range(width + 1)] for y in range(height + 1)]
best_path_values = np.array(best_path_values)

best_path_indices = [[[None] for x in range(width+1)] for y in range(height+1)]

# Fill initial best_path_values with right and bottom arr values
for i in range(0, height):
    best_path_values[i][width] = (arr[i][width])
    best_path_indices[i][width][0] = (width, i)
for j in range(0, width):
    best_path_values[height][j] = (arr[height][j])
    best_path_indices[height][j][0] = (j, height)
best_path_values[height][width] = arr[height][width]


def choose_best_path_from_index(x, y):
    below_x = x
    below_y = y + 1
    right_x = x + 1
    right_y = y

    below_value = best_path_values[below_y][below_x] + arr[y][x]
    right_value = best_path_values[right_y][right_x] + arr[y][x]

    if below_value >= right_value:
        best_value = below_value
        best_path_indices[y][x] = best_path_indices[below_y][below_x][:]
        best_path_indices[y][x].append((x, y))
    elif below_value < right_value:
        best_value = right_value
        best_path_indices[y][x] = best_path_indices[right_y][right_x][:]
        best_path_indices[y][x].append((x, y))

    return best_value


def best_path(x, y):
    for i in range(x, -1, -1):
        best_path_values[y][i] = choose_best_path_from_index(i, y)
    for j in range(y, -1, -1):
        best_path_values[j][x] = choose_best_path_from_index(x, j)
    return

for k in range(width - 1, -1, -1):
    best_path(k, k)

max_value = np.amax(best_path_values)
max_index = np.where(best_path_values == max_value)
best_path = best_path_indices[max_index[1][0]][max_index[0][0]]

outFile.write(str(max_value) + "\n")
outFile.write(str(len(best_path)) + "\n")

print(max_value)
print(len(best_path))

for i in reversed(best_path):
    print(i)
    outFile.write("{} {} \n".format(i[0], i[1]))
