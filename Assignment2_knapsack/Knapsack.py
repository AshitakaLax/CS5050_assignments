# CLASS: CS5050
# AUTHOR: Levi Balling
# DATE: Aug 31, 2018
# ASSIGNMENT: 2

#imports needed for the assignment
import random
import time
import timeit
import copy
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
#import matplotlib.pylot as plt
# This class will the package N that may vary by size
class Item:
	"""Package N that may vary by size
	"""
	Size = 0


# This will represent a Knapsack
# with the Number of Max size it can fill
class Knapsack:
	Capacity = 0
	FillAmount = 0

	def Initialize(self, capacity):
		self.Capacity = capacity
		self.FillAmount = 0

	# Adds the item to the knapsack if there is room
	# returns true if there is room, false if there is no room
	def AddItem(self, item):
		remainingSpace = self.Capacity - self.FillAmount
		if (remainingSpace < item.Size):
			return False
		self.FillAmount += item.Size
		return True

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

def SingleKnapRecursive(n, l1, l2):
	"""Recursive algorithm that returns true if both 
	knap sacks are filled
	
	Args:
		n (List<Item>): The list of Items to add to knapsacks
		l1 (int): The Size of the knapsack
	"""
	knapSackOne = Knapsack()
	knapSackOne.Capacity = l1
	if(knapSackOne.Capacity < 0):
		return False
	if(knapSackOne.Capacity == 0):
		return True
	if(len(n) == 0):
		return False
	item = n.pop(0)
	# this is if we put it in the knapsack or  This is if we want to discard the package
	# to put it in the bag
	return SingleKnapRecursive(n, knapSackOne.Capacity - item.Size, 0) or SingleKnapRecursive(n, knapSackOne.Capacity, 0)

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
#	copiedItem = copy.deepcopy(n)
#	item = copiedItem.pop(0)
	#item = n.pop(0)
	# this is if we put it in the knapsack or  This is if we want to discard the package
	# to put it in the bag

	return (KnapNoClassRecursive(n-1, l1 - itemSize, l2) # put in KnapsackOne
	or KnapNoClassRecursive(n-1, l1, l2 - itemSize) # put in knapsackTwo
	or KnapNoClassRecursive(n-1, l1, l2)) # discard the item

def KnapRecursive(n, l1, l2):
	"""Recursive algorithm that returns true if both 
	knap sacks are filled
	
	Args:
		n (List<Item>): The list of Items to add to knapsacks
		l1 (int): The Size of the first knapsack
		l2 (int): The Size of the Second knapsack
	"""
	knapSackOne = Knapsack()
	knapSackOne.Capacity = l1
	knapSackTwo = Knapsack()
	knapSackTwo.Capacity = l2
	if(knapSackOne.Capacity < 0 or knapSackTwo.Capacity < 0):
		return False
	if(knapSackOne.Capacity == 0 and knapSackTwo.Capacity == 0):
		return True
	if(len(n) == 0):
		return False
	copiedItem = copy.deepcopy(n)
	item = copiedItem.pop(0)
	#item = n.pop(0)
	# this is if we put it in the knapsack or  This is if we want to discard the package
	# to put it in the bag

	return (KnapRecursive(copiedItem, knapSackOne.Capacity - item.Size, knapSackTwo.Capacity) # put in KnapsackOne
	or KnapRecursive(copiedItem, knapSackOne.Capacity, knapSackTwo.Capacity - item.Size) # put in knapsackTwo
	or KnapRecursive(copiedItem, knapSackOne.Capacity, knapSackTwo.Capacity)) # discard the item
# First solve this problem for One knapsack

def runTest(n, k1, k2, expect, testFunction):
	print("Size of knapsackOne: "+ str(k1))
	print("Size of knapsackTwo: "+ str(k2))
	print("Number of objects: "+ str(len(n)))
	print([item.Size for item in n])
	result = testFunction(n, k1, k2)
	print("Can Fill all cells:" + str(result))
	if(result == expect):
		print("SUCCESS")
	else:
		print("FAILED")
	return result == expect

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

