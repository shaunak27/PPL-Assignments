L = list()
G = list()
M = list()
i = input("Enter Available pages\n")
L = i.split()
L.sort()
for i in range(1, int(L[-1]) + 1):
	G.append(str(i))
M = [j for j in G if j not in L]
print("Missing Pages are")
print(" ".join(M))

