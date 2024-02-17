import pandas as pd
import streamlit as st
import plotly.express as px

st.header("In Search for Happiness")

options=["GDP","Happiness","Generosity"]

x_axis = st.selectbox("Select the data for the X-axis",options)
y_axis = st.selectbox("Select the data for the Y-axis",options)

st.subheader(f"{x_axis} and {y_axis}")


#read data
df=pd.read_csv("happy.csv")

#create a scatter plot using Plotly Express

fig=px.scatter(df,x=str(x_axis).lower(),y=str(y_axis).lower(),labels={"x": str(x_axis) ,"y": str(y_axis)})

#show the plotly figure using streamlit
st.plotly_chart(fig)