def algorithm3(arr):
	maxLength = 0
	if len(arr) <= 0:
		return 0
	if len(arr) == 1:
		return 1
	for i in arr:
		print "i is: " + str(i)
		temp = [arr[i-1]]
		for j in range(len(arr) - i):

			spliceArrayJ = arr[j+1:]
			print "reversed array: "
			reversedArray = spliceArrayJ[::-1]
			print reversedArray

			print "This is temp: " + str(temp)
			print "This is tempSize: " + str(len(temp))

			print "if temp in reversedArray is: " + str(isSublist(temp, reversedArray))
			print "if len(temp) > maxLength is: " + str(len(temp) > maxLength)

			if isSublist(temp, reversedArray) and len(temp) > maxLength: #temp in reversedArray
				maxLength = len(temp)
				#maxLength = reversedArray.count(temp)
				print "DAAAAA MATX LENGTH: " + str(maxLength)
			temp.append(arr[i + j])
		print "maxLength is: " + str(maxLength)
	return maxLength

def isSublist(a, b):
    if a == []: return True
    if b == []: return False
    return b[:len(a)] == a or isSublist(a, b[1:])

#algorithm3([1,2,3,4,5,6,7,8,9])
#algorithm3([1,2,1,4,5,1,2,1])
#algorithm3([1,3,4,1,1])

#print isSublist([1,2],[1,2,3])