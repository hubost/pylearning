user_prompt = "Enter a todo:"
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)
# [] - python list
todos = [todo1,todo2,todo3,"Hello"]
print(todos)
print("typ danych:",type(user_prompt))
print("typ danych:",type(todos))
print("typ danych:",type(todo1))

# prompt type: string, todos type: list, todo1 type: string

# both '' and "" can be used but '' can be more confusing (example: ' don't '

# wide space doesn't matter in python (example: todo=2 and todo = 2)

#one declaration in one line

#python console is used for throwaway-code that u want to test

####### 
user_prompt = "Enter a todo: "
todos = []
count = 0
while count < 3:
    todo = input(user_prompt)
    todos.append(todo.capitalize())
    print(todos)
    count = count+1

# for, while, do while, if, - loops

#append - add element to list
#capitalize - first letter uppercase
#title - all first letters uppercase  todos.append(todo.title())


##methods - powtórzyć, arguments - powtórzyć

password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")
print("Correct password")
####

name = input("What is your name? ")
while True:
    print(name.capitalize())
#####
x = 0
while x<5:
    name = input("Insert your name: ")
    name_upper = name.capitalize()
    print(name_upper)
    x = x+1


### list of all functions (in console) import builtins , dir (builtins)
# user_action = user_action.strip() - usuwa spacje

while True:
    user_action = input("Type add or show: ")
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

rate = 2
amount = input("Input dollar amount")
calculate = rate * float(amount)
print(calculate)

ranking = ['John', 'Sen', 'Lisa']
rank = int(input("Enter rank number: ")) - 1
name = ranking[rank]

print(name)
##tugles
color_codes = ((1,2,3),(4,5,6),(7,8,9))
##print 3rd
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

#add string to list

seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)

country = "India"

match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")

members = ["john smith", "sen plakay", "dora ngacely"]

for item in members:
    print(item.title())