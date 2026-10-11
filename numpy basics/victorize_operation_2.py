import numpy as np

price_array=np.array([100,150,200,250,300,270])
current_price = price_array[1:]
previous_price = price_array[:-1]


return_ar=(current_price-previous_price)/previous_price
print(return_ar)

deposits_amount=np.array([10,15,20,25,30,27])
total_amount_ar=np.cumsum(deposits_amount)
print(total_amount_ar)
# print(np.cumsum(deposits_amount))

co2_emission=np.array([100,150,200,250,300])
minimum=np.min(co2_emission)
maximum=np.max(co2_emission)
x_norm=(co2_emission-minimum)/(maximum-minimum)
print(x_norm)

def increment_salary(current_salary):
    if current_salary<1000:
        increased_salary=current_salary+0.2*current_salary
        return increased_salary
    if 1000<=current_salary<=5000:
        increased_salary=current_salary+0.1*current_salary
        return increased_salary
    if current_salary>5000:
        increased_salary=current_salary+0.05*current_salary
        return increased_salary
    
current_salary=np.array([800,1200,3000,6000])
new_salary_array=np.vectorize(increment_salary)(current_salary)
print(new_salary_array)
