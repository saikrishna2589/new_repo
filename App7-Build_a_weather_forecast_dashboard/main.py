import streamlit as st
import plotly.express as px
# Custom CSS to inject into the Streamlit app to set the background to white

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
    temperature=[10,11,33]
    temperature = [days * i for i in temperature]
    return dates, temperature

d,t=get_data(days)


#x and y in the arguments needs to be arrays, for ex-list,tuple,
# dataframe column, series object etc
#labels object needs to be dictionary

#Plotly and Bokeh are figure objects that go into the input
figure=px.area(x=d, y=t)

#The above figure object needs to go inside plotly chart
st.plotly_chart(figure)
#other than line method , we have area, histogram, density heatmap, funnel, sctter
#,pie etc .you can get these methiods by checking dir
# of the plotly.express method
#print(dir(px))
