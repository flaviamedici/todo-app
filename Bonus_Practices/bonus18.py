import FreeSimpleGUI as gui
from zip_extractor import extract_archive

gui.theme("Reddit")
label1 = gui.Text("Select Archive")
input1 = gui.Input()
choose_button1 = gui.FilesBrowse("Choose", key="archive")

label2 = gui.Text("Select Dest dir")
input2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose", key="folder")

extract_button = gui.Button("Extract")
output_label = gui.Text(key="output", text_color="white")

window = gui.Window("Archive Extractor",
                    layout =[[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [extract_button, output_label],])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    destdir = values["folder"]
    extract_archive(archivepath, destdir)
    window['output'].update(value="Extraction Completed")

window.close()