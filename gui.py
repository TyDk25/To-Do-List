import functions 
import PySimpleGUI as gi

label = gi.Text("Type in a to-do")
input_box = gi.InputText(tooltip="Enter todo", key="todo")
add_button = gi.Button("Add")
list_box = gi.Listbox(values=functions.get_todos(), key='todos', 
                      enable_events=True, size =[45, 10])

edit_button = gi.Button("Edit")

window = gi.Window('My To-do List', 
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos= functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
        
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gi.WIN_CLOSED:
        
                break   
                
window.close()



