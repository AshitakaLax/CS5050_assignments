# CS5050 Sep10 Notes

'''
INT Change (c)
	if(c == 0)
		return 0
	if(c < 0)
		return INFINITY
	best = INFINITY
	for i in range(0, n)
		best= min(best, change(c-d[i]))
	
	return best + 1
'''

0
[0,,,,,n]
[0,,,,,]

[] 	[] 	[] 	[j]
		j-C[0]
		j-C[1]
		j-C[2]

This is the code to have a recursive algorithm converting it into a DP alorigthm by return the cache
```python
# n is the number of denominations
# 
int Cache [C+1]
cache[0] = 0
for j in range(0, C+1):
	best = sys.maxsize
	for(i in range(0, N)):
		best = min(best, cache[j-d[i]])
	cache[j]= best+1
return cache[c]
```
We start at 1 to N+1 since 0 is the base case, and we don't want to wipe it out
 It currently would crash since ```cache[j-d[i]]``` would go out of range

In order to fix this, we would need to put in a guard

```python
# n is the number of denominations
# 
int Cache [C+1]
cache[0] = 0
for j in range(0, C+1):
	best = sys.maxsize
	for(i in range(0, N)):
		if (j-d[i]>= 0):
			best = min(best, cache[j-d[i]])
	cache[j]= best+1
return cache[c]
```

```python
C=13
d[0] = 1
d[1] = 7
d[2] = 3
d[3] = 2
n = 4
```

cache

| index |0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
| iterator | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| Value    | 0 | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | 3 | 3 |
| formula   | j-c[13] | j-c[12] | j-c[11] | j-c[10] | j-c[9] | j-c[8] | j-c[7] | j-c[6] | j-c[5] | j-c[4] | j-c[3] | j-c[2] | j-c[1] | j-c[0] | 

Which coins
make up 13
This is called the **Trace Back Method**

This method mirrors the behavior of the coin selection
<- traceback(c) where c= problem
```python
	# base case
	if(c == 0):
		return []
	# general case
	# Which coin did the algorithm use
	best = sys.maxsize
	# this is the same as the for i in range(0,n) in the original function
	for i in range(0, n):
		#                     /--This is the arg min
		#                    |
		if (cache[c-d[i]] < best):
			best = cache[c-d[i]]
			usedcoin=d[i]# <-- remember the coin that gave the best answer
	return [usedcoin] + tracebackback(c-usedcoin) # appends the result of the traceback
	# when the loop is compelet we will know which coin was used to give us the best
```

Which **i** gave use the best 
usedcoin=d[i] # would be 7 or 3

traceback will return 7 or 3
if 7
[7] +([3] + ([3]))
