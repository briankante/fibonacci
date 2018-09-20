print("hello.... enter number of fibonnaci needed")
n=input()
def fibonnaci1 (k):
	if k == 1 or k == 2:
		return 1
	return fibonnaci1 (k-1) + fibonnaci1 (k-2)

for i in fibonnaci1():
	if k >= n:
		break
	print (i)
	k += 1