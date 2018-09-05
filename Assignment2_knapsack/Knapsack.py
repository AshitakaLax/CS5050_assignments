# CLASS: CS5050
# AUTHOR: Levi Balling
# DATE: Aug 31, 2018
# ASSIGNMENT: 2

#imports needed for the assignment
import random
import copy
import datetime
import numpy as np
import matplotlib.pyplot as plt
# This class will the package N that may vary by size
class Item:
	"""Package N that may vary by size
	"""
	Size = 0

##
# @brief  Create a problem generator that
# takes n and m and returns a list of n uniformly
# @param N The number of items to generate
# @param M the random number range from 0 to M-1
def ProblemGenerator(N, M):
	problemSet = []
	# Create N Items
	# Randoms assign sizes to the Items from 0 to M-1
	for count in range(N):
		item = Item()
		item.Size = random.randint(0, M - 1)
		problemSet.append(item)
	return problemSet

class ProblemController:
	Items = []
	def SetProblemItems(self, items):
		self.Items = items
	

problemCntrl = ProblemController()

def GetIndexBlockSize(index):
	return problemCntrl.Items[index].Size

def ConstantProblemGenerator(N, C):
	"""Generates a List of N Items that are size C
	
	Arguments:
		N {int} -- The Number of cells to generate
		C {int} -- The size of each item
	
	Returns:
		list -- The list of N items with size C in each
	"""
	problemSet = []
	# Create N Items
	# Randoms assign sizes to the Items from 0 to M-1
	for count in range(N):
		item = Item()
		item.Size = C
		problemSet.append(item)
	return problemSet

recursiveCounter = 0
def KnapNoClassRecursive(n, l1, l2):
	"""Recursive algorithm that returns true if both 
	knap sacks are filled
	
	Args:
		n (List<Item>): The list of Items to add to knapsacks
		l1 (int): The Size of the first knapsack
		l2 (int): The Size of the Second knapsack
	"""
	if(l1 < 0 or l2 < 0):
		return False
	if(l1 == 0 and l2 == 0):
		return True
	if(n == 0):
		return False
	itemSize = GetIndexBlockSize(n-1)	
	global recursiveCounter
	recursiveCounter += 1
	# this is if we put it in the knapsack or  This is if we want to discard the package
	# to put it in the bag

	return (KnapNoClassRecursive(n-1, l1 - itemSize, l2) # put in KnapsackOne
	or KnapNoClassRecursive(n-1, l1, l2 - itemSize) # put in knapsackTwo
	or KnapNoClassRecursive(n-1, l1, l2)) # discard the item

# First solve this problem for One knapsack

def runNoClassTest(n, k1, k2, expect, testFunction):
	print("Size of knapsackOne: "+ str(k1))
	print("Size of knapsackTwo: "+ str(k2))
	print("Number of objects: "+ str(n))
	result = testFunction(n, k1, k2)
	print("Can Fill all cells:" + str(result))
	if(result == expect):
		print("SUCCESS")
	else:
		print("FAILED")
	return result == expect

def RunConstantNoClassTest(testFunction):
	"""Runs a set of simple expected result tests against a knapsack function
	
	Arguments:
		testFunction {Method(int, int, int)} -- Function that will run the Knapsack alorgithm and return true or false
	"""
	# Create Test size sets
	# test data sets
	# Testing a Single Knapsack
	n = ConstantProblemGenerator(0, 1)
	problemCntrl.SetProblemItems(n)

	sumResult = runNoClassTest(len(n), 0, 0, True, testFunction)
	n = ConstantProblemGenerator(1, 2)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 0, 0, True, testFunction)
	n = ConstantProblemGenerator(10, 2)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 16, 0, True, testFunction)
	n = ConstantProblemGenerator(20, 10)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 100, 0, True, testFunction)
	n = ConstantProblemGenerator(5, 1)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 5, 0, True, testFunction)

	# Testing multiple Knapsacks
	n = ConstantProblemGenerator(5, 5)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 20, 5, True, testFunction)
	n = ConstantProblemGenerator(5, 5)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 20, 6, False, testFunction)
	n = ConstantProblemGenerator(3, 3)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 3, 6, True, testFunction)
	n = ConstantProblemGenerator(3, 3)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 0, 6, True, testFunction)
	n = ConstantProblemGenerator(3, 3)
	problemCntrl.SetProblemItems(n)
	sumResult &= runNoClassTest(len(n), 0, 10, False, testFunction)

	if(sumResult):
		print("ALL Tests PASS")
	else:
		print("Some Test Failed")

