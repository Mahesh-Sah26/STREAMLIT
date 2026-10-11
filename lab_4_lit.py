import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Quality checker")
st.write("We check and provide data quality of your input file")


col_1,col_2,col_3=st.columns(3)
file_type=col_2.pills("Choose you file type",['Excel','CSV'])
file_path=col_1.file_uploader("Upload your file")

if file_type=="CSV":
    sep=col_3.radio("Choose your seperator",['\\t',',','|'],horizontal=True)

if file_path:
    if file_type=='Excel':

        df=pd.read_excel(file_path)
    elif file_type=="CSV":
        df=pd.read_csv(file_path)

    st.write("**sample data**")
    st.dataframe(df)
    st.write("**Data Types:**")
    st.dataframe(df.dtypes)

    st.write("** Missing Data**")
    fig,ax=plt.subplots()
    missing_data=df.isna().sum()
    missing_data.plot()
    missing_only=missing_data[missing_data>0]
    missing_only.plot(kind='bar')
    # missing_data.plot(kind='bar')
    st.pyplot(fig)
    # st.write(missing_data.columns)
    # sns.barplot(data=missing_data,)

    # Create a drop down to choose chart type
    # Create another drop down to choose x-axis
    # Create another drop down to choose y-axis
    # make the plot according to inputs from three width

    column_names=df.columns.to_list()
    col_1,col_2,col_3=st.columns(3)

    chart_type=col_1.selectbox("Choose chart type you want to show: ",['line','bar','scatter'])
    x_col=col_2.selectbox("Choose X-axis",column_names)
    y_col=col_3.selectbox("Choose Y-axis",column_names)

    fig,ax=plt.subplots()
    if chart_type=='line':
        sns.lineplot(data=df,x=x_col,y=y_col)
    elif chart_type=='bar':
        sns.barplot(data=df,x=x_col,y=y_col)

    else:
        sns.scatterplotplot(data=df,x=x_col,y=y_col)
    st.pyplot(fig)

