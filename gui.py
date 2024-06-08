import tkinter as tk
from tkinter import ttk, messagebox
from functions import get_todos, append_todos, write_todo

def add_todo():
    todo_text = todo_entry.get("1.0", tk.END).strip()
    if todo_text:
        append_todos(todo_text + '\n')
        update_todos()
        todo_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a to-do item")

def update_todo():
    selected_index = todo_listbox.curselection()
    if selected_index:
        new_todo_text = todo_entry.get("1.0", tk.END).strip()
        if new_todo_text:
            todos = get_todos()
            index = selected_index[0]
            todos[index] = new_todo_text + '\n'
            write_todo(todos)
            update_todos()
        else:
            messagebox.showwarning("Warning", "Please enter a to-do item to update")
    else:
        messagebox.showwarning("Warning", "Please select a to-do item to update")

def complete_todo():
    selected_index = todo_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        todos = get_todos()
        completed_todo = todos.pop(index)
        write_todo(todos)
        update_todos()
        messagebox.showinfo("Completed", f"To-do item '{completed_todo.strip()}' has been completed.")
    else:
        messagebox.showwarning("Warning", "Please select a to-do item to complete")

def write_todos():
    todos = [todo.strip() + '\n' for todo in todo_listbox.get(0, tk.END)]
    write_todo(todos)

def update_todos():
    todos = get_todos()
    todo_listbox.delete(0, tk.END)
    for i, todo in enumerate(todos, 1):
        todo_listbox.insert(tk.END, f'{i}. {todo.strip()}')

# Create main window
root = tk.Tk()
root.title("To-Do App")
root.configure(bg="Medium Purple")  # Set background color

# Todo entry
todo_entry = tk.Text(root, width=40, height=5)
todo_entry.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

# Label above writing box
write_label = tk.Label(root, text="Write your new task", font=("Monospace", 12, "bold"), fg="white", bg="Medium Purple")
write_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nw")

# Add Todo button
add_button = ttk.Button(root, text="Add Todo", command=add_todo, width=20, style="C.TButton")
add_button.grid(row=1, column=1, padx=(0, 10), pady=5, sticky="ne")

# Update Todo button
update_button = ttk.Button(root, text="Update Todo", command=update_todo, width=20, style="C.TButton")
update_button.grid(row=2, column=1, padx=(0, 10), pady=5, sticky="ne")

# Configure row to stretch
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

# Complete Todo button
complete_button = ttk.Button(root, text="Complete", command=complete_todo, width=20, style="C.TButton")
complete_button.grid(row=3, column=1, padx=(0, 10), pady=5, sticky="ne")

# Write button
write_button = ttk.Button(root, text="Write", command=write_todos, width=20, style="C.TButton")
write_button.grid(row=4, column=1, padx=(0, 10), pady=5, sticky="ne")

# Todo list
todo_listbox = tk.Listbox(root, width=50)
todo_listbox.grid(row=2, column=0, rowspan=3, padx=10, pady=10, sticky="ns")

# Initial update of todos
update_todos()

# Configure ttk Style
style = ttk.Style()
style.configure("C.TButton", foreground="black", background="#7289da", borderwidth=0, font=("Helvetica", 10))
# Add simple shadow effect using border color
style.map("C.TButton", background=[('active', "#5f73b7")], bordercolor=[('active', "#4f5f77")])

# Run the application
root.mainloop()