# We are going to use the cache, this cache will be the concat of 'n'+'l1'+'l2' into a single string, with '_' symbol between them.

cache = {"":False}

def GenerateCacheKey(n, l1, l2):
	return str(n)+ "_" + str(l1) + "_" + str(l2)

CacheHitCounter = 0
def KnapNoClassMemo(n, l1, l2):
	"""Recursive algorithm that returns true if both 
	knap sacks are filled
	
	Args:
		n (List<Item>): The list of Items to add to knapsacks
		l1 (int): The Size of the first knapsack
		l2 (int): The Size of the Second knapsack
	"""
	global cache

	if(l1 < 0 or l2 < 0):
		return False
	if(l1 == 0 and l2 == 0):
		return True
	if(n == 0):
		return False
	itemSize = GetIndexBlockSize(n-1)	
	global recursiveCounter
	recursiveCounter += 1
	# this is if we put it in the knapsack or  This is if we want to discard the package
	# to put it in the bag

	hitOneCache = False
	global CacheHitCounter
	cacheKeyOne = GenerateCacheKey(n-1, l1 - itemSize, l2)
	if(cacheKeyOne in cache):
		CacheHitCounter += 1
		hitOneCache = True
		if(cache[cacheKeyOne]):
			return True
	#cache result was false, need to call the next one

	hitTwoCache = False
	cacheKeyTwo = GenerateCacheKey(n-1, l1, l2 - itemSize)
	if(cacheKeyTwo in cache):
		CacheHitCounter += 1
		hitTwoCache = True
		if(cache[cacheKeyTwo]):
			return True
	#Cache result was false
	hitThreeCache = False
	cacheKeyThree = GenerateCacheKey(n-1, l1, l2)
	if(cacheKeyThree in cache):
		CacheHitCounter += 1
		hitThreeCache = True
		if(cache[cacheKeyThree]):
			return True

	result = False
	if(not(hitOneCache)):
		result = KnapNoClassMemo(n-1, l1 - itemSize, l2) # put in KnapsackOne
		cache[cacheKeyOne] = result

	if(not(result) and not(hitTwoCache)):
		result = KnapNoClassMemo(n-1, l1, l2 - itemSize)
		cache[cacheKeyThree] = result

	if(not(result) and not(hitThreeCache)):
		result = KnapNoClassMemo(n-1, l1, l2)
		cache[cacheKeyThree] = result
	
	return result

#empirical  study
def RunEmpiricalNoClassStudy(testFunction):
	L1 = 100
	L2 = 100
	min = 10
	max = 200
	incrementAmount = 10
	itemSizeM = 50
	numberOfRuns = 10

	# iterate from min to max
	for i in range(min, max, incrementAmount):
		# run each test 10 times with i
		# Generate the data set to use in the test
		print("TESTING " + str(i) + " OBJECTS")
		for j in range(numberOfRuns):
			items = ProblemGenerator(i, itemSizeM)
			problemCntrl.SetProblemItems(items)
			print("Start Run:" + str(j) + " of " + str(numberOfRuns))
			global recursiveCounter
			recursiveCounter = 0
			dateStartTime = datetime.datetime.now()
			#startTime = time.time()
			testFunction(i, L1, L2)
			dateEndTime = datetime.datetime.now()
			#endTime = time.time()
			duration = dateEndTime - dateStartTime
			
			durationStr =  str(duration)#time.strftime("%H:%M:%S", time.gmtime(duration))
			print("finished Run:" + str(j) + " of " + str(numberOfRuns) + " with :" + durationStr)
			print("Number of Calls:" + str(recursiveCounter))

