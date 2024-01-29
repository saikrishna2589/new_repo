import pandas as pd
import streamlit as st
from send_email import email_send

# reading the file and converting to a list
topics = pd.read_csv("../topics.csv")["topic"].tolist()
print(topics)

# creating the content on contact page
with st.form(key="email_form"):
    customer_email = st.text_input("Your Email Address")

    topic_of_interest = st.selectbox("What topic do you want to discuss?", options=topics)

    customer_message = st.text_area("Text")

    final_message = f"""
    Subject: New message from {customer_email}
    
    From: {customer_email}
    Topic: {topic_of_interest}
    message : {customer_message}
    """
    button = st.form_submit_button("Submit")

    if button:
        email_send(final_message)
        st.info("Your message was successfully sent! :) Be happy now")
