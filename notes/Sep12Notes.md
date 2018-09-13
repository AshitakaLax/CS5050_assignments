# CS5050 Sep 12

## String Processing

### Spell Check

Strings don't just represent words, for e.g. DNA.

DNA is about 8 billion characters

They are able to match Ebola to the source with the DNA tracking.

Golden State serial killer is an example of good DNA matching

### Example problem of matching strings

 Given A => length n
 Given B => length m

Errors 
 invalid would be an 'a'-> 'z' char substitution
 Transposition
 missing character
 extra characters

given the word 
correctWord = "character"
invalidWord = "chrabterr"
"ch(r)a(b)ter(r)" missing a before, substituted, extra 

```python
# What is the minimum number of edits to get the next word
# of del, insert, sub
# this would be a naive implementation, it wouldn't handle various aspects of actual options, keyboard placement, etc...

#A= "    " # of length n
#B= "    " # of length M

A= "abc" # of length n
B= "bcad" # of length M


def MinED(n, m):
	# this handles if you need to insert additional characters, and if they match also
	if(n==0):
		return m
	if(m==0):
		return n

	#return min( of the following 3 functions)
	# What can we do to make it smaller
	return min((MinEd(n-1, m) + 1), # the +1 is since we have to make an edit ( This falls under the Solution contruction phase)
	(MinEd(n, m-1) + 1),
	(MinEd(n-1, m-1) + (A[n] != B[m]))) # add 1 if they are not equal this last function call is the only place that we actually compare the characters


print(MinEd(len(A),len(B)))


```
There are N+1*M+1 unique function call.

We don't want to do this recursively.
we could do this using memoize
or we can use DP by caculating all of the options up front, then call into DP

Friday TA will introduce BigO notation

side note: algorithm function typically work in terms of indexes