def RunEmpiricalCompareStudy(testFunction, testMemoFunction):
	L1 = 100
	L2 = 100
	min = 10
	max = 200
	incrementAmount = 10
	itemSizeM = 50
	numberOfRuns = 10

	# iterate from min to max
	for i in range(min, max, incrementAmount):
		# run each test 10 times with i
		# Generate the data set to use in the test
		print("TESTING " + str(i) + " OBJECTS")
		for j in range(numberOfRuns):
			items = ProblemGenerator(i, itemSizeM)
			problemCntrl.SetProblemItems(items)
			#print("Start Run:" + str(j) + " of " + str(numberOfRuns))
			global recursiveCounter
			recursiveCounter = 0
			dateStartTime = datetime.datetime.now()
			recursiveResult = testFunction(i, L1, L2)
			dateEndTime = datetime.datetime.now()
			duration = dateEndTime - dateStartTime
			durationStr =  str(duration)#time.strftime("%H:%M:%S", time.gmtime(duration))
			#print("finished Run:" + str(j) + " of " + str(numberOfRuns) + " with :" + durationStr)
			#print("Number of Calls:" + str(recursiveCounter))
			nonCacheCounter = recursiveCounter

			# Testing the Memo version
			recursiveCounter = 0
			global CacheHitCounter
			CacheHitCounter = 0
			global cache
			cache = {"": False}
			problemCntrl.SetProblemItems(items)
			dateStartTime = datetime.datetime.now()
			cacheResult = testMemoFunction(i, L1, L2)
			dateEndTime = datetime.datetime.now()
			durationMemo = dateEndTime - dateStartTime
			durationMemoStr =  str(durationMemo)
			#print("finished Run:" + str(j) + " of " + str(numberOfRuns) + " with :" + durationStr)
			#print("Number of Calls:" + str(recursiveCounter))
			print("Recursive:" + str(durationStr) + " recursiveCounter:" + str(nonCacheCounter) + " RecursiveResult:" + str(recursiveResult) + " Cache:" + str(durationMemoStr) + " CacheCounter:" + str(recursiveCounter) + " CacheResult:" + str(cacheResult) + "CacheHitCounter:" + str(CacheHitCounter))


def RunEmpiricalStudyForGraphData(testFunction):
	L1 = 100
	L2 = 100
	min = 10
	max = 200
	incrementAmount = 10
	itemSizeM = 50
	numberOfRuns = 10


	# iterate from min to max
	for i in range(min, max, incrementAmount):
		# run each test 10 times with i
		# Generate the data set to use in the test
		print("TESTING " + str(i) + " OBJECTS")
		for j in range(numberOfRuns):
			items = ProblemGenerator(i, itemSizeM)
			problemCntrl.SetProblemItems(items)
			#print("Start Run:" + str(j) + " of " + str(numberOfRuns))
			global recursiveCounter
			recursiveCounter = 0
			dateStartTime = datetime.datetime.now()
			recursiveResult = testFunction(i, L1, L2)
			dateEndTime = datetime.datetime.now()
			duration = dateEndTime - dateStartTime
			durationStr =  str(duration)#time.strftime("%H:%M:%S", time.gmtime(duration))
			#print("finished Run:" + str(j) + " of " + str(numberOfRuns) + " with :" + durationStr)
			#print("Number of Calls:" + str(recursiveCounter))
			nonCacheCounter = recursiveCounter

			# Testing the Memo version
			recursiveCounter = 0
			global CacheHitCounter
			CacheHitCounter = 0
			global cache
			cache = {"": False}
			problemCntrl.SetProblemItems(items)
			dateStartTime = datetime.datetime.now()
			cacheResult = testMemoFunction(i, L1, L2)
			dateEndTime = datetime.datetime.now()
			durationMemo = dateEndTime - dateStartTime
			durationMemoStr =  str(durationMemo)
			#print("finished Run:" + str(j) + " of " + str(numberOfRuns) + " with :" + durationStr)
			#print("Number of Calls:" + str(recursiveCounter))
			print("Recursive:" + str(durationStr) + " recursiveCounter:" + str(nonCacheCounter) + " RecursiveResult:" + str(recursiveResult) + " Cache:" + str(durationMemoStr) + " CacheCounter:" + str(recursiveCounter) + " CacheResult:" + str(cacheResult) + "CacheHitCounter:" + str(CacheHitCounter))



# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

#RunEmpiricalStudy(KnapMemo)
#RunEmpiricalCompareStudy(KnapNoClassRecursive, KnapNoClassMemo)
#RunConstantNoClassTest(KnapNoClassRecursive)

# Creating the graphing data

# Load the example iris dataset
diamonds = sns.load_dataset("diamonds")

# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
tips = sns.load_dataset("tips")

data = np.array([['', 'Col1', "Col2"],
				['Row1', 1, 2],
				['Row2', 3, 4]])
				
xData = [1,2,3]
yData = [3,2,1]

#dataFrame = pd.DataFrame(data=data[1:,1:],
#                  index=data[1:,0],
#                  columns=data[0,1:])
#print(dataFrame)
plt.scatter(xData, yData)
plt.show()
RunConstantNoClassTest(KnapNoClassRecursive)