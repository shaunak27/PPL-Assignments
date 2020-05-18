a = int(input('Enter Starting Term\n'))
r = int(input('Enter Common Ratio\n'))
m = a
c = 0
print('Geometric Progression is:')
while(c < 10):
	print(m)
	m = m * r
	c += 1
