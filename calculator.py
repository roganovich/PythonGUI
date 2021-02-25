from tkinter import *
buttons = (
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+'),
)

start = True
lastcomand = "="
result = 0

def clickkey(event):
    global start
    global lastcomand
    global info
    text = event.widget.cget("text")
    print(text)
    if(text.isdigit() or text == '.'):
        if(start):
            info.configure(text='')
            start = False
        if(text != '.' or info.cget('text').find('.') == -1):
            info.configure(text = (info.cget('text') + text) )
    else:
        if(start):
            lastcomand = text
        else:
            calculate(float(info.cget('text')))
            lastcomand = text
            start = True

def calculate(x):
    global lastcomand
    global info
    global result
    if(lastcomand == '+'):
        result += x
    elif (lastcomand == '-'):
        result -= x
    elif (lastcomand == '*'):
        result *= x
    elif (lastcomand == '/'):
        try:
            result /= x
        except ZeroDivisionError:
            pass
    elif (lastcomand == '='):
        result = x
    info.configure(text=result)

root = Tk()
root.title("Простой калькулятор")

root.resizable(False, False)


w = root.winfo_reqwidth()
h = root.winfo_reqheight()

ws = root.winfo_screenmmwidth()
hs = root.winfo_screenheight()
# x = int(user_screen_width / 2 - w / 2)
x = int(ws)
y = int(hs / 2 - h)

geometrystring = "+{0}+{1}".format( x, y);

root.geometry(geometrystring)

info = Label(root, text="0", font="Tahoma 20", bd=10 )
info.grid(row=0, column=0, columnspan=4)

for row in range(4):
    for column in range(4):
        button = Button(root, text = buttons[row][column], font="Tahoma 20", width="7")
        button.grid(row = row+1, column=column, padx =5, pady=5, ipady=20, sticky="nsew")
        button.bind('<Button-1>', clickkey)


root.mainloop()