from tkinter import *

def analyze_with_filters(name, var1, var2):
    print(name, var1, var2)

def main1():
    root = Tk()

    howto_label = Label( root, text="enter path of resumes below then press button")
    howto_label.grid(row=0, sticky=W)

    path_input = Text(root, height=1, width=49)
    path_input.grid(row=1, sticky=W)


    label2 = Label( root, text="must have atleast one from each condition:")
    label2.grid(row=2, sticky=W)

    var1 = IntVar()
    check1 = Checkbutton(root, text='solid', variable=var1)
    check1.grid(row=3, sticky=W)

    var2 = IntVar()
    check2 = Checkbutton(root, text='restful', variable=var2)
    check2.grid(row=4, sticky=W)

    var3 = IntVar()
    check3 = Checkbutton(root, text='oop or object oriented', variable=var2)
    check3.grid(row=5, sticky=W)

    # create the button that gets the input and runs function
    output = Button(root, text="Run parser", 
                    command=lambda: analyze_with_filters(str(path_input.get("1.0", 'end-1c')),
                                                         var1.get(), 
                                                         var2.get()
                                                         ))
    output.grid(row=6, sticky=W)

    root.mainloop()

if __name__ == '__main__':
    main1()