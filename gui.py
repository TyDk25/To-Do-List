
import PySimpleGUI as gi

label = gi.Text("Type in a to-do")
input_box = gi.InputText(tooltip="Enter todo")
add_button = gi.Button("Add")

window = gi.Window('My To-do List', layout=[[label], [input_box, add_button]])
window.read()