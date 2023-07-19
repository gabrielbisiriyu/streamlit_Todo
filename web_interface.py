import streamlit as st 
import functions 

todos=functions.get_todo() 
def add_todo():
    to=st.session_state["new_todo"]+'\n'
    todos.append(to) 
    functions.write_todos(todos) 
    st.success("New todo added")  

    

st.title("MY Todo App") 
st.subheader("This is my Todo app") 
st.write("To increase your productivity. i no understand sha") 

n=0
for index,todo in enumerate(todos):
    n=n+1
    checkbox=st.checkbox(todo,key=n)  
    if checkbox:
        todos.pop(index) 
        functions.write_todos(todos) 
        del st.session_state[n]
        #st.experimental_rerun()
        st._rerun()
#li = [st.checkbox(todo,key=todo) for todo in todos] 

st.text_input(label="add",placeholder="Add a todo here",label_visibility="hidden",
on_change=add_todo,key="new_todo")  
# label_visibility MAKES THE label TO BE  VISIBLE
#DEFAULT label_visibility IS SET TO VISIBLE 
# HERE WE DECIDED TO HIDE THE LABEL 



