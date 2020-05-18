import numpy as np
while(1):
	print('You rolled:  ',np.random.randint(1,7))
	p = input('Would you like to try again ? [y/n] ')
	while(1):
		if(p is 'y'):
			break
		elif(p is 'n'):
			exit()
		else:
			p = input('Would you like to try again ? [y/n] ')

