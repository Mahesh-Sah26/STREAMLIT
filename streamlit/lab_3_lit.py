import streamlit as st
import pandas as pd

st.title("Data Quality checker")
st.write("We check and provide data quality of your input file")

file_type=st.pills("Choose you file type",['Excel','CSV'])
file_path=st.file_uploader("Upload your file")
if file_path:
    if file_type=='Excel':

        df=pd.read_excel(file_path)
    elif file_type=="CSV":
        df=pd.read_csv(file_path)
    st.dataframe(df)



