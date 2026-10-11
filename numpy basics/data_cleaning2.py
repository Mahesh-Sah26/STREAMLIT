import numpy as np
salary_array=np.array([400,800,1200,5000,7000,3000])
def increment_salary(salary_array):
    conditions=[
        (salary_array<1000),
        (salary_array >=1000) & (salary_array<=5000),
        (salary_array>5000)
         ]
    choices=[(salary_array+0.20*salary_array),(salary_array+salary_array*0.1),(salary_array+salary_array*0.05)]

    increased_salary=np.select(conditions,choices,"Invalid")
    return increased_salary

result=increment_salary(salary_array)
# print(result)

def categorize_age(age_array):
    conditions=[
            (age_array>=0)&(age_array<10),
            (age_array>=10)&(age_array<20),
            (age_array>=20)&(age_array<40),
            (age_array>=40)&(age_array<60),
            (age_array>=60)
            ]
    choices=["Child","Teen","Young","Mid-age","old"]
    age_category=np.select(conditions,choices,"Invalid")
    return age_category

age_array=np.array([12,43,65,34,7,43,65,87,98,-1])
# print(categorize_age(age_array))


temp_data=np.array([15,22,30,5,18,25])
average=np.mean(temp_data)
condition=temp_data<average
temp_cat=np.where(condition,"below_avg","above_avg") 
print(temp_cat)


player_name=np.array(["player1","player2","player3","player4","player5"])
player_score=np.array([85,92,78,90,100])
condition=player_score>90
top_players=player_name[np.where(condition)]
# print(top_players)

# Write a function incrment_salary that takes salary_array and returns increased salary.
# Hike Rule: <1000 => 20%, 1000-5000 => 10%, >5000 => 5%. 
# (use: np.select)
# Write a function categorize_age that takes age_array 
# and categorizes it as Child, Teen, Adult, Senior depending on age range. 
# (use: np.select)
# Assign temp_data as [15, 22, 30, 5, 18, 25].
# Generate new array temp_category that has elements below_avg and above_avg. 
# (use: np.where)
# Assign player_name as ["Player1", "Player2", "Player3", "Player4"],
# player_score as [85, 92, 78, 90]. 
# Find the name of players with score above 90 and store as top_players.