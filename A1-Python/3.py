def check(website):
    if ('.org' in website or '.xyz' in website):
        return True
    else:
        return False
if check(input('Enter site address\n')) is True:
	print("It is blocked");
else:
	print("It is not blocked");
