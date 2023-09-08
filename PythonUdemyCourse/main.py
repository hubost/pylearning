todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1} . {item}"
                print(row)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1
            newtodo = input("Input new value: ")
            todos[number] = newtodo
        case 'complete':
            number = int(input("Number of todo to complete: "))
            todos.pop(number - 1)
        case whatever:
            print("Wrong typing.")

print("Exit...")
