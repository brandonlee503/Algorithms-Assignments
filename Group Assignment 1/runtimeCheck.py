from random import randint
import time

def fillArray(arr, size):
	for i in range(size):
		arr.append(randint(-10, 10))
	#print arr

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

arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []
arr8 = []
arr9 = []
elapsed = 0

fillArray(arr1, 100)
fillArray(arr2, 200)
fillArray(arr3, 300)
fillArray(arr4, 400)
fillArray(arr5, 500)
fillArray(arr6, 600)
fillArray(arr7, 700)
fillArray(arr8, 800)
fillArray(arr9, 900)

for i in range(10):	
	start = time.time()
	print algorithm1(arr9)
	end = time.time()
	elapsed += end - start
print elapsed/10
