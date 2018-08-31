# CS5050 Advanced Algorithms
# Assignment 1
# Levi Balling
# Aug 28, 2018

# Approach One using just recursion
def Win(A, B, C):
	remainingStones = A + B + C
	if remainingStones == 0:
		return True
	if remainingStones == 1:
		return False
	# Recursive call toward various piles
	# check if the pile is empty before 
	# solve for all possible A by taking all of the A
	return (WinSinglePile(A) or WinSinglePile(B) or WinSinglePile(C))

def WinSinglePile(n):
	if(n == 0):
		return True
	if(n == 1):
		return False
		
	winResult = True
	for i in range(0, n):
		winResult &= WinSinglePile(i)
	return not(winResult)

#print("2,1,0 " + str(Win(2, 1, 0)))
#print("0,1,0 " + str(Win(0, 1, 0)))
#print("0,0,0 " + str(Win(0, 2, 0)))
#print("1,1,0 " + str(Win(1, 1, 0)))
print("0,0,0 Expect(TRUE), Actual(" + str(Win(0, 0, 0)) + ")")
print("1,0,0 Expect(FALSE), Actual(" + str(Win(1, 0, 0)) + ")")
print("1,1,0 Expect(TRUE), Actual(" + str(Win(1, 1, 0)) + ")")
print("1,1,1 Expect(FALSE), Actual(" + str(Win(1, 1, 1)) + ")")
print("2,1,1 Expect(TRUE), Actual(" + str(Win(2, 1, 1)) + ")")
print("5,1,1 Expect(TRUE), Actual(" + str(Win(5, 1, 1)) + ")")

#for i in range(0, 8):
	#print(i)
	#print("XOR")
	#print(str(i) + " " + str(WinXor(i, i, i)))

	#print(str(i) + " " + str(Win(i, i, i)))

# Simple Problem
# A XOR B XOR C
# if(win(a-1) ^ win(B-1) ^ win(C-1))