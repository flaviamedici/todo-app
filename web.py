import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''

st.title('My Todo app')
st.subheader('This is my todo app')
st.write('<h4>This app is to increase your <b>productivity</b></h4>',
         unsafe_allow_html=True)

st.text_input(label="",placeholder='Type a new todo',
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()




#st.session_state