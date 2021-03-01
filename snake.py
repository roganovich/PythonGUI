from tkinter import *
from PIL import Image, ImageTk
import random

WIDTH = 1000
HEIGHT = 1000
BODYSIZE = 50
START_DELAY = 200
MIN_DELAY= 100;
STEP_DELAY=10
LENGHT = 3


countBodyW = WIDTH / BODYSIZE
countBodyH = HEIGHT / BODYSIZE




class Snake(Canvas):
    x = False
    y = False
    headImage = False
    bodyImage = False
    appleImage = False
    head = False
    body = False
    apple = False
    delay = 0
    direction = "Right"
    directionTmp = "Right"
    loss = False

    def __init__(self):
        Canvas.__init__(self, width=WIDTH, height=HEIGHT, background="gray")
        self.focus_get()
        self.bind_all("<Key>", self.onKeyPressed)
        self.loadResourses()
        self.beginPlay()
        self.pack()

    def onKeyPressed(self, event):
        key = event.keysym;
        if key == "Left" and self.direction != "Right":
            self.directionTmp = "Left"
        if key == "Right" and self.direction != "Left":
            self.directionTmp = "Right"
        if key == "Up" and self.direction != "Down":
            self.directionTmp = "Up"
        if key == "Down" and self.direction != "Up":
            self.directionTmp = "Down"
        if key == "space" and self.loss:
            self.beginPlay()
        if key == "r":
            self.loss = True

    def updateDirection(self):
        self.direction = self.directionTmp
        head = self.find_withtag("head")
        head_x, head_y = self.coords(head)
        self.delete(head)
        if self.direction == "Left":
            self.head = ImageTk.PhotoImage(self.headImage.transpose(Image.FLIP_LEFT_RIGHT).resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        else:
            rotates = {"Right":0, "Up":90, "Down":-90}
            self.head = ImageTk.PhotoImage(self.headImage.rotate(rotates[self.direction]).resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.create_image(head_x, head_y, image=self.head, anchor="nw", tag="head")

    def loadResourses(self):
        self.headImage = Image.open("./images/head.png")
        self.bodyImage = Image.open("./images/body.png")
        self.appleImage = Image.open("./images/apple.png")

        self.head = ImageTk.PhotoImage(self.headImage.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.body = ImageTk.PhotoImage(self.bodyImage.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))
        self.apple = ImageTk.PhotoImage(self.appleImage.resize((BODYSIZE, BODYSIZE), Image.ANTIALIAS))

    def beginPlay(self):
        self.delay = START_DELAY
        self.direction = "Right"
        self.directionTmp = "Right"
        self.loss = False
        self.delete(ALL)
        self.x = [0] * int(countBodyW)
        self.y = [0] * int(countBodyH)

        self.spawnActors()
        self.after(self.delay, self.timer)

    def timer(self):
        self.checkCollisions()
        print(self.loss)
        if not self.loss:
            self.checkApple()
            self.updateDirection()
            self.moveSnake()
            self.after(self.delay, self.timer)
        else:
            self.gameOver()

    def moveSnake(self):
        head = self.find_withtag("head")
        body = self.find_withtag("body")
        items = body + head
        for i in range(len(items) - 1):
            current_xy = self.coords(items[i])
            next_xy =  self.coords(items[i + 1])
            self.move(items[i], next_xy[0] - current_xy[0], next_xy[1] - current_xy[1])

        if self.direction == "Left":
            self.move(head, -BODYSIZE, 0)
        elif self.direction == "Right":
            self.move(head, BODYSIZE, 0)
        elif self.direction == "Up":
            self.move(head, 0, -BODYSIZE)
        elif self.direction == "Down":
            self.move(head, 0, BODYSIZE)

    def spawnActors(self):
        self.spawnApple()

        self.x[0] = int(countBodyW / 2) * BODYSIZE
        self.y[0] = int(countBodyH / 2) * BODYSIZE

        for i in range(1, LENGHT):
            self.x[i] = self.x[0] - BODYSIZE * i
            self.y[i] = self.y[0]

        self.create_image(self.x[0], self.y[0], image=self.head, anchor="nw", tag="head")
        for i in range(LENGHT - 1, 0,-1):
            self.create_image(self.x[i], self.y[i], image=self.body, anchor="nw", tag="body")


    def spawnApple(self):
        apple = self.find_withtag("apple")
        if apple:
            self.delete(apple[0])
        rx = random.randint(0, countBodyW - 1)
        ry = random.randint(0, countBodyH - 1)
        self.create_image(rx * BODYSIZE, ry * BODYSIZE, image = self.apple, anchor = "nw", tag="apple")

    def checkApple(self):
        apple = self.find_withtag("apple")[0]
        head = self.find_withtag("head")[0]
        body = self.find_withtag("body")[-1]

        x1, y1, x2, y2 = self.bbox(head)
        overlaps = self.find_overlapping(x1, y1, x2, y2)
        for actor in overlaps:
            if actor == apple:
                temp_x, temp_y = self.coords(body)

                self.spawnApple()
                self.create_image(temp_x, temp_y, image = self.body, anchor = "nw", tag="body")
                if self.delay > MIN_DELAY:
                    self.delay -= STEP_DELAY

    def checkCollisions(self):
        head = self.find_withtag("head")
        body = self.find_withtag("body")
        x1, y1, x2, y2 = self.bbox(head)
        overlaps = self.find_overlapping(x1, y1, x2, y2)
        for b in body:
            for actor in overlaps:
                if actor == b:
                    self.loss = True

        if x1 < 0:
            self.loss = True
        if x2 > WIDTH:
            self.loss = True
        if y1 < 0:
            self.loss = True
        if y2 > HEIGHT:
            self.loss = True

    def gameOver(self):
        body = self.find_withtag("body")
        self.delete(ALL)
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2 -60, text="GAME OVER", fill="white", font="Robo 40", tag="text1")
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2 +60, text="Press SPACE to Continue...", fill="white",
                         font="Robo 40", tag="text1")
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2 , text="Snake level: " + str(len(body)),
                         fill="white",
                         font="Robo 40", tag="text1")
root = Tk()
root.title("Игра Змейка")

root.board = Snake()

root.resizable(False, False)
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenmmwidth()
hs = root.winfo_screenheight()
# x = int(user_screen_width / 2 - w / 2)
x = int(ws)
y = int(hs / 5.5 - h)
geometrystring = "+{0}+{1}".format( x, y);
root.geometry(geometrystring)
root.mainloop()