def RunConstantTest(testFunction):
	"""Runs a set of simple expected result tests against a knapsack function
	
	Arguments:
		testFunction {Method(Item[], int, int)} -- Function that will run the Knapsack alorgithm and return true or false
	"""
	# Create Test size sets
	# test data sets
	# Testing a Single Knapsack
	n = ConstantProblemGenerator(0, 1)
	print([item.Size for item in n])
	sumResult = runTest(n, 0, 0, True, testFunction)
	n = ConstantProblemGenerator(1, 2)
	sumResult &= runTest(n, 0, 0, True, testFunction)
	n = ConstantProblemGenerator(10, 2)
	sumResult &= runTest(n, 16, 0, True, testFunction)
	n = ConstantProblemGenerator(20, 10)
	sumResult &= runTest(n, 100, 0, True, testFunction)
	n = ConstantProblemGenerator(5, 1)
	sumResult &= runTest(n, 5, 0, True, testFunction)

	# Testing multiple Knapsacks
	n = ConstantProblemGenerator(5, 5)
	sumResult &= runTest(n, 20, 5, True, testFunction)
	n = ConstantProblemGenerator(5, 5)
	sumResult &= runTest(n, 20, 6, False, testFunction)
	n = ConstantProblemGenerator(3, 3)
	sumResult &= runTest(n, 3, 6, True, testFunction)
	n = ConstantProblemGenerator(3, 3)
	sumResult &= runTest(n, 0, 6, True, testFunction)
	n = ConstantProblemGenerator(3, 3)
	sumResult &= runTest(n, 0, 10, False, testFunction)

	if(sumResult):
		print("ALL Tests PASS")
	else:
		print("Some Test Failed")

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

def RunEquivalantTest(testFunctionOne, TestFunctionTwo):
	"""Runs a 2 sets of knapsack function calls, and compares the results
	
	Arguments:
		testFunctionOne {Method(Item[], int, int)} -- Function that will run the Knapsack alorgithm and return true or false
		TestFunctionTwo {Method(Item[], int, int)} -- Function that will run the Knapsack alorgithm and return true or false
	"""
	# Create Test size sets
	# test data sets
	# Testing a Single Knapsack
	n = ConstantProblemGenerator(0, 1)
	m = ConstantProblemGenerator(0, 1)
	print([item.Size for item in n])
	sumResult = runTest(n, 0, 0, True, testFunctionOne) and runTest(m, 0, 0, True, TestFunctionTwo)
	n = ConstantProblemGenerator(1, 2)
	m = ConstantProblemGenerator(1, 2)
	sumResult &= runTest(n, 0, 0, True, testFunctionOne) and runTest(m, 0, 0, True, TestFunctionTwo)
	n = ConstantProblemGenerator(10, 2)
	m = ConstantProblemGenerator(10, 2)
	sumResult &= runTest(n, 16, 0, True, testFunctionOne) and runTest(m, 16, 0, True, TestFunctionTwo)
	n = ConstantProblemGenerator(20, 10)
	m = ConstantProblemGenerator(20, 10)
	sumResult &= runTest(n, 100, 0, True, testFunctionOne) and runTest(m, 100, 0, True, TestFunctionTwo)
	n = ConstantProblemGenerator(5, 1)
	m = ConstantProblemGenerator(5, 1)
	sumResult &= runTest(n, 5, 0, True, testFunctionOne) and runTest(m, 5, 0, True, TestFunctionTwo)

	# Testing multiple Knapsacks
	n = ConstantProblemGenerator(5, 5)
	m = ConstantProblemGenerator(5, 5)
	sumResult &= runTest(n, 20, 5, True, testFunctionOne) and runTest(m, 20, 5, True, TestFunctionTwo)
	n = ConstantProblemGenerator(5, 5)
	m = ConstantProblemGenerator(5, 5)
	sumResult &= runTest(n, 20, 6, False, testFunctionOne) and runTest(m, 20, 6, False, TestFunctionTwo)
	n = ConstantProblemGenerator(3, 3)
	m = ConstantProblemGenerator(3, 3)
	sumResult &= runTest(n, 3, 6, True, testFunctionOne) and runTest(m, 3, 6, True, TestFunctionTwo)
	n = ConstantProblemGenerator(3, 3)
	m = ConstantProblemGenerator(3, 3)
	sumResult &= runTest(n, 0, 6, True, testFunctionOne) and runTest(m, 0, 6, True, TestFunctionTwo)

	n = ConstantProblemGenerator(3, 3)
	m = ConstantProblemGenerator(3, 3)
	sumResult &= runTest(n, 0, 10, False, testFunctionOne) and runTest(m, 0, 10, False, TestFunctionTwo)

	if(sumResult):
		print("ALL Tests PASS")
	else:
		print("Some Test Failed")
