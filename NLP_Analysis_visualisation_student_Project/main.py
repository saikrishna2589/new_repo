
import glob  #for reading file paths
import streamlit as st
import plotly.express as px #for graphs on streamlit


from nltk.sentiment import SentimentIntensityAnalyzer

#Instantiate the SentimentIntensityAnalyser class
analyser=SentimentIntensityAnalyzer()

#Define the pattern to match all .txt files in diary directory
file_pattern="diary/*.txt"

#Use glob to get a list of all matching files
file_list= glob.glob(file_pattern)

#sorting files in correct order
file_list=sorted(file_list)


#prepare 2 empty lists for storing negativity and positivity coefficients
negativity=[]
positivity=[]


for file_path in file_list:
    with open(file_path,'r') as file:
        each_file=file.read()
    scores=analyser.polarity_scores(each_file)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

print(scores)


dates=[date_info.strip('./txt').strip("diary/") for date_info in file_list]


#streamlit
st.title("Diary Tone")
st.subheader("Positivity")
pos_figure=px.line(x=dates,y=positivity,labels={"x":"Date","y":"positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure=px.line(x=dates,y=negativity,labels={"x":"Date","y":"negativity"})
st.plotly_chart(neg_figure)