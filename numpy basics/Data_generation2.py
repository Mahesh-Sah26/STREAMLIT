import csv
import numpy as np
n=int(input("Enter how many number of detail you want: "))
np.random.seed(101)
rollno=np.arange(1,n+1)
# print(rollno)
age=np.random.randint(18,25,(n,))
# print(age)
firstname=["Mahesh","Ganesh","Roshan","Bikee","Nishant"]
first_name=np.random.choice(firstname,n)
lastname=["Sah","sah","Kalwar","chaudhary","Yadav"]
last_name=np.random.choice(lastname,n)
height=np.random.normal(160,20,(n,))
# print(height)

rating=np.random.uniform(1.0,5.0,n)
rounded_rating=np.round(rating,1)
# print(rounded_rating)
header=['RollNo','FirstName','lastName','Age','Height',"Rating2"]
data=zip(rollno,first_name,last_name,age,height,rating)
with open("students.csv",'w') as file:

    writer=csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

