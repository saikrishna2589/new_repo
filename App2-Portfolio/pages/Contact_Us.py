import streamlit as st
from send_email import send_email

st.header("Contact Me")


# other components are going to be contained with st.form .therefore we use with context
#within st.form method, we will have components and this can be built by using 'with'
#this is similar to with col1 we used in Home.py . within col1 , we have components

with st.form(key="email_forms"):
   user_email=st.text_input("Your email address")
   user_message=st.text_area("Your message")
   message= f"""\
Subject:New email from {user_email}

From: {user_email}
{user_message}

"""
   button = st.form_submit_button("Submit")

   if button:
       send_email(message)
       st.info("Your email was sent successfully")

