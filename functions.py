def get_todos():
    """
    Read a text file and return the list of to-do items
    """
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def append_todos(todo):
    """
    Append a new to-do item to the end of the file.

    Parameters:
        todo (str): The new to-do item to be appended.
    
    Returns:
        str: The added to-do item.
    """
    with open('todos.txt', 'a') as file:
        file.write(todo)
    return todo

def write_todo(todo):
    """
    Write a new to-do item to the file, replacing its contents.

    Parameters:
        todo (str): The new to-do item to be written.
    """
    with open('todos.txt', 'w') as file:
        file.writelines(todo)
