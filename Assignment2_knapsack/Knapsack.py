# CLASS: CS5050
# AUTHOR: Levi Balling
# DATE: Aug 31, 2018
# ASSIGNMENT: 2

#imports needed for the assignment
import random

# This class will the package N that may vary by size
class Item:
	Size = 0
	def Initialize(self, size):
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
		if(remainingSpace < item.Size):
			return False
		self.FillAmount += item.Size
		return True

# Create a problem generator that 
# takes n and m and returns a list of n uniformly 
# random integers in the range 0 to m-1 
def ProblemGenerator(N, M):
	problemSet = []
	# Create N Items
	# Randoms assign sizes to the Items from 0 to M-1
	for count in range(N):
		item = Item()
		item.Size = random.randint(0, M-1)
		problemSet.append(item)
	return problemSet

# Create Test size sets

# print problem set
listSet = ProblemGenerator(10, 10)

print([item.Size for item in listSet])

# Testing out the Knapsack class
sack = Knapsack()

print(sack.Capacity)
print(sack.FillAmount)
sack.Initialize(10)
testItem = Item()
testItem.Size = 5
print("Result of add:" + str(sack.AddItem(testItem)))
print(sack.Capacity)
print(sack.FillAmount)

testItem.Size = 5
print("Result of add:" + str(sack.AddItem(testItem)))
print(sack.Capacity)
print(sack.FillAmount)
print("Result of add:" + str(sack.AddItem(testItem)))
print(sack.Capacity)
print(sack.FillAmount)


