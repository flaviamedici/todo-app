import functions
import FreeSimpleGUI as gui

label = gui.Text("Type a todo: ")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")

window = gui.Window('To-Do app', layout=[[label], [input_box, add_button]],
                    font="Helvetica, 20")

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)
        case gui.WIN_CLOSED:
            break



window.close()
