
import threading
import time
import tkinter as tk

def demo():
    root = tk.Tk()
    frame = tk.Frame(root)
    root.title("menu")
    frame.pack()
    closemenubutton = tk.Button(frame,
                                    text="close menu",
                                    command=root.destroy)
    closemenubutton.pack(side=tk.RIGHT)
    root.mainloop()

#thread 1
def main1():
    
    #thread 2
    threading.Thread(target=demo).start()
    
    #thread 1
    while True:
        time.sleep(3)
        print("thread",threadnum," running")

if __name__ == '__main__':
    main1()