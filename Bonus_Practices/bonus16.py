import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button = sg.FilesBrowse('Choose')

label2 = sg.Text("Select folder destination: ")
input2 = sg.Input()
choose_folder_button = sg.FolderBrowse('Choose')

compress_button = sg.Button('Compress')

window = sg.Window("File Compressor", layout=[
    [label1, input1, choose_button],
    [label2, input2, choose_folder_button],
    [compress_button]])

window.read()
window.close()