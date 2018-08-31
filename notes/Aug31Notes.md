CS5050 Aug31 Notes

### Steps to solve the problems
* Input/Output
** Input description => Problem Description
** Solution Description
* Simple Problem -> Simple Solution
* Big Problem -> Smaller Problems
* Smaller Solutions -> bigger Solutions

New Simple Problem

### Knapsack Problem

Used often, USP how packages can I pack into my truck like problem

Given: 
	n 10 objects
		each size s(i) 0 <=i<n
		size is int
	k size of the knapsack
	
Find: Does there exist a subset of objects that exactly fit into k?

example
K = 10
3 objects
	s(0) = 5
	s(1) = 2
	s(2) = 7

### Step 1
We should recursively insert all of the different packages till all of the packages have been placed into the knapsack, if it is larger that the other then use that.


### Step 2 : Have the Recursive Solution

1. How many calls? -> Too many countCalls(n)
2. How many unique problems?   count Problems(n) => (n+1)x(k+1)
3. If countcalls(n) >> countProblems(n) -> duplicate calls
4. Apply memoizing -- cache solution


Board 2
Bool 	Knap(n, k)		s[0], s[1],....
								ints

						knap(n, k)							1 call
			knap						knap				2 calls
		knap	knap			knap			knap		4 calls
knap	knap knap	knap 	knap 	knap	knap	knap	8 calls

	if n == 0:
The problem code is in the python program


### How to cache the solution

problem -> solution


sol[i, j] = Bool
