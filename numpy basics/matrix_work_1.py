import numpy as np
temp_data=[1.2,6.34,5.21,3.2,2.5,1.5,0.4,4.6,2.4,3.1,1.7,3.53,3.11,2.22,5.33,3.22,5.6,7.5,7.4,3.5,5.7,9.6,7.54,6.44]
array=np.array(temp_data)
print(array)
print(len(array))
print(array.shape) # used to print shape of the array
print(array.dtype) # used to print data type of the items in array
print(array.ndim) # used to show the dimension of the array

print(f" Temperature at 12PM: {array[12]}")
print(array[-10])
array[-10]=-1
print(array[14])
print(f" Temperature from 10 AM to 6 PM : {array[10:19]}")
n_array=np.delete(array,-10)
print(f"Temperature of 2 PM is deleted successfylly! : {array[-10]}")
print(n_array)
print(np.median(n_array))
array=np.insert(n_array,-9,np.median(n_array))
print(array)
min_temperature=np.min(array)
time=np.argmin(array)
if time==0:
    print(f"Minimum temperature is {min_temperature} at 12 AM")
if time<12:
    print(f"Minimum temperature is {min_temperature} at {time} AM")
if time==12:
    print(f"Minimum temperature is {min_temperature} at {time} PM")
if time>12:
    print(f"Minimum temperature is {min_temperature} at {time-12} PM")
max_temperature=np.max(array)
time=np.argmax(array)
if time>12:
    print(f"Maximum temperature is {max_temperature} at {time-12} PM")
if time==12:
    print(f"Maximum temperature is {max_temperature} at {time} PM")
if time==0:
    print(f"Maximum temperature is {max_temperature} at 12 AM")
if time<12:
    print(f"Maximum temperature is {max_temperature} at {time} AM")

print(f"Standard Deviation : {np.std(array):.2f}")