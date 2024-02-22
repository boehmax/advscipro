import numpy as np

a = np.zeros(10) 
a[4] = 1
a

b = np.arange(10,49)
b

c = b[::-1]
c

d = np.arange(9).reshape(3,3)
d

e = b[1,2,0,0,4,0]
e

f = np.random.random_sample(30)
np.mean(f)


X = 3; Y = 4
g = np.zeros(X*Y).reshape(X,Y)
g[-1] = 1
g[0] = 1
g[:,-1] = 1
g[:,0] = 1

h = np.zeros((8,8), dtype=int)
h[1::2, ::2] = 1
h[::2, 1::2] =1
h

i = np.array([[0,1],[1,0]])
np.tile(i,(4,4))

j = np.arange(11)
j[4:8] = j[4:8]*-1
print(j)

k = np.random.random(10)
np.sort(k)

l_A = np.random.randint(0,2,5)
l_B = np.random.randint(0,2,5)
equal = l_A == l_B
print(equal)


m = np.arange(10, dtype=np.int32)
print(m.dtype)
m = np.square(m)
print(m.dytpe)

n_A = np.arange(9).reshape(3,3)
n_B = n_A + 1
n_C = np.dot(n_A,n_B)
n_D = np.diag(n_C)
print(n_D)

