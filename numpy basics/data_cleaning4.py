import numpy as np
np.random.seed(20)
array_4x3=np.random.randint(0,60,(4,3))
array_2x3=np.random.randint(10,80,(2,3))
combined_array=np.concatenate((array_4x3,array_2x3),axis=0)
# print(combined_array)
# print(np.vstack((array_4x3,array_2x3)))

array_1=np.random.randint(60,80,(3,4))
array_2=np.random.randint(20,90,(3,4))
combined_array=np.concatenate((array_1,array_2),axis=1)
# print(combined_array)
# print(np.hstack((array_1,array_2)))

ram_reading=np.array([[.5, 22], [.3, 20], [.7, 25]])
shyam_reading=np.array([[.3, 20], [.2, 23], [.24, 21]])
combined_reading=np.concatenate((ram_reading,shyam_reading),axis=0)
# print(combined_reading)

# print(f"Min Co2: {np.min(combined_reading[:,0])}")
# print(f"Max Co2: {np.max(combined_reading[:,0])}")
# print(f"Min Temp: {np.min(combined_reading[:,1])}")
# print(f"Max Temp: {np.max(combined_reading[:,1])}")

brnd_sz_ar = np.array([['Adidas', 'S'], ['Nike', 'L'], ['Adidas', 'M'], ['Nike', 'S']])
prc_wrnty_ar = np.array([[150, 1], [120, 0.6], [200, 1.2], [180, 0.9]])
tshirt_info=np.concatenate((brnd_sz_ar,prc_wrnty_ar),axis=1)
print(tshirt_info)

# Create 4x3 array with random values from 0-60. 
# Another 2x3 array with random values from 10-80.
#  Merge them vertically using concat and vstack.
# Create 3x4 array with random values from 60-80. 
# Another 3x2 array with random values from 20-90. 
# Merge them horizontally using concat and hstack.
# Ram and Shyam are doing survey on KTM & POKHARA city for pollution.
# CO2 & Temp reading recorded by them are [[.5, 22], [.3, 20], [.7, 25]], [[.3, 20], [.2, 23], [.24, 21]].
# - What is max & min value of CO2 and Temperature? (considering both cities)
# - Display CO2 & Temp readings for day - 2? (both city)
# Store brnd_sz_ar as [['Adidas', 'S'], ['Nike', 'L'], ['Adidas', 'M'], ['Nike', 'S']. 
#  Store prc_wrnty_ar as [[150, 1], [120, 0.6], [200, 1.2], [180, 0.9]]. 
#  Create array tshirt_info by combining feature from these.