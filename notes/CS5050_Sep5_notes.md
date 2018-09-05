CS5050 Notes
Date: Sep 5th, 2018

# Dynamic Programming
* No stack
* No Recursion
* Simple iteration
* Eager Algorithm

## Memoizing
* Compute once use many times
* Trades Space for Time
* Lazy Algorithm
* Needs a Stack!

You compute it save it, then move on

## example of DP

	One D Knapsack
	knap(n, k)
e.g. X =knap(55, 100)

2d array
kF               X
+F
+F-----[D][C]map(i,j)
+F         |
+F         |
+F     [E] |
+F         |
0 0++++++++++++++n(a)
      Time

base cases in 1d knapsack

if(k < 0) return False
A  if(k == 0) return True 
B  if(n == 0) return False

knap(i, j) = knap(i-1, j) or knap(i-1, j-S[i])
     C            D                 E

## The Meta Algorithm
When you start you calculate all of the possible results in the 2d array before running the algorithm
cache <- array(n+1, k+1)
 // base case
	for i in  range(0, n+1):
		cache[i,0] = True
	for j in range(1, k+1):
		Cache[0, j] = False
	for i in range(1, n+1):
		for j in range(1, k+1):
			cache[i,j] = cache[i-1, j-S[i]] or cache[i-1, j]
	return cache[n, k]

We have to cache 'cache[i-1, j-S[i]]' so it will require that we put up a guard

Question is why would Eager be faster than the recursive one since it calculates multiple

memory purporition to n x k
Time purporition to n x k