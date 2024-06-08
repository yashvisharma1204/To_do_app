todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()
    
    if user_action.startswith('add'):
        todo = input("Enter a todo: ") + '\n'
        with open('todos.txt', 'a') as file:
            file.write(todo)

    elif user_action.startswith('show'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        for i, item in enumerate(todos):
            item = item.strip()
            print(f'{i+1}. {item}')

    elif user_action.startswith('edit'):
        number = int(input('Number of the todo to edit: '))
        number -= 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        print("Here are the existing todos:")
        for i, item in enumerate(todos, 1):
            print(f'{i}. {item}', end='')
        new_todo = input("\nEnter your new todo: ") + '\n'
        todos[number] = new_todo
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('complete'):
        number = int(input("Enter the number of the completed todo: "))
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        to_remove = todos.pop(number - 1)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        print(f"Todo '{to_remove.strip()}' has been removed from the list.")
    elif user_action.startswith('exit'):
        break

print("Bye!")