# We are going to use the cache, this cache will be the concat of 'n'+'l1'+'l2' into a single string, with '_' symbol between them.

cache = {"":False}

def GenerateCacheKey(n, l1, l2):
	return str(n)+ "_" + str(l1) + "_" + str(l2)

def KnapMemo(n, l1, l2):
	"""Recursive algorithm that returns true if both 
	knap sacks are filled, and Uses a Cache to determine whether we need to dig deeper
	
	Args:
		n (List<Item>): The list of Items to add to knapsacks
		l1 (int): The Size of the first knapsack
		l2 (int): The Size of the Second knapsack
	"""
	cacheKey = GenerateCacheKey(len(n), l1, l2)
	# check whether the key is already in the cache, similar to a hash
	if(cacheKey in cache):
		return cache[cacheKey]

	knapSackOne = Knapsack()
	knapSackOne.Capacity = l1
	knapSackTwo = Knapsack()
	knapSackTwo.Capacity = l2
	if(knapSackOne.Capacity < 0 or knapSackTwo.Capacity < 0):
		cache[cacheKey] = False
		return False
	if(knapSackOne.Capacity == 0 and knapSackTwo.Capacity == 0):
		cache[cacheKey] = True
		return True
	if(len(n) == 0):
		cache[cacheKey] = False
		return False
		
	copiedItem = copy.deepcopy(n)
	item = copiedItem.pop(0)
	#item = n.pop(0)
	# this is if we put it in the knapsack or  This is if we want to discard the package
	# to put it in the bag

	return (KnapMemo(copiedItem, knapSackOne.Capacity - item.Size, knapSackTwo.Capacity) # put in KnapsackOne
	or KnapMemo(copiedItem, knapSackOne.Capacity, knapSackTwo.Capacity - item.Size) # put in knapsackOne
	or KnapMemo(copiedItem, knapSackOne.Capacity, knapSackTwo.Capacity)) # discard the item

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
	# cacheKey = GenerateCacheKey(n, l1, l2)
	# if(cacheKey in cache):
	# 	global CacheHitCounter
	# 	CacheHitCounter += 1
	# 	return cache[cacheKey]

	if(l1 < 0 or l2 < 0):
		return False
	if(l1 == 0 and l2 == 0):
		return True
	if(n == 0):
		return False
	itemSize = GetIndexBlockSize(n-1)	
	global recursiveCounter
	recursiveCounter += 1
#	copiedItem = copy.deepcopy(n)
#	item = copiedItem.pop(0)
	#item = n.pop(0)
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
	# return (KnapNoClassMemo(n-1, l1 - itemSize, l2) # put in KnapsackOne
	# or KnapNoClassMemo(n-1, l1, l2 - itemSize) # put in knapsackTwo
	# or KnapNoClassMemo(n-1, l1, l2)) # discard the item


#RunConstantTest(KnapRecursive)
#RunConstantTest(KnapMemo)
# verify that the function calls are equivalent
#RunEquivalantTest(KnapRecursive, KnapMemo)

#empirical  study
def RunEmpiricalStudy(testFunction):
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
			print("Start Run:" + str(j) + " of " + str(numberOfRuns))
			startTime = time.time()
			#duration = timeit.timeit('testFunction(items, L1, L2', number=numberOfRuns)
			testFunction(items, L1, L2)
			endTime = time.time()
			duration = endTime - startTime
			durationStr =  time.strftime("%H:%M:%S", time.gmtime(duration))
			print("finished Run:" + str(j) + " of " + str(numberOfRuns) + " with :" + durationStr)

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
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds, ax=ax)
