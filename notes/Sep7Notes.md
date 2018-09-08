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


results of running 10-140
The memorizing approach
TESTING 10 OBJECTS
0:00:00.231615, 11754,13584, Result:False
0:00:00.161930, 7517, 3947,  Result:False
0:00:00.022059, 863,  285,   Result:True
0:00:00.196537, 9037, 6521,  Result:False
0:00:00.278208, 13046,10642, Result:False
0:00:00.193584, 9237, 6787,  Result:False
0:00:00.011025, 477,  100,   Result:True
0:00:00.083723, 3584, 1205,  Result:False
0:00:00.218130, 9870, 8357,  Result:False
0:00:00.092742, 4250, 2894,  Result:False
TESTING 20 OBJECTS
Duration:0:00:00.010528 RecursiveCounter:428 CacheHitCounter:65 Result:True
Duration:0:00:00 RecursiveCounter:9 CacheHitCounter:0 Result:True
Duration:0:00:00.031588 RecursiveCounter:1260 CacheHitCounter:491 Result:True
Duration:0:00:00.026573 RecursiveCounter:1004 CacheHitCounter:298 Result:True
Duration:0:00:00.005547 RecursiveCounter:186 CacheHitCounter:6 Result:True
Duration:0:00:00.003018 RecursiveCounter:105 CacheHitCounter:1 Result:True
Duration:0:00:00.003008 RecursiveCounter:79 CacheHitCounter:2 Result:True
Duration:0:00:00.000502 RecursiveCounter:11 CacheHitCounter:0 Result:True
Duration:0:00:00.002007 RecursiveCounter:50 CacheHitCounter:1 Result:True
Duration:0:00:00.023563 RecursiveCounter:945 CacheHitCounter:18 Result:True
TESTING 30 OBJECTS
Duration:0:00:00 RecursiveCounter:12 CacheHitCounter:0 Result:True
Duration:0:00:00.058657 RecursiveCounter:2406 CacheHitCounter:782 Result:True
Duration:0:00:00.022089 RecursiveCounter:876 CacheHitCounter:89 Result:True
Duration:0:00:00 RecursiveCounter:10 CacheHitCounter:0 Result:True
Duration:0:00:00.018558 RecursiveCounter:761 CacheHitCounter:212 Result:True
Duration:0:00:00.003509 RecursiveCounter:160 CacheHitCounter:29 Result:True
Duration:0:00:00.002532 RecursiveCounter:69 CacheHitCounter:4 Result:True
Duration:0:00:00.027092 RecursiveCounter:1104 CacheHitCounter:241 Result:True
Duration:0:00:00.026070 RecursiveCounter:1100 CacheHitCounter:707 Result:True
Duration:0:00:00.001003 RecursiveCounter:33 CacheHitCounter:0 Result:True
TESTING 40 OBJECTS
Duration:0:00:00.001504 RecursiveCounter:63 CacheHitCounter:0 Result:True
Duration:0:00:00.068180 RecursiveCounter:2870 CacheHitCounter:1161 Result:True
Duration:0:00:00.016042 RecursiveCounter:713 CacheHitCounter:96 Result:True
Duration:0:00:00.130842 RecursiveCounter:6034 CacheHitCounter:4196 Result:True
Duration:0:00:00.000502 RecursiveCounter:21 CacheHitCounter:0 Result:True
Duration:0:00:00.010509 RecursiveCounter:476 CacheHitCounter:31 Result:True
Duration:0:00:00.028100 RecursiveCounter:1129 CacheHitCounter:503 Result:True
Duration:0:00:00.046155 RecursiveCounter:2046 CacheHitCounter:965 Result:True
Duration:0:00:00.005514 RecursiveCounter:237 CacheHitCounter:2 Result:True
Duration:0:00:00.001034 RecursiveCounter:63 CacheHitCounter:0 Result:True
TESTING 50 OBJECTS
Duration:0:00:00.006016 RecursiveCounter:245 CacheHitCounter:19 Result:True
Duration:0:00:00.001034 RecursiveCounter:30 CacheHitCounter:0 Result:True
Duration:0:00:00.001038 RecursiveCounter:38 CacheHitCounter:0 Result:True
Duration:0:00:00.002004 RecursiveCounter:66 CacheHitCounter:0 Result:True
Duration:0:00:00.008016 RecursiveCounter:364 CacheHitCounter:69 Result:True
Duration:0:00:00.001503 RecursiveCounter:51 CacheHitCounter:0 Result:True
Duration:0:00:00.004519 RecursiveCounter:188 CacheHitCounter:5 Result:True
Duration:0:00:00.000501 RecursiveCounter:21 CacheHitCounter:0 Result:True
Duration:0:00:00.001004 RecursiveCounter:44 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:27 CacheHitCounter:0 Result:True
TESTING 60 OBJECTS
Duration:0:00:00.195519 RecursiveCounter:8964 CacheHitCounter:6183 Result:True
Duration:0:00:00.003008 RecursiveCounter:120 CacheHitCounter:2 Result:True
Duration:0:00:00.000988 RecursiveCounter:42 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:44 CacheHitCounter:0 Result:True
Duration:0:00:00.021051 RecursiveCounter:876 CacheHitCounter:93 Result:True
Duration:0:00:00.001033 RecursiveCounter:41 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:47 CacheHitCounter:0 Result:True
Duration:0:00:00.085697 RecursiveCounter:3656 CacheHitCounter:991 Result:True
Duration:0:00:00.007055 RecursiveCounter:300 CacheHitCounter:18 Result:True
Duration:0:00:00.017516 RecursiveCounter:672 CacheHitCounter:138 Result:True
TESTING 70 OBJECTS
Duration:0:00:00.001503 RecursiveCounter:51 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:32 CacheHitCounter:0 Result:True
Duration:0:00:00.005507 RecursiveCounter:204 CacheHitCounter:13 Result:True
Duration:0:00:00.000501 RecursiveCounter:37 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:45 CacheHitCounter:0 Result:True
Duration:0:00:00.276734 RecursiveCounter:11795 CacheHitCounter:8563 Result:True
Duration:0:00:00.001505 RecursiveCounter:62 CacheHitCounter:0 Result:True
Duration:0:00:00.007520 RecursiveCounter:267 CacheHitCounter:5 Result:True
Duration:0:00:00.000503 RecursiveCounter:12 CacheHitCounter:0 Result:True
Duration:0:00:00.007520 RecursiveCounter:227 CacheHitCounter:1 Result:True
TESTING 80 OBJECTS
Duration:0:00:00.000500 RecursiveCounter:32 CacheHitCounter:0 Result:True
Duration:0:00:00.002018 RecursiveCounter:103 CacheHitCounter:0 Result:True
Duration:0:00:00.001967 RecursiveCounter:93 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:16 CacheHitCounter:0 Result:True
Duration:0:00:00.009023 RecursiveCounter:348 CacheHitCounter:6 Result:True
Duration:0:00:00.002005 RecursiveCounter:43 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:75 CacheHitCounter:0 Result:True
Duration:0:00:00.000991 RecursiveCounter:44 CacheHitCounter:0 Result:True
Duration:0:00:00.005013 RecursiveCounter:167 CacheHitCounter:5 Result:True
Duration:0:00:00.017046 RecursiveCounter:588 CacheHitCounter:14 Result:True
TESTING 90 OBJECTS
Duration:0:00:00.000490 RecursiveCounter:29 CacheHitCounter:0 Result:True
Duration:0:00:00.001001 RecursiveCounter:35 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:34 CacheHitCounter:0 Result:True
Duration:0:00:00.029579 RecursiveCounter:966 CacheHitCounter:58 Result:True
Duration:0:00:00.002016 RecursiveCounter:48 CacheHitCounter:0 Result:True
Duration:0:00:00.002005 RecursiveCounter:84 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:35 CacheHitCounter:0 Result:True
Duration:0:00:00.034091 RecursiveCounter:1266 CacheHitCounter:199 Result:True
Duration:0:00:00.001003 RecursiveCounter:39 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:48 CacheHitCounter:0 Result:True
TESTING 100 OBJECTS
Duration:0:00:00.002005 RecursiveCounter:84 CacheHitCounter:0 Result:True
Duration:0:00:00.002007 RecursiveCounter:68 CacheHitCounter:0 Result:True
Duration:0:00:00.005013 RecursiveCounter:192 CacheHitCounter:1 Result:True
Duration:0:00:00.001003 RecursiveCounter:51 CacheHitCounter:0 Result:True
Duration:0:00:00.002507 RecursiveCounter:76 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:18 CacheHitCounter:0 Result:True
Duration:0:00:00.013020 RecursiveCounter:552 CacheHitCounter:17 Result:True
Duration:0:00:00.002507 RecursiveCounter:78 CacheHitCounter:0 Result:True
Duration:0:00:00.003520 RecursiveCounter:94 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:51 CacheHitCounter:0 Result:True
TESTING 110 OBJECTS
Duration:0:00:00.002005 RecursiveCounter:80 CacheHitCounter:0 Result:True
Duration:0:00:00.004010 RecursiveCounter:200 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:17 CacheHitCounter:0 Result:True
Duration:0:00:00.002007 RecursiveCounter:77 CacheHitCounter:0 Result:True
Duration:0:00:00.005013 RecursiveCounter:195 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:20 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:31 CacheHitCounter:0 Result:True
Duration:0:00:00.060662 RecursiveCounter:2192 CacheHitCounter:115 Result:True
Duration:0:00:00.016543 RecursiveCounter:685 CacheHitCounter:31 Result:True
Duration:0:00:00.001504 RecursiveCounter:54 CacheHitCounter:0 Result:True
TESTING 120 OBJECTS
Duration:0:00:00.002508 RecursiveCounter:112 CacheHitCounter:0 Result:True
Duration:0:00:00.000500 RecursiveCounter:28 CacheHitCounter:0 Result:True
Duration:0:00:00.001505 RecursiveCounter:64 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:40 CacheHitCounter:0 Result:True
Duration:0:00:00.002005 RecursiveCounter:101 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:78 CacheHitCounter:0 Result:True
Duration:0:00:00.006518 RecursiveCounter:250 CacheHitCounter:1 Result:True
Duration:0:00:00.001505 RecursiveCounter:58 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:26 CacheHitCounter:0 Result:True
Duration:0:00:00.003510 RecursiveCounter:88 CacheHitCounter:0 Result:True
TESTING 130 OBJECTS
Duration:0:00:00.004013 RecursiveCounter:145 CacheHitCounter:0 Result:True
Duration:0:00:00.011028 RecursiveCounter:337 CacheHitCounter:1 Result:True
Duration:0:00:00.001504 RecursiveCounter:35 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:40 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:32 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:69 CacheHitCounter:0 Result:True
Duration:0:00:00.003509 RecursiveCounter:84 CacheHitCounter:0 Result:True
Duration:0:00:00.004010 RecursiveCounter:128 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:10 CacheHitCounter:0 Result:True
Duration:0:00:00.001503 RecursiveCounter:71 CacheHitCounter:0 Result:True
TESTING 140 OBJECTS
Duration:0:00:00.004512 RecursiveCounter:121 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:30 CacheHitCounter:0 Result:True
Duration:0:00:00.004512 RecursiveCounter:126 CacheHitCounter:0 Result:True
Duration:0:00:00.001495 RecursiveCounter:58 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:47 CacheHitCounter:0 Result:True
Duration:0:00:00.004011 RecursiveCounter:186 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:8 CacheHitCounter:0 Result:True
Duration:0:00:00.001001 RecursiveCounter:46 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:49 CacheHitCounter:0 Result:True
Duration:0:00:00.004012 RecursiveCounter:162 CacheHitCounter:0 Result:True
TESTING 150 OBJECTS
Duration:0:00:00.001003 RecursiveCounter:41 CacheHitCounter:0 Result:True
Duration:0:00:00.002506 RecursiveCounter:82 CacheHitCounter:0 Result:True
Duration:0:00:00.002507 RecursiveCounter:99 CacheHitCounter:0 Result:True
Duration:0:00:00.002506 RecursiveCounter:118 CacheHitCounter:0 Result:True
Duration:0:00:00.003509 RecursiveCounter:96 CacheHitCounter:0 Result:True
Duration:0:00:00.005515 RecursiveCounter:174 CacheHitCounter:0 Result:True
Duration:0:00:00.004012 RecursiveCounter:150 CacheHitCounter:0 Result:True
Duration:0:00:00.002544 RecursiveCounter:101 CacheHitCounter:0 Result:True
Duration:0:00:00.001503 RecursiveCounter:75 CacheHitCounter:0 Result:True
Duration:0:00:00.019055 RecursiveCounter:618 CacheHitCounter:3 Result:True
TESTING 160 OBJECTS
Duration:0:00:00.002508 RecursiveCounter:58 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:28 CacheHitCounter:0 Result:True
Duration:0:00:00.036096 RecursiveCounter:1325 CacheHitCounter:83 Result:True
Duration:0:00:00.003509 RecursiveCounter:149 CacheHitCounter:0 Result:True
Duration:0:00:00.001469 RecursiveCounter:57 CacheHitCounter:0 Result:True
Duration:0:00:00.001001 RecursiveCounter:32 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:51 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:50 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:57 CacheHitCounter:0 Result:True
Duration:0:00:00.001505 RecursiveCounter:65 CacheHitCounter:0 Result:True
TESTING 170 OBJECTS
Duration:0:00:00.001001 RecursiveCounter:48 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:47 CacheHitCounter:0 Result:True
Duration:0:00:00.002974 RecursiveCounter:116 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:28 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:32 CacheHitCounter:0 Result:True
Duration:0:00:00.002005 RecursiveCounter:75 CacheHitCounter:0 Result:True
Duration:0:00:00.002507 RecursiveCounter:113 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:19 CacheHitCounter:0 Result:True
Duration:0:00:00.008036 RecursiveCounter:174 CacheHitCounter:0 Result:True
Duration:0:00:00.014537 RecursiveCounter:418 CacheHitCounter:1 Result:True
TESTING 180 OBJECTS
Duration:0:00:00.001504 RecursiveCounter:32 CacheHitCounter:0 Result:True
Duration:0:00:00.000500 RecursiveCounter:22 CacheHitCounter:0 Result:True
Duration:0:00:00.004010 RecursiveCounter:109 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:60 CacheHitCounter:0 Result:True
Duration:0:00:00.002507 RecursiveCounter:101 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:19 CacheHitCounter:0 Result:True
Duration:0:00:00.039605 RecursiveCounter:1441 CacheHitCounter:76 Result:True
Duration:0:00:00.001004 RecursiveCounter:45 CacheHitCounter:0 Result:True
Duration:0:00:00.002506 RecursiveCounter:119 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:13 CacheHitCounter:0 Result:True
TESTING 190 OBJECTS
Duration:0:00:00.005014 RecursiveCounter:165 CacheHitCounter:0 Result:True
Duration:0:00:00.002507 RecursiveCounter:86 CacheHitCounter:0 Result:True
Duration:0:00:00.002508 RecursiveCounter:110 CacheHitCounter:0 Result:True
Duration:0:00:00.003008 RecursiveCounter:125 CacheHitCounter:0 Result:True
Duration:0:00:00.003510 RecursiveCounter:125 CacheHitCounter:0 Result:True
Duration:0:00:00.001991 RecursiveCounter:69 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:40 CacheHitCounter:0 Result:True
Duration:0:00:00.004512 RecursiveCounter:185 CacheHitCounter:0 Result:True
Duration:0:00:00.002510 RecursiveCounter:80 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:54 CacheHitCounter:0 Result:True


