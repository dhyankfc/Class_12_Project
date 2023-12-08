from tkinter import *

def Instructions():
    
    root=Tk()
    root.geometry="600x900"
    canvas = Canvas(root, width = 780, height=520, bg = '#2f2f2f')
    canvas.grid(row=0, column=0)
    canvas.pack()
    File = open(r".\text files\Instr.txt")
    str = File.read()
    File.close()
    
    canvas_text = canvas.create_text(10, 10, text='',font=("Lato",15,'bold'),fill="#fa7223", anchor=NW)
    delta = 5 
    delay = 0
    for i in range(len(str) + 1):
        s = str[:i]
        update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
        canvas.after(delay, update_text)
        delay += delta
    