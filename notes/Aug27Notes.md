He says his exams are hard. not multiple choice

Game algorithm practice
NIM/
pile of stones 2 person game
take turns by taking one or two stones. the last person to take a stone Loses.

variables
Number of stones = N
Number of choice = C
Remaining Stones = R
To determine how many stones you should take
Win decision procedure to determine C

Win(N) = C

N - C = N1
N == 1 you lose

o

you want to have 3 remaining when you get down to the end.

if you can select on the following you will win
2
3
4
5
6
7

Once you have more than that you

you want to have a Decision procedure to determine whether to take one or two stones.

### Problem Decomposition

Split Big Problems into smaller problems
you want to do a recursive search of the problem to determine the best chance of wining


### Meta Algorithm

    bool Win(N)
    {
        if (n == 0)
		    return true
		
		return !(Win(n-1) && Win(n-2))
    }

Win (n-1)    and Win(n-2)

### Solution Construction

| Win(n-1)    |  Win(n-2)   |   Win(n)  |
| ------------- |:-------------:| --------:|
| T              | T               |  F        |
| F              | T               |   T       |
| T              | F               |    T      |
| F              | F               |    T      |

**Example of using Win()**
	 
	 Play(n)
	 {
	    if (!Win(n-1))
			return 1
		else
			return 2
		
	 }
	 
	 
