# 📝 To-Do App

A simple to-do application with a graphical user interface (GUI) built using `tkinter`. This app allows you to add, update, and complete tasks. The tasks are stored in a text file (`todos.txt`), so your to-do list persists between sessions.

## Features

- ➕ Add new to-do items
- ✏️ Update existing to-do items
- ✅ Mark to-do items as completed
- 📋 List and view all to-do items

## File Structure

- `app.py`: Main application code including the GUI and user interactions.
- `functions.py`: Helper functions for reading, writing, and updating the to-do list stored in `todos.txt`.
- `todos.txt`: Text file to store the to-do items.

## `functions.py`

Contains the following functions:

- `get_todos()`: Reads the `todos.txt` file and returns a list of to-do items.
- `append_todos(todo)`: Appends a new to-do item to the end of the `todos.txt` file.
- `write_todo()`: Writes a list of to-do items to the `todos.txt` file, replacing its contents.

## `app.py`

Main application logic including the GUI setup and user interaction functions.

### GUI Setup

The GUI is created using `tkinter`. It includes a main window, text entry for to-dos, listbox to display to-dos, and buttons for various actions.

### Button Functions

- `add_todo()`: Adds a new to-do item and updates the listbox.
- `update_todo()`: Updates the selected to-do item.
- `complete_todo()`: Marks a to-do item as completed by removing it from the list.
- `write_todos()`: Writes the current state of the listbox to the `todos.txt` file.
- `update_todos()`: Updates the listbox with the current to-do items.

### Run the Application

The application is run using `tkinter`'s `mainloop()` function.

## Command-Line Interface (CLI) Interaction

For those who prefer a command-line interface, a basic CLI is included to add, show, edit, complete, and exit the to-do application.

