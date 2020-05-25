current_bank = 1
s1 = {"tiger", "goat"}
s2 = {"goat", "grass"}
first = {"tiger", "goat", "grass"}
second = set()
while len(first) > 0 :
	if current_bank == 1 :
		if len(first) == 3 :
			x = first.pop()
			if (first != s1) and (first != s2) :
				print( x  + " taken from first bank to second bank")
				second.add(x)
				current_bank = 2
			else :
				first.add(x)
		else :
			x = first.pop()
			print( x  + " taken from first bank to second bank")
			second.add(x)
			current_bank = 2
	else :
		if (second != s1) and (second != s2) :
			print("Person comes back")
		else :
			x = second.pop()
			print( x  + " taken from second bank to first bank")
			first.add(x)
		current_bank = 1
print("End of Game !!")
