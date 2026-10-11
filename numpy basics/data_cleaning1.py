import numpy as np
np.random.seed(10)
array_1=np.array([12,43,65,1,76,776,7,-90])
def clean_outlier(array_1):
    q1=np.quantile(array_1,0.25)
    q3=np.quantile(array_1,0.75)
    IQR=q3-q1
    lower_bound=q1-1.5*IQR
    upper_bound=q3+1.5*IQR
    mid=np.median(array_1)
    clean_data=np.where((array_1<=lower_bound)|(array_1>=upper_bound),mid,array_1)
    return clean_data
# print(clean_outlier(array_1))

def clean_outlier_std(array_1):
    average=np.mean(array_1)
    stdeviation=np.std(array_1)
    mid=np.median(array_1)
    lower_bound=average-2*stdeviation
    upper_bound=average+2*stdeviation
    clean_data=np.where(((array_1<=lower_bound) | (array_1>=upper_bound)),mid,array_1)
    return clean_data

# print(clean_outlier_std(array_1))


sensor_data=np.random.randint(-1,20,10)
# print(type(sensor_data))
def clean_invalid(sensor_data):
    print(sensor_data)
    clean_data=sensor_data.copy()
    for i in range(len(sensor_data)):
        if sensor_data[i]==-1:
            if i==0:
                clean_data[i]=sensor_data[i+1]
            elif i==(len(sensor_data)-1):
                clean_data[i]=sensor_data[i-1]
            else:
                clean_data[i]=(sensor_data[i-1]+sensor_data[i+1])/2

    return clean_data

result=clean_invalid(sensor_data)
# print(result)

matrix_2d=np.array([[34,544,-999],[32,432,-322],[321,432,212]])
print(matrix_2d)

# def fix_invalid_data(matrix_2d):
#     mean=np.mean(matrix_2d)
#     clean_data=np.round(np.where(matrix_2d==-999,mean,matrix_2d),2)
#     print(clean_data)

# fix_invalid_data(matrix_2d)

# def fix(matrix_2d,axis):
#     mean=np.mean(matrix_2d,axis=axis)
#     print(np.round(np.where(matrix_2d==-999),mean,matrix_2d))

# fix(matrix_2d,0)

