from random import randint
import time

def fillArray(arr, size):
	for i in range(size):
		arr.append(randint(-10, 10))

def algorithm1(arr):
	maxSum = 0

	# Try all subarray lengths
	for j in range(0, len(arr)):

		# Try all subarray locations
		for i in range(0, len(arr) - j):
			currentSum = 0

			# Sum subarray
			for element in arr[i : i + j]:
				currentSum += element
			if currentSum > maxSum:
				maxSum = currentSum
	return maxSum


def algorithm2(arr):
	maxSum = 0
	
	# Try all subarray lengths
	for j in range(0, len(arr)):
		
		# Compute first subarray sum
		currentSum = 0
		for element in arr[0 : j]:
			currentSum += element
		
		# Try all subarray locations
		for i in range(0, len(arr) - j):
			if i > 0:
				currentSum = currentSum - arr[i - 1] + arr[i + j - 1]
			if currentSum > maxSum:
				maxSum = currentSum
	return maxSum


def algorithm3(arr):
    maxSum = 0
    currentSum = 0

    for i in arr:

        # If the current index and subarray are positive, keep adding to the subarray
        if currentSum + i > 0:
            currentSum = currentSum + i
        else:
            currentSum = 0
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum

arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []
arr8 = []
arr9 = []

arr10 = []
arr11 = []
arr12 = []
arr13 = []
arr14 = []
arr15 = []
arr16 = []
arr17 = []
arr18 = []


fillArray(arr1, 100)
fillArray(arr2, 200)
fillArray(arr3, 300)
fillArray(arr4, 400)
fillArray(arr5, 500)
fillArray(arr6, 600)
fillArray(arr7, 700)
fillArray(arr8, 800)
fillArray(arr9, 900)

fillArray(arr10, 1000)
fillArray(arr11, 2000)
fillArray(arr12, 3000)
fillArray(arr13, 4000)
fillArray(arr14, 5000)
fillArray(arr15, 6000)
fillArray(arr16, 7000)
fillArray(arr17, 8000)
fillArray(arr18, 9000)

elapsed = 0

for i in range(10):	
	start = time.time()
	print algorithm2(arr18)
	end = time.time()
	elapsed += end - start

print elapsed/10
