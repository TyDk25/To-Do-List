user_prompt = "Enter a todo:"


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + "\n"

                # READS FILE
        file = open('todos.txt', 'r')

                # RETURNS A LIST

        with open('todos.txt', 'r') as file:
                    todos = file.readlines()

        todos.append(todo)

                # OPENS AND OVERWRITES EXISTING FILE
        with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
    elif 'show' in user_action:
         with open('todos.txt', 'r') as file:
            todos = file.readlines()

            for index, item in enumerate(todos):
             item = item.strip('\n')
             row = f"{index + 1}-{item}"
             print(row)


    elif 'edit' in user_action:
        number =int((user_action[5:]))
        print(number)
        number = number - 1
            
        with open('todos.txt', 'r') as file:
                todos = file.readlines()
                
            
           
        new_todo = input("Enter new todo:")
        todos[number] = new_todo + ' \n '
      
            
        with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
    elif 'complete' in user_action:
                number = int(user_action[9:])
                with open('todos.txt', 'r') as file:
                        todos = file.readlines()
                        index = number - 1
                        todo_to_remove = todos[index].strip('\n')
                        todos.pop(index)
                        with open('todos.txt', 'w') as file:
                                file.writelines(todos)
            
    elif 'exit' in user_action:
            break
    
    else: 
        print("This command is not valid.")

        
print("Bye!")
    