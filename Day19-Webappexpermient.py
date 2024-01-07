# streamlit library is good for creating webapps
# it also integrates well with graphs. so we can create data dashboards,graphs and widgets like sliders, textboxes
# buttons. it is also easy to deploy apps to public using streamlit

# to run the streamlit app,yu need to run from terminal
# streamlit run C:\Users\saikr\Documents\pycharm projects\Day Classes\Day19-Webapps GUI.py [ARGUMENTS]
# Set the background color at the start of your app
import streamlit as st
from modules import Functions

# getting list of todos and storing in a variable
todos = Functions.get_todo_list()

# the below is a medthod to configure the page width and height
st.set_page_config(layout="wide")
# creating a custom function that is used in st.text_input(
# on_change=add_todo) parameter.
# this parameter helps webapp interact with user entries on the app

# Add feature
def add_todo():
    # st.session_state is the key and value associated
    # with new to-do entered in the web app.
    # so here we are calling the key 'new_todo' to get the
    # user latest entry into the text box on webapp
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    Functions.write_to_do_list(todos)


import streamlit as st

st.title("My Todo App")

st.subheader("This is my todo app.")

# the below <b> makes the word bold but since it is an html tag,
# #we give unsage_allow_html=True for it to be bold rather than literal
# <h> is for header. but we can use st.title instead as it is preferred
st.write("<h1>This app is to increase your <b>productivity</b><h1>"
         ,unsafe_allow_html=True)


st.text_input(label="Enter a to-do task: ",
              placeholder="Add a new to-do...",
              on_change=add_todo, key='new_todo')
# creating checkboxes on webapp for each todo task
# Adding a key='tod0' so it whenever we check the
# tod0 on the app, the key value changes to true from
# false. we can use this value in session state object
# to add a complete
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_to_do_list(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# creating a text box on the webapp
# on_change parameter is a callbackfunction
# callback function is nothing but a custom funtion


print("Hello")


