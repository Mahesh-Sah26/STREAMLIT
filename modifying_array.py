import numpy as np

info=[["Rabindra","Instructor"],["Mahesh","Student"],["Roshan","Student"]]
array_list=np.array(info)
# print(array_list)
# print(array_list.shape)
# print(array_list.dtype)

new_array=np.append(array_list,[["Sita","Student"]],axis=0)
# print(new_array)

matrix_4x3=np.append(new_array,[[30],[25],[28],[22]],axis=1)
# print(matrix_4x3)

matrix_3x3=np.delete(matrix_4x3,1,axis=0)
# print(matrix_3x3)

matrix_3x2=np.delete(matrix_3x3,-1,axis=1) 
# print(matrix_3x2)

matrix_3x3=np.insert(matrix_3x2,1,["kathandu","mumbai","newyork"],axis=1)
# print(matrix_3x3)

print(matrix_3x3[:,0])
print(matrix_3x3[0][1])
print(matrix_3x3[1][:])

