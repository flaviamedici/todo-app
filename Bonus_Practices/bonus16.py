import FreeSimpleGUI as sg
from zip_creator import make_archive


label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button = sg.FilesBrowse('Choose', key='files')

label2 = sg.Text("Select folder destination: ")
input2 = sg.Input()
choose_folder_button = sg.FolderBrowse('Choose', key='folder')

compress_button = sg.Button('Compress')
message = sg.Text(key="output")

window = sg.Window("File Compressor", layout=[
    [label1, input1, choose_button],
    [label2, input2, choose_folder_button],
    [compress_button, message]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    window['output'].update(value='Compression completed!')

window.close()