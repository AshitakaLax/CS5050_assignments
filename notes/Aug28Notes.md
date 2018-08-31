## Aug 29 Notes

Office Hours
1pm-2:30 M,W
1pm-2:30 Tue


## Meta Algorithm

1. Solution Type
	Problem Representation

2. Simple Problems - Simple Solutions

3. Hard Problem -> break into -> Smaller Problems

4. Solution (smaller problems) -> Solution to Larger Problem

## NIM Game

  T,F <= Win (n)
	if n == 0
		return true
	if n == 1
		return false
	
	return !((win(n-1)&& win(n-2))
	
## Performance
	Time(Problem Size)  Space(Problem Size)
	
	
Time: Count the number of operations
	Function Calls ( of a function of N)
	
Create function countof <- calls(n) (where n is the problem size)

Calls	
	if n <= 1 return 1
	return calls(n-1) + calls (n-2) + 1

To simplify it we update it to the following which results in the Fibonacci sequence
f(0) = 1
f(1) = 1
f(n) = f(n-1) + f(n+2)

BigO
F(n) = a^n  where a > 1

Short curcuit evaluation ex. if(0 && 1) then it won't evaluate 1 since it already knows it is false

call tree

							win(n) 
		win(n-1)							win(n-2)
	win(n-2)	 win(n-3)		win(n-3)		win(n-4)
win(n-3)	win(n-4)			win(n-4) win(n-5)

There are a lot of duplicate function calls
Store the function calls
here is the  Memorization of the nim game

https://stackoverflow.com/questions/22918242/is-dynamic-programming-backtracking-with-cache
  T,F <= Win (n)
	if n == 0
		return true
	if n == 1
		return false
	
	Cache[n] =!((win(n-1)&& win(n-2))



	