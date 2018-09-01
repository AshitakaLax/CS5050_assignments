# STudy notes for knapsack problem

# returns bool, and takes (n, k)
def knap(n, k):
	if(k < 0):
		return False
	# must check if k == 0 first before n since it means n doesn't fill k
	if k == 0:
		return True
	if n == 0:
		# It would have to be the same size as k
		return False

	# this is if we put it in the knapsack or  This is if we want to discard the package
	return knap(n-1, k-s(n)) or knap(n-1, k) 

# returns the size of the specific objects
def s(n):
	return 1


# test the output of the inputs

def runTest(n, k, expect):
	print("Number of objects: "+ str(n))
	print("Size of knapsack: "+ str(k))
	result = knap(n, k)
	print("Can Fill all cells:" + str(result))
	if(result == expect):
		print("SUCCESS")
	else:
		print("FAILED")
	print("Can Fill all cells:" + str(result))
	return result
	

sumResult = runTest(5, 0, True)
sumResult &= runTest(0, 0, True)
sumResult &= runTest(5, 5, True)
sumResult &= runTest(4, 5, False)
sumResult &= runTest(4, 4, True)

if(sumResult):
	print("ALL Tests PASS")
else:
	print("Some Test Failed")