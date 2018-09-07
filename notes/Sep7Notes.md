# September 7 Notes

answers to the NIM.py problem
A lot of 
people forgot to negate the solution

you could take any number of stones from any pile

It should use a Loop(but this wasn't a requirement)

What is expected for assignment 2

## Problem to Solve during class

### [The Make Change problem](https://en.wikipedia.org/wiki/Change-making_problem)

This needs to be done in recursion

**Given:**
* amount of money (change) a= 273
* n Denominations of d<sub>1</sub> -> d<sub>n</sub>

**Find:**
* min number of coins need to make the change

### example of function

	/**
	* parameter a: the amount change needed
	* return: the number of coins to return
	**/
    int makeChange(int a)
		if( a < 0):
			return infinite
		if( a == 0)
			return 0
		for(i in range(0, n)):
			sol=min(makeChange(a-d(i)), sol)
		# we need to return +1 since we used up one problem
		return sol+1

The above approach will generate 4 recursive calls which each call will generate 4 recursive calls

If the number of function calls is greater than the input count. Then we know that it is duplicating calls, and Calls out for caching

## Dynamic Programming
this is the processo of converting the recursion algorithm to using cache

Cache
int <- S[a+1]

0
[0,,,,,n]
[0,,,,,]


Questions for TA:

What sub aspects are required for each problem