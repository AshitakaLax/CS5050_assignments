# Single Knapsack.py
# this is just the implementation of the single knapsack in python

import random
import copy
import datetime

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


cache = {"":False}
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