import tkinter as tk
from tkinter import messagebox

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    title = title_entry.get()
    description = description_entry.get()
    if title and description:
        task = {
            'id': len(tasks) + 1,
            'title': title,
            'description': description,
            'status': 'Not Completed'
        }
        tasks.append(task)
        save_tasks()
        update_task_list()
        title_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both title and description.")

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, f"{task['id']}. {task['title']} - {task['status']}")

def view_task(event):
    selected_task = task_list.curselection()
    if selected_task:
        task = tasks[selected_task[0]]
        title_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        title_entry.insert(0, task['title'])
        description_entry.insert(0, task['description'])

def update_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_id = tasks[selected_task[0]]['id']
        title = title_entry.get()
        description = description_entry.get()
        for task in tasks:
            if task['id'] == task_id:
                task['title'] = title
                task['description'] = description
                break
        save_tasks()
        update_task_list()

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_id = tasks[selected_task[0]]['id']
        global task
        tasks = [task for task in tasks if task['id'] != task_id]
        save_tasks()
        update_task_list()

def mark_task_completed():
    selected_task = task_list.curselection()
    if selected_task:
        task_id = tasks[selected_task[0]]['id']
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = 'Completed'
                break
        save_tasks()
        update_task_list()

# GUI setup
root = tk.Tk()
root.title("To-Do List Application")

frame = tk.Frame(root)
frame.pack(pady=10)

title_label = tk.Label(frame, text="Task Title:")
title_label.grid(row=0, column=0, padx=5, pady=5)
title_entry = tk.Entry(frame, width=40)
title_entry.grid(row=0, column=1, padx=5, pady=5)

description_label = tk.Label(frame, text="Task Description:")
description_label.grid(row=1, column=0, padx=5, pady=5)
description_entry = tk.Entry(frame, width=40)
description_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

task_list = tk.Listbox(root, width=80, height=10)
task_list.pack(pady=10)
task_list.bind("<<ListboxSelect>>", view_task)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_task_completed)
mark_completed_button.pack(side=tk.LEFT, padx=10)

load_tasks()
update_task_list()

root.mainloop()
