import numpy as np
import sys

# Initialize read/write files
try:
    filename = sys.argv[1]
    inFile = open(filename, "r")
    outFile = open("best-output.txt", "w+")
except:
    print("Error: Must provide valid filename as a command line argument")
    raise

try:
    inArr = [int(x) for x in inFile.read().split()]
    numRows = inArr[0]
    numCols = inArr[1]
    arr = inArr[2:]
    arr = np.reshape(arr, (-1, numCols))
except:
    print("Error: Invalid array")
    raise

print(arr)

# Main algorithm, takes a 2D numpy array as an argument
def mostValuablePath(arr):
    arrHeight = arr.shape[0] - 1
    arrWidth  = arr.shape[1] - 1

    intermediateResults = []
    intermediateResultsPath = []
    finalResults = []


    # Takes a "root" and treats every possible option as a tree branch, 
    # returning the best path
    def bestPathFromRoot(x, y, curResult):
        intermediateResults.append(curResult)
        curResult = curResult + arr[y, x]
        intermediateResultsPath.append([curResult, [y, x]])
        if x > 0:
        	print str(y) + "," + str(x) + ": " + str(arr[y,x])
        	bestPathFromRoot(x-1, y, curResult)
        if y > 0:
            bestPathFromRoot(x, y-1, curResult)
        #print intermediateResults
        #print max(intermediateResults)
        print intermediateResultsPath
        return max(intermediateResults)

    # Iterate through bottom row
    for i in range(0, arrWidth):
        intermediateResults = []
        res = bestPathFromRoot(i, arrHeight, 0)
        finalResults.append(res)

    # Iterate through right column
    for j in range(0, arrHeight):
        intermediateResults = []
        res = bestPathFromRoot(arrWidth, j, 0)
        finalResults.append(res)

    #print intermediateResultsPath[]

    print intermediateResults
    outFile.write(str(max(finalResults)))
    return max(finalResults)

print(mostValuablePath(arr))