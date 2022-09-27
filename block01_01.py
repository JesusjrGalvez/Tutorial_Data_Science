import numpy as np


matrix_01 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix_01)
print(f"Typs is {type(matrix_01)}")
print(f"Shape of matrix is {matrix_01.shape}")

zero_01 = np.zeros(3)
print(zero_01)
zero_02 = np.zeros((3,3))
print(zero_02)

ones_01 = np.ones(2)
print(ones_01)
ones_02 = np.ones((2, 4))
print(ones_02)

full = np.full((3, 3), 10)
print(full)

identity = np.eye(5)
print(identity)

print("----------")
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

print(a)
print(a[:, 1]) # prints second column

print(a[:1, 2:2])



