import numpy as np

arr = np.array([[1, 2, 5],
                [8, 7, -7],
                [-3, -1, 6]])

arrHeight = arr.shape[0] - 1
arrWidth  = arr.shape[1] - 1

results = []

# Takes a "root" and treats every possible option as a tree branch, 
# returning the best path
def bestPathFromRoot(x, y, curResult):
    results.append(curResult)
    curResult = curResult + arr[y, x]
    if x > 0:
        bestPathFromRoot(x-1, y, curResult)
    if y > 0:
        bestPathFromRoot(x, y-1, curResult)
    return max(results)

finalResults = []
# Iterate through bottom row
for i in range(0, arrWidth):
    results = []
    res = bestPathFromRoot(i, arrHeight, arr[0][0])
    finalResults.append(res)

# Iterate through right column
for j in range(0, arrHeight):
    results = []
    res = bestPathFromRoot(arrWidth, j, arr[0][0])
    finalResults.append(res)

print(max(finalResults))


'''
import numpy

print numpy.zeros((5,5))

foo = numpy.matrix([[11,12,13],
                    [21,22,23],
                    [31,32,33]])

print foo[0,10]
rows = foo.shape[0]
columns = foo.shape[1]

print rows
print columns

# Note that matrix is implemented with numpy
def algorithm1(matrix):

	rows = matrix.shape[0] - 1
	columns = matrix.shape[1] - 1

	if matrix.size == 0:
		return 0

	bestSolution = 0

	for i in rows:
		currentSolution = findBestSolution(matrix, (i,n), bestSolution)
		if bestSolution < currentSolution:
			bestSolution = currentSolution

	for j in columns:
		currentSolution = findBestSolution(matrix, (n,j), bestSolution)
		if bestSolution < currentSolution:
			bestSolution = currentSolution

	return bestSolution


def findBestSolution(matrix, startPoint, bestSolution):
	print "Still need to implement"
	
	currentSolution = 0

	matrix[startPoint[0], startPoint[1]]



	if i - 1 and j - 1 == null:
		return bestSolution
	if currentSolution > bestSolution:
		bestSolution = currentSolution

	return currentSolution
'''
