import streamlit as st
import pandas as pd
st.title('Student Enrollment')
st.write('Enter your details')
name=st.text_input("Enter your name",placeholder='enter your name')
age=st.number_input("Enter your age",step=1,min_value=1,max_value=100)
date=st.date_input("Enter your preffered date for joining")
gender=st.radio("Choose your gender",["Male","Female","Other"],horizontal=True)

photo=st.file_uploader("Upload your photo",type=['jpg','jpeg','png','pdf'])

agree=st.checkbox("I agree to fees details")
course=st.selectbox("Choose course to enroll",['science','management','law'])
optional_subject=st.multiselect("choose optional subjects",['python','c++','c','Javascript'])
submit=st.button("Submit")

if not name:
    # raise ValueError("Name is required")
    st.error("Name is mendatory")
if not photo:
    st.error("Photo is mendatory")
if not agree:
    st.error("Please agree to our terms")
    

if name and photo and agree and submit:
    user_dict={"name":name,"age":age,"gender":[gender],"preferred_course":course,"Optioal_course":optional_subject}
    df=pd.DataFrame(user_dict)
    st.write(f"Hello {name}. You are {age} years old and you want to join on {date}")
    st.image(photo)
    st.write(f'You choose {optional_subject} as optional subject')
    st.write(df)




