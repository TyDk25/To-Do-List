import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
user_prompt = "Enter a todo:"


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):   
        todo = user_action[4:] + "\n"

        # READS FILE
        file = open('todos.txt', 'r')

        # RETURNS A LIST

        todos =functions.get_todos()

        todos.append(todo)

        # OPENS AND OVERWRITES EXISTING FILE
        functions.write_todos(todos)
    
    elif user_action.startswith("show"):

        todos = functions.get_todos()
        

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int((user_action[5:]))
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + ' \n '

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("Your number does not exist")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Your number does not exist")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("This command is not valid.")


print("Bye!")
