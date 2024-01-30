import streamlit as st
import pandas as pd

# this is to set configuration of streamlit page on website exto increase container size to fit text etc
st.set_page_config(layout="wide")
st.title("The Best Company ")

content = """
The company is great at blahblahblah.we have some many top clients, top investors, blah blah and more blah.
The company is great at blahblahblah.we have some many top clients, top investors, blah blah and more blah.
The company is great at blahblahblah.we have some many top clients, top investors, blah blah and more blah.
"""

st.write(content)

st.subheader("Our Team")

# this method 'columns' of st module will return 5 column objects. we assign we object to a variable
col1, empty_col, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

# reading the data
df = pd.read_csv("My homework projects/company_website_data.csv", sep=',')

print(df)


# custom function to make the name title case
def convert_to_title_case(name):
    return name.title()


# then using custom function here on first name and last name.

#iterate over 0 to 3 rows in first col. then 4 to 7 in col2 and 8 to 12 in col3
with (col1):
    for index, row in df[:4].iterrows():
        first_name = convert_to_title_case(row["first name"])
        last_name = convert_to_title_case(row["last name"])

        full_name = f"{first_name} {last_name}"
        st.subheader(full_name)
        st.write(row["role"])
        st.image("My homework projects/company_website_images/" + row["image"])

with (col2):
    for index, row in df[4:8].iterrows():
        first_name = convert_to_title_case(row["first name"])
        last_name = convert_to_title_case(row["last name"])

        full_name = f"{first_name} {last_name}"
        st.subheader(full_name)
        st.write(row["role"])
        st.image("My homework projects/company_website_images/" + row["image"])

with (col3):
    for index, row in df[8:].iterrows():
        first_name = convert_to_title_case(row["first name"])
        last_name = convert_to_title_case(row["last name"])

        full_name = f"{first_name} {last_name}"
        st.subheader(full_name)
        st.write(row["role"])
        st.image("My homework projects/company_website_images/" + row["image"])
