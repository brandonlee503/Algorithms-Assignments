import numpy as np

arr = np.array([[1, 2, 5],
                [8, 7, -7],
                [-3, -1, 6]])

# Main Algorithm, takes a numpy array as 
def mostValuablePath(arr):
    arrHeight = arr.shape[0] - 1
    arrWidth  = arr.shape[1] - 1

    intermediateResults = []
    finalResults = []

    # Takes a "root" and treats every possible option as a tree branch, 
    # returning the best path
    def bestPathFromRoot(x, y, curResult):
        intermediateResults.append(curResult)
        curResult = curResult + arr[y, x]
        if x > 0:
            bestPathFromRoot(x-1, y, curResult)
        if y > 0:
            bestPathFromRoot(x, y-1, curResult)
        return max(intermediateResults)

    # Iterate through bottom row
    for i in range(0, arrWidth):
        intermediateResults = []
        res = bestPathFromRoot(i, arrHeight, arr[0][0])
        finalResults.append(res)

    # Iterate through right column
    for j in range(0, arrHeight):
        intermediateResults = []
        res = bestPathFromRoot(arrWidth, j, arr[0][0])
        finalResults.append(res)

    return max(finalResults)

print(mostValuablePath(arr))
