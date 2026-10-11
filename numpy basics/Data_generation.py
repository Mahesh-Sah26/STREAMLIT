import numpy as np
np.random.seed(42)
array_3x3=np.random.randint(1,100,(3,3))
# print(array_3x3)

array_4x4=np.random.standard_normal(size=(4,4))
# print(array_4x4)

matrix_5x5=np.identity(5)
# print(matrix_5x5)

matrix_5x4=np.random.normal(50,10,(5,4))
# print(matrix_5x4)

evenly_10=np.linspace(0,1,10)
print(evenly_10)

list=[10,20,30]
print(np.random.choice(list,size=(2,3)))

