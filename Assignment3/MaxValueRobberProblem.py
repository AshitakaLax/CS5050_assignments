# CLASS: CS5050
# AUTHOR: Levi Balling
# DATE: Sep 11, 2018
# ASSIGNMENT: 3-1 Maximum Value robber problem

# Problem statement: Given n items each with a weight[i] and a positive value v[i], a bag
# to store the objects and maximum weight limit L (the heaviest the robber can carry), 
# find the subset of objects that is less than or equal to L that is worth the maximum cumulative value.


# The money object that has weight and value
class MoneyObject:
	Weight = 0
	Value = 0

def DefineMoney(numOfItems):
	moneyList = []
	for i in range(numOfItems):
		money = MoneyObject() 
		money.Value = i
		money.Weight = i
		moneyList.append(money)
	return moneyList

moneyTempList = DefineMoney(3)

#Derive Recursive Function:
#First simplify the problem to determine the maximum value that can be obtained, not the actual objects.
money = []
moneyObj = MoneyObject() 
moneyObj.Value = 5
moneyObj.Weight = 1
money.append(moneyObj)
moneyObj = MoneyObject() 
moneyObj.Value = 10
moneyObj.Weight = 3
money.append(moneyObj)
moneyObj = MoneyObject() 
moneyObj.Value = 10
moneyObj.Weight = 2
money.append(moneyObj)
moneyObj = MoneyObject() 
moneyObj.Value = 3
moneyObj.Weight = 4
money.append(moneyObj)
#psuedo code
# the size of the bag
# As each item is placed into the bag, we get closer to the max
# but the other facet to this problem is that we want the max value available

recursiveLevel = 0

# returns the max value as an int
def GetMaxValue(n, L, label):
	global recursiveLevel
	recursiveLevel += 1
	if(L == 0 or n == 0):
		return 0
	if(L < 0 or n < 0):
		return -999999
	print("typeOfCall" + str(label) + "recursionLevel:" + str(recursiveLevel) + " n:" + str(n) + " L:" + str(L) + " Value[n]=" + str(money[n-1].Value) + " weight[n]=" + str(money[n-1].Weight))

	# iterate over all possible options
	val = 0
	for i in range(1, n + 1):
		# reduce by size and compare by value
		temp1=GetMaxValue(n-1, L, "Drop")
		temp2=GetMaxValue(n-1, L-money[n-i].Weight, "Add") + money[n-i].Value
		print("Label:"+ str(label) + "n: " + str(n) + " i=" + str(i))
		print("Label:"+ str(label) + "GetValueDropObject:" + str(temp1) + "GetValueAddObject:" + str(temp2) + " Val:" + str(val))					
		val= max(temp1, temp2, val)

	return val


# returns the max value as an int
def GetValue(n, L, label, level = 0):
	global recursiveLevel
	recursiveLevel += 1
	if(L == 0 or n == 0):
		return 0
	if(L < 0 or n < 0):
		return -999999
	tabStr = ""
	for j in range(0, level):
		tabStr += "----"
	print(tabStr + "level:" + str(level)+ " typeOfCall" + str(label) + " recursionLevel:" + str(recursiveLevel) + " n:" + str(n) + " L:" + str(L) + " Value[n]=" + str(money[n-1].Value) + " weight[n]=" + str(money[n-1].Weight))

	# iterate over all possible options
	val = 0
	# reduce by size and compare by value
	temp1=GetValue(n-1, L, "Drop", level + 1)
	temp2=GetValue(n-1, L-money[n-1].Weight, "Add", level + 1) + money[n-1].Value
	#print("Label:"+ str(label) + " n: " + str(n) )
	#print("Label:"+ str(label) + " GetValueDropObject:" + str(temp1) + " GetValueAddObject:" + str(temp2) + " Val:" + str(val))					
	val= max(temp1, temp2, val)

	return val


#print("result:" + str(GetMaxValue(3, 5)))
#print("result:" + str(GetMaxValue(4, 5, "Start")))
print("result:" + str(GetValue(4, 5, "Start")))

# Weight vs Value

# Max Value


# Questions about assignment
# how can a larger problem be broken down into a smaller problem

# The real question is how to make the problem smaller
# the last part of each problem is the Traceback
# the robber problem, then find the list of objects in the
# what is the maxium value I can obtain
