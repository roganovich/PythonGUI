from tkinter import *

def setDefault(root):
    root.resizable(False, False)
        #windiows widht
    w = 282
    #windows height
    h = 258

    user_screen_width = root.winfo_screenmmwidth()
    user_screen_height = root.winfo_screenheight()

    print(user_screen_width, user_screen_height)
    #x = int(user_screen_width / 2 - w / 2)
    x = int(user_screen_width)
    y =  int(user_screen_height / 2 - h / 2)

    #root.geometry("800x600+700+600")
    geometrystring = "{0}x{1}+{2}+{3}".format(w, h, x, y);

    print(geometrystring)

    root.geometry(geometrystring)

root = Tk()
root.title("Windows test 1")
setDefault(root)

def handlerClick(event):
    print(event.widget)
    event.widget.config(bg="red")

def handlerLeace(event):
    print(event.widget)
    event.widget.config(bg="white")

b1 = Button(root, text="1", bg="white", width="12", height="5")
b2 = Button(root, text="2", bg="white",  width="12", height="5")
b3 = Button(root, text="3", bg="white",  width="12", height="5")
b4 = Button(root, text="4", bg="white",  width="12", height="5")
b5 = Button(root, text="5", bg="white",  width="12", height="5")
b6 = Button(root, text="6", bg="white",  width="12", height="5")
b7 = Button(root, text="7", bg="white",  width="12", height="5")
b8 = Button(root, text="8", bg="white",  width="12", height="5")
b9 = Button(root, text="9", bg="white",  width="12", height="5")

b1.grid(row=0, column=0, padx=0, pady=0)
b2.grid(row=0, column=1, padx=0, pady=0)
b3.grid(row=0, column=2, padx=0, pady=0)
b4.grid(row=1, column=0, padx=0, pady=0)
b5.grid(row=1, column=1, padx=0, pady=0)
b6.grid(row=1, column=2, padx=0, pady=0)
b7.grid(row=2, column=0, padx=0, pady=0)
b8.grid(row=2, column=1, padx=0, pady=0)
b9.grid(row=2, column=2, padx=0, pady=0)


b1.bind("<Enter>", handlerClick)
b1.bind("<Leave>", handlerLeace)
b2.bind("<Enter>", handlerClick)
b2.bind("<Leave>", handlerLeace)
b3.bind("<Enter>", handlerClick)
b3.bind("<Leave>", handlerLeace)
b4.bind("<Enter>", handlerClick)
b4.bind("<Leave>", handlerLeace)
b5.bind("<Enter>", handlerClick)
b5.bind("<Leave>", handlerLeace)
b6.bind("<Enter>", handlerClick)
b6.bind("<Leave>", handlerLeace)
b7.bind("<Enter>", handlerClick)
b7.bind("<Leave>", handlerLeace)
b8.bind("<Enter>", handlerClick)
b8.bind("<Leave>", handlerLeace)
b9.bind("<Enter>", handlerClick)
b9.bind("<Leave>", handlerLeace)

root.mainloop()