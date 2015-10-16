import numpy

print numpy.zeros((5,5))

# Currently just a pseudocode test implementation
def algorithm1(matrix):

	if len(matrix) == 0:
		return 0

	bestSolution = 0

	for i in matrix.rows:
		currentSolution = findBestSolution(matrix[i][n])
		if bestSolution < currentSolution:
			bestSolution = currentSolution

	for j in matrix.columns:
		currentSolution = findBestSolution(matrix[n][j])
		if bestSolution < currentSolution:
			bestSolution = currentSolution

	return bestSolution


def findBestSolution(matrix):
	print "Still need to implement"