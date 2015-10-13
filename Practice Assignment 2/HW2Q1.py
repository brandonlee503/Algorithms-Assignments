def algorithm1(n, k, current):
	print "start"
	if len(n) <= 0:
		return False
	if k in n:
		return True

	tempMax = max(n)
	n.remove(tempMax)

	if current + tempMax <= k:
		current += tempMax
	if current == k:
		return True
		
	algorithm1(n, k, current)

algorithm1([1,1,3,2,3,5], 10, 0)
algorithm1([1,4,5], 5, 0)