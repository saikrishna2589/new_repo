import streamlit as st

# Custom CSS to inject into the Streamlit app to set the background to white



st.title("Weather Forecast in the short-term ")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted")

option = st.selectbox("Select data to view",
                      ("Temperature", "Weather"))
st.subheader(f"{option} for next {days} days in {place}")
