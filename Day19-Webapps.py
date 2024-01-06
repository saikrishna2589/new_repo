# streamlit library is good for creating webapps
# it also integrates well wtith graphs. so we can create data dashboards,graphs and widgets like sliders, textboxes
# buttons. it is also easy to deploy apps to public using streamlit

# to run the streamlit app,yu need to run from terminal
# streamlit run C:\Users\saikr\Documents\pycharm projects\Day Classes\Day19-Webapps GUI.py [ARGUMENTS]
# Set the background color at the start of your app
import streamlit as st
from modules import Functions


#getting list of todos and storing in a variable
todos=Functions.get_todo_list()


#creating a custom function that is used in st.text_input(
# on_change=add_todo) parameter.
#this paramter helps webapp interact with user entries on the ap.
def add_todo():
    # st.session_state is the key and value assosiated
    # with new to-do entered in the web app.
    # so here we are calling the key 'new_todo' to get the
    # user latest entry into the text box on webapp
    new_todo = st.session_state["new_todo"] +"\n"
    todos.append(new_todo)
    Functions.write_to_do_list(todos)




import streamlit as st

st.title("My Todo App")

st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

#creating checkboxes on webapp for each todo task
for todo in todos:
    st.checkbox(todo)

#creating a text box on the webapp
# on_change parameter is a callbackfunction
#callback function is nothing but a custom funtion
st.text_input(label="Enter a to-do task: ",
              placeholder="Add a new to-do...",
              on_change=add_todo, key='new_todo')

print("Hello")

st.session_state