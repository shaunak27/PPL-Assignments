import numpy as np
c = 5
t = np.random.randint(100);
print("You have ",c,"chances to guess");
while(c > 0) :
	g = int(input("Enter your guess\n"))
	if(g < t):
		print("Your Guess no. is less than original no.")
	elif(g > t):
		print("Your Guess no. is more than original no.")
	else:
		print("You guessed Correctly !!")
		break;
	c -= 1

