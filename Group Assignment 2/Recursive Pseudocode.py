import numpy as np

arr = np.array([[1, 2, 5],
                [8, 7, -7],
                [-3, -1, 6]])

# Main Algorithm, takes a numpy array
def mostValuablePath(arr):
    arrHeight = arr.shape[0] - 1
    arrWidth  = arr.shape[1] - 1

    intermediateResults = []
    finalResults = []

    # Takes a "root" and treats every possible option as a tree branch, 
    # returning the best path
    def bestPathFromRoot(x, y, curResult):
        intermediateResults.append(curResult)
        curResult = curResult + arr[y, x] # [row, col]
        if x > 0:
            bestPathFromRoot(x-1, y, curResult)
        if y > 0:
            bestPathFromRoot(x, y-1, curResult)
        return max(intermediateResults)

    # Iterate through bottom row
    for i = 0 ... arrWidth:
        intermediateResults = []
        res = bestPathFromRoot(i, arrHeight, 0)
        finalResults.append(res)

    # Iterate through right column
    for j = 0 ... arrHeight:
        intermediateResults = []
        res = bestPathFromRoot(arrWidth, j, 0)
        finalResults.append(res)

    return max(finalResults)

print(mostValuablePath(arr))
