# Normal game of nim

def win(n):
	if n == 0:
		return True
	if n == 1:
		return False
	return not (win(n-1) and win(n-2))

for i in range(0, 20):
	#print(i)
	print(str(i) + " " + str(win(i)))
  