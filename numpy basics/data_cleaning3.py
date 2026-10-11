import numpy as np
np.random.seed(10)
matrix_4x4=np.random.randint(0,255,(4,4))
# print(matrix_4x4)
matrix_3x3=np.resize(matrix_4x4,(3,3))
# print(matrix_3x3)

matrix_6x6=np.random.randint(0,255,(6,6))
matrix_4x9=np.reshape(matrix_6x6,(4,9))
# print(matrix_4x9)

matrix_4x8=np.random.normal(40,10,(4,8))
# print(matrix_4x8)
# print()
transpose_matrix=np.transpose(matrix_4x8)
# print(transpose_matrix)

matrix_3x3=np.random.randint(0,255,(3,3))
#  to do

matrix_4x4=np.random.randint(0,20,(4,4))
matrix_1D=np.reshape(matrix_4x4,(-1,))
print(matrix_1D)
matrix_1D=np.resize(matrix_4x4,(1,16))
print(matrix_1D)
print(matrix_4x4.flatten())
print(np.ravel(matrix_4x4))
