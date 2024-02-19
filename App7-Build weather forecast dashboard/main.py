import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data

st.set_page_config(layout="wide")

st.title("Weather Forecast in the short-term ")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted")

option = st.selectbox("Select data to view",
                      ("Temperature", "Weather"))
st.subheader(f"{option} for next {days} days in {place}")


data=get_data(place,days,options)



# Create a line plot using Plotly Express
fig = px.line(data, x="Date", y="Temperature", title=f"{option} for next {days} days in {place}")

# Show the Plotly figure using Streamlit
st.plotly_chart(fig)
