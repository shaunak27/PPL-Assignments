x = input('Site name');
path = "/etc/hosts"
ip = "127.0.0."
fp = open(path,"a+")
fp.write(x,ip);
fp.close()

if __name__ == "__main__":
	main()

