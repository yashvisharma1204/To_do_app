todos=[]
while True:
    user_action= input("Type add,show,edit,complete or exit: ")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            todo=input("Enter a todo: ") + '\n'
            file = open('todos.txt','r')
            todos=file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
           file = open('todos.txt','r')
           todos=file.readlines()
           file.close()
           for i,item in enumerate(todos):
               print(f'{i+1}. {item}')
        case 'edit':
            number=int(input('Number of the todo to edit: '))
            number=number-1
            new=input("Enter your new todo: ")
            todos[number]=new
        case 'complete':
            number=int(input("Enter a number you completed: "))
            todos.pop(number-1)
        case 'exit':
            break
print("Bye!")
