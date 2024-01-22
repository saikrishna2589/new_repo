import streamlit as st
import pandas as pd

# this is to set configuration of streamlit page on website exto increase container size to fit text etc
st.set_page_config(layout="wide")

# this method 'columns' of st module will return 2 column objects. we assign we object to a variable
col1, col2 = st.columns(2)

# width in below will reduce the image size on th streamlit website
# in col1 , we input image
with col1:
    st.image("images/photo.jpg", width=450)

# in column 2 we input description.using multi-line string
with col2:
    st.title("Sai Krishna Samudrala")
    content = """With over a decade of experience in data analysis, predictive analytics, and data visualization, 
    I am a Certified Data Analytics Consultant proficient in Azure, Alteryx, PowerBI, Tableau, SQL, and Python. I 
    specialize in transforming raw data into meaningful insights to help solve complex business problems and have a 
    proven track record with Fortune 500 companies like Schneider Electric and Nestlé. My goal is to deliver 
    innovative data-driven solutions that benefit both clients and society"""

    # # we can use st.write(content) as well but st.info(content) makes it looks prettier on website(background color)
    st.info(content)

# giving some space after the container above
st.write("  ")

content2 = """Below are some of the Python apps I developed.Feel free to contact me!"""
# writing text below the image object and description object
st.write(content2)

# creating 2 columns. storing each column object in a variable
col3, col4 = st.columns(2)


#using pandas to read the data file as it has the title, description, link and image of all the apps.
pd.read_csv("data.csv",sep=';')


#alternate method using with open(). but this method will read data as string and not parsed at delimiter
# Pandas instead parses the csv in a tabular format in well strucuted way
#with open("data.csv") as file:
       # content=file.read()
   
#content

df = pd.read_csv("data.csv",sep=';')

# we use df.iterrows() method to loop through each row of dataframe
# we only loop through 'title' column and write them on webpage

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])