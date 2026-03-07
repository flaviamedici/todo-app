import functions
import FreeSimpleGUI as gui

label = gui.Text("Type a todo: ")
input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add")

window = gui.Window('To-Do app', layout=[[label], [input_box, add_button]])
window.read()
window.close()
