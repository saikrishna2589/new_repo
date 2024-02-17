import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

st.title("Weather Forecast in the short-term ")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted")

option = st.selectbox("Select data to view",
                      ("Temperature", "Weather"))
st.subheader(f"{option} for next {days} days in {place}")


def get_data(days):
    dates =  ["2022-25-10", "2022-06-10", "2022-27-10"]
    temperature = [10, 11, 33]
    temperature = [days * i for i in temperature]
    return dates, temperature

dates, temperatures = get_data(days)

# Create a DataFrame from the data
data = pd.DataFrame({"Date": dates, "Temperature": temperatures})

# Create a line plot using Plotly Express
fig = px.line(data, x="Date", y="Temperature", title=f"{option} for next {days} days in {place}")

# Show the Plotly figure using Streamlit
st.plotly_chart(fig)