This is the Recursion approach
TESTING 10 OBJECTS
Duration:0:00:00.018549 RecursiveCounter:1653 CacheHitCounter:0 Result:True
Duration:0:00:00.238132 RecursiveCounter:25124 CacheHitCounter:0 Result:False
Duration:0:00:00.059157 RecursiveCounter:6597 CacheHitCounter:0 Result:True
Duration:0:00:00.038612 RecursiveCounter:4304 CacheHitCounter:0 Result:True
Duration:0:00:00.102233 RecursiveCounter:11582 CacheHitCounter:0 Result:False
Duration:0:00:00.093751 RecursiveCounter:10564 CacheHitCounter:0 Result:True
Duration:0:00:00.083222 RecursiveCounter:9410 CacheHitCounter:0 Result:False
Duration:0:00:00.204061 RecursiveCounter:22650 CacheHitCounter:0 Result:False
Duration:0:00:00.015041 RecursiveCounter:1686 CacheHitCounter:0 Result:True
Duration:0:00:00.197579 RecursiveCounter:20498 CacheHitCounter:0 Result:False
TESTING 20 OBJECTS
Duration:0:00:00.000493 RecursiveCounter:60 CacheHitCounter:0 Result:True
Duration:0:00:00.000489 RecursiveCounter:43 CacheHitCounter:0 Result:True
Duration:0:00:00.321914 RecursiveCounter:37887 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:47 CacheHitCounter:0 Result:True
Duration:0:00:00.074689 RecursiveCounter:8829 CacheHitCounter:0 Result:True
Duration:0:00:00.043106 RecursiveCounter:4987 CacheHitCounter:0 Result:True
Duration:0:00:00.244150 RecursiveCounter:29044 CacheHitCounter:0 Result:True
Duration:0:00:00.005014 RecursiveCounter:671 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:149 CacheHitCounter:0 Result:True
Duration:0:00:00.010532 RecursiveCounter:1217 CacheHitCounter:0 Result:True
TESTING 30 OBJECTS
Duration:0:00:00.000502 RecursiveCounter:28 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:31 CacheHitCounter:0 Result:True
Duration:0:00:00.002005 RecursiveCounter:283 CacheHitCounter:0 Result:True
Duration:0:00:00.002998 RecursiveCounter:407 CacheHitCounter:0 Result:True
Duration:0:00:00.207089 RecursiveCounter:24635 CacheHitCounter:0 Result:True
Duration:0:00:01.005345 RecursiveCounter:122011 CacheHitCounter:0 Result:True
Duration:0:00:00.007521 RecursiveCounter:895 CacheHitCounter:0 Result:True
Duration:0:00:00.048154 RecursiveCounter:5311 CacheHitCounter:0 Result:True
Duration:0:00:00.001029 RecursiveCounter:117 CacheHitCounter:0 Result:True
Duration:0:00:00.009024 RecursiveCounter:1058 CacheHitCounter:0 Result:True
TESTING 40 OBJECTS
Duration:0:00:00.004011 RecursiveCounter:471 CacheHitCounter:0 Result:True
Duration:0:00:00.006015 RecursiveCounter:675 CacheHitCounter:0 Result:True
Duration:0:00:00.002005 RecursiveCounter:219 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:81 CacheHitCounter:0 Result:True
Duration:0:00:00.013568 RecursiveCounter:1396 CacheHitCounter:0 Result:True
Duration:0:00:34.326295 RecursiveCounter:4164336 CacheHitCounter:0 Result:True
Duration:0:00:24.217850 RecursiveCounter:2975729 CacheHitCounter:0 Result:True
Duration:0:00:00.088735 RecursiveCounter:10715 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:18 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:56 CacheHitCounter:0 Result:True
TESTING 50 OBJECTS
Duration:0:00:00.001536 RecursiveCounter:189 CacheHitCounter:0 Result:True
Duration:0:00:00.006517 RecursiveCounter:805 CacheHitCounter:0 Result:True
Duration:0:00:00.004500 RecursiveCounter:476 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:19 CacheHitCounter:0 Result:True
Duration:0:00:00.005014 RecursiveCounter:568 CacheHitCounter:0 Result:True
Duration:0:00:00.002006 RecursiveCounter:175 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:25 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:10 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:67 CacheHitCounter:0 Result:True
Duration:0:00:00.004512 RecursiveCounter:520 CacheHitCounter:0 Result:True
TESTING 60 OBJECTS
Duration:0:00:00.000517 RecursiveCounter:17 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:44 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:32 CacheHitCounter:0 Result:True
Duration:0:00:00.002506 RecursiveCounter:296 CacheHitCounter:0 Result:True
Duration:0:00:00.053141 RecursiveCounter:5817 CacheHitCounter:0 Result:True
Duration:0:00:00.001001 RecursiveCounter:103 CacheHitCounter:0 Result:True
Duration:0:00:00.002507 RecursiveCounter:268 CacheHitCounter:0 Result:True
Duration:0:00:00.000500 RecursiveCounter:38 CacheHitCounter:0 Result:True
Duration:0:00:00.010528 RecursiveCounter:1228 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:73 CacheHitCounter:0 Result:True
TESTING 70 OBJECTS
Duration:0:00:00 RecursiveCounter:14 CacheHitCounter:0 Result:True
Duration:0:00:00.002004 RecursiveCounter:221 CacheHitCounter:0 Result:True
Duration:0:00:00.002004 RecursiveCounter:197 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:42 CacheHitCounter:0 Result:True
Duration:0:00:00.009024 RecursiveCounter:935 CacheHitCounter:0 Result:True
Duration:0:00:00.000493 RecursiveCounter:52 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:74 CacheHitCounter:0 Result:True
Duration:0:00:00.000498 RecursiveCounter:53 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:43 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:55 CacheHitCounter:0 Result:True
TESTING 80 OBJECTS
Duration:0:00:00 RecursiveCounter:46 CacheHitCounter:0 Result:True
Duration:0:00:00.005014 RecursiveCounter:380 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:69 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:25 CacheHitCounter:0 Result:True
Duration:0:00:00.001503 RecursiveCounter:138 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:23 CacheHitCounter:0 Result:True
Duration:0:00:00.006017 RecursiveCounter:687 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:227 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:145 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:21 CacheHitCounter:0 Result:True
TESTING 90 OBJECTS
Duration:0:00:00.001504 RecursiveCounter:143 CacheHitCounter:0 Result:True
Duration:0:00:00.030081 RecursiveCounter:3160 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:83 CacheHitCounter:0 Result:True
Duration:0:00:00.000495 RecursiveCounter:36 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:31 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:31 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:85 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:147 CacheHitCounter:0 Result:True
Duration:0:00:00.002005 RecursiveCounter:211 CacheHitCounter:0 Result:True
Duration:0:00:00.003009 RecursiveCounter:388 CacheHitCounter:0 Result:True
TESTING 100 OBJECTS
Duration:0:00:00.000501 RecursiveCounter:53 CacheHitCounter:0 Result:True
Duration:0:00:00.001006 RecursiveCounter:74 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:76 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:51 CacheHitCounter:0 Result:True
Duration:0:00:00.003009 RecursiveCounter:348 CacheHitCounter:0 Result:True
Duration:0:00:00.001035 RecursiveCounter:78 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:42 CacheHitCounter:0 Result:True
Duration:0:00:00.067680 RecursiveCounter:7730 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:99 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:81 CacheHitCounter:0 Result:True
TESTING 110 OBJECTS
Duration:0:00:00.002005 RecursiveCounter:175 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:12 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:82 CacheHitCounter:0 Result:True
Duration:0:00:00.021558 RecursiveCounter:2553 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:22 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:100 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:9 CacheHitCounter:0 Result:True
Duration:0:00:00.001514 RecursiveCounter:206 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:50 CacheHitCounter:0 Result:True
Duration:0:00:00.000509 RecursiveCounter:20 CacheHitCounter:0 Result:True
TESTING 120 OBJECTS
Duration:0:00:00.004011 RecursiveCounter:446 CacheHitCounter:0 Result:True
Duration:0:00:00.002005 RecursiveCounter:243 CacheHitCounter:0 Result:True
Duration:0:00:00.000503 RecursiveCounter:45 CacheHitCounter:0 Result:True
Duration:0:00:00.001504 RecursiveCounter:213 CacheHitCounter:0 Result:True
Duration:0:00:00.018047 RecursiveCounter:2044 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:47 CacheHitCounter:0 Result:True
Duration:0:00:00.002506 RecursiveCounter:254 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:83 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:121 CacheHitCounter:0 Result:True
Duration:0:00:00.014037 RecursiveCounter:1579 CacheHitCounter:0 Result:True
TESTING 130 OBJECTS
Duration:0:00:00.000501 RecursiveCounter:48 CacheHitCounter:0 Result:True
Duration:0:00:00.002507 RecursiveCounter:340 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:67 CacheHitCounter:0 Result:True
Duration:0:00:00.001003 RecursiveCounter:105 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:33 CacheHitCounter:0 Result:True
Duration:0:00:00.000502 RecursiveCounter:22 CacheHitCounter:0 Result:True
Duration:0:00:00.000512 RecursiveCounter:45 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:20 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:49 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:12 CacheHitCounter:0 Result:True
TESTING 140 OBJECTS
Duration:0:00:00.001003 RecursiveCounter:114 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:101 CacheHitCounter:0 Result:True
Duration:0:00:00.001002 RecursiveCounter:99 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:24 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:28 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:18 CacheHitCounter:0 Result:True
Duration:0:00:00 RecursiveCounter:17 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:13 CacheHitCounter:0 Result:True
Duration:0:00:00.000501 RecursiveCounter:46 CacheHitCounter:0 Result:True
Duration:0:00:00.002018 RecursiveCounter:245 CacheHitCounter:0 Result:True
TESTING 150 OBJECTS
Duration:0:00:00.001003 RecursiveCounter:81 CacheHitCounter:0 Result:True