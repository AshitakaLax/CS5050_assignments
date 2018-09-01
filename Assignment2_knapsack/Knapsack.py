# CLASS: CS5050
# AUTHOR: Levi Balling
# DATE: Aug 31, 2018
# ASSIGNMENT: 2

#imports needed for the assignment
import random


# This class will the package N that may vary by size
class Item:
	"""Package N that may vary by size
	"""
	Size = 0

	def Initialize(self, size):
		self.Size = 0

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

def KnapRecursive(n, l1, l2):
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
	return KnapRecursive(n, knapSackOne.Capacity - item.Size, 0) or KnapRecursive(n, knapSackOne.Capacity, 0)
# First solve this problem for One knapsack

def runTest(n, k, expect):
	print("Size of knapsack: "+ str(k))
	print("Number of objects: "+ str(len(n)))
	print([item.Size for item in n])
	result = KnapRecursive(n, k, 0)
	print("Can Fill all cells:" + str(result))
	if(result == expect):
		print("SUCCESS")
	else:
		print("FAILED")
	print("Can Fill all cells:" + str(result))
	return result

# Create Test size sets
# test data sets
n = ProblemGenerator(0, 1)
print([item.Size for item in n])
sumResult = runTest(n, 0, True)
n = ProblemGenerator(1, 2)
sumResult &= runTest(n, 0, True)
n = ProblemGenerator(50, 3)
sumResult &= runTest(n, 16, True)
n = ProblemGenerator(5, 10)
sumResult &= runTest(n, 100, True)
n = ConstantProblemGenerator(5, 1)
sumResult &= runTest(n, 5, True)
# sumResult &= runTest(4, 5, False)
# sumResult &= runTest(4, 4, True)

if(sumResult):
	print("ALL Tests PASS")
else:
	print("Some Test Failed")
