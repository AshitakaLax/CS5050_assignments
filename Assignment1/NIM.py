# CS5050 Advanced Algorithms
# Assignment 1
# Levi Balling
# Aug 28, 2018

# This will recursive decrement the values to determine whether it
# I know there is a cleaner solution, and look forward to seeing what it is
def Win(A, B, C):
	# base case if any pile has more than 1 than the answer is true
	if(A == 2 or B == 2 or C == 2):
		return True

	# Handle a few cases to make sure that the value is correct
	remainingStones = A + B + C
	if remainingStones == 0:
		return True
	if remainingStones == 1:
		return False
	if(A == 1 and B == 1 and C == 1):
		return False

	# Recursively determine whether there is a win
	if A > 1:
		return (Win(A-1, B, C))
	if B > 1:
		return (Win(A, B-1, C))
	if C > 1:
		return (Win(A, B, C-1))

	return True

# here is my Non recursive solution that is performant	
def NonRecursiveOptimalWin(A, B, C):
	a=not(A != 1)
	b=not(B != 1)
	c=not(C != 1)
	return not(a ^ b ^ c)

# tests to validate that the code is working properly
print("0,0,0 Expect(TRUE), Actual(" + str(Win(0, 0, 0)) + ")")
print("1,0,0 Expect(FALSE), Actual(" + str(Win(1, 0, 0)) + ")")
print("0,1,0 Expect(FALSE), Actual(" + str(Win(0, 1, 0)) + ")")
print("0,0,1 Expect(FALSE), Actual(" + str(Win(0, 0, 1)) + ")")
print("1,1,0 Expect(TRUE), Actual(" + str(Win(1, 1, 0)) + ")")
print("1,0,1 Expect(TRUE), Actual(" + str(Win(1, 0, 1)) + ")")
print("0,1,1 Expect(TRUE), Actual(" + str(Win(0, 1, 1)) + ")")
print("0,0,2 Expect(TRUE), Actual(" + str(Win(0, 0, 2)) + ")")
print("0,1,2 Expect(TRUE), Actual(" + str(Win(0, 0, 2)) + ")")
print("1,1,1 Expect(FALSE), Actual(" + str(Win(1, 1, 1)) + ")")
print("2,1,1 Expect(TRUE), Actual(" + str(Win(2, 1, 1)) + ")")
print("3,1,1 Expect(TRUE), Actual(" + str(Win(3, 1, 1)) + ")")
print("3,2,1 Expect(TRUE), Actual(" + str(Win(3, 2, 1)) + ")")
print("5,2,1 Expect(TRUE), Actual(" + str(Win(5, 2, 1)) + ")")

