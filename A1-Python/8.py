
import numpy as np
m = int(input("Enter the size of the matrix\n"))
a = np.zeros((m,m), dtype = float)
for i in range (m):
    s = input('Enter ' + str(i) + ' th Row\n')
    t = s.split()
    for j,ij in zip(t,range(len(t))):
        a[i][ij] = float(int(j))
print(a)


u = a.copy()
l = np.identity(m)

for i in range(m-1):
    for j in range(i+1,m):
        l[j][i] = u[j][i]/u[i][i]
        u[j][:] -= u[j][i]/u[i][i]*u[i][:]
print('U :\n',u)
print('L: \n',l)





