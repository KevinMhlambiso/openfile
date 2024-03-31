from tkinter import *
from tkinter import filedialog

# def click():

def opemFile():
    filepath = filedialog.askopenfilename(initialdir="",title="open yo file",filetypes=(("text file","*.txt"),("all file","*-*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()
 
windows = Tk()




button = Button(windows,command=opemFile,text='open')
button.pack()

windows.mainloop()