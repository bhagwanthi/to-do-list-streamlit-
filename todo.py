# import streamlit as st
import streamlit as st

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display tasks and mark them as completed
def display_tasks(tasks):
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([0.8, 0.2])
        col1.write(task)
        if col2.button("Complete", key=f"complete_{i}"):
            tasks.pop(i)
            save_tasks(tasks)
            st.experimental_rerun()

# Load existing tasks
tasks = load_tasks()

# App title
st.title("Simple To-Do List")

# Add new task
new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        st.experimental_rerun()

# Display tasks
st.subheader("Your Tasks")
if tasks:
    display_tasks(tasks)
else:
    st.write("No tasks available.")
