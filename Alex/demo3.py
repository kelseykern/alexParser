from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as ET

root = Tk()

def Readstatus(key):
    print(var.get(key))

listTree = ET.parse('test.xml')
listRoot = listTree.getroot()

var = dict()
count=1
for child in listRoot:
    var[child]=IntVar()
    chk = Checkbutton(root, text='Text'+str(count), variable=var[child], 
                      command=lambda key=child: Readstatus(key))
    count += 1
    chk.pack()

root.mainloop()