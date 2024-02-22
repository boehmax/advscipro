import numpy as np
import random

N = 250

# NxN matrix
X = np.random.randint(0, 100, size=(N, N))

# Nx(N+1) matrix
Y = np.random.randint(0, 100, size=(N, N+1))

# Multiply matrices
result = np.dot(X, Y)

print(result)
