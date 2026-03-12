import FreeSimpleGUI as sg

label1 = sg.Text("Enter Feet: ")
input1 = sg.Input()

label2 = sg.Text("Enter inches: ")
input2 = sg.Input()

convert_button = sg.Button('Convert')
message = sg.Text(key="output")

window = sg.Window("File Compressor", layout=[
    [label1, input1],
    [label2, input2],
    [convert_button, message]])

while True:
    event, values = window.read()
    print(event, values)
    feet = float(values[0])
    inches = float(values[1])
    result = feet * 0.3048 + inches * 0.0254
    window['output'].update(value=f"{result} m")

window.close()