x = 0
c = 0
while(c < 10):
	x += 1
	s1 = 1
	y = 1
	for i in range(2,x+1):
		if x%i==0:
			s1+=1/i
			y += 1
	if(y/s1 == y//s1):
		print(x)
		c += 1
