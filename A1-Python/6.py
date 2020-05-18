c = 0
i = 0
while c < 20:
	L = list()
	L = [e  for e in range(i) if e !=0 and i%e==0]
	x = sum(L)
	if(i != x):
		M = list()
		M = [e for e in range(x) if e!=0 and x%e ==0]
		y = sum(M)
		if(y == i):
			c += 1
			print(i,x)
	i+=1
