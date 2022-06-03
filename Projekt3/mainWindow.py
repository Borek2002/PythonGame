from tkinter import *
from world import World

from Projekt3.point import Point


class MainWindow(Frame):

    SCALE = 50
    HEIGHT = 700
    WIDTH = 1300


    def __init__(self):
        print("Okienczko")
        self.world = None
        self.screenBoard = None
        self.canvas = None
        self.text = None
        self.sccrollBar = None
        self.window=None
        self.sscale = 50


    def addWindow(self):
        self.window = Tk()
        self.window.geometry("1300x750")
        self.addButtons(self.window, self.world)
        self.window.mainloop()

    def printBoard(self):
        self.canvas.delete("all")
        for i in range(self.world.worldHeight):
            for j in range(self.world.worldWidth):
                if self.world.board[i][j] == None:
                    self.canvas.create_rectangle(j * self.sscale,  i * self.sscale,
                                                 self.SCALE + self.sscale * self.world.worldWidth,
                                                 self.SCALE + self.sscale * self.world.worldWidth, fill="#DF9800")
                else:
                    self.canvas.create_rectangle(j * self.sscale,  i * self.sscale,
                                                 self.SCALE + self.sscale * self.world.worldWidth,
                                                 self.SCALE + self.sscale * self.world.worldWidth, fill=self.world.board[i][j].getColor())
        self.canvas.place(height=650, width=650, x=10, y=self.SCALE+10, )
        self.addText(self.window)

    def addNewWorld(self, window):
        input = Tk()
        e = Entry(input)
        e.pack()

        def callback():
            sscale = e.get()
            self.sscale=int(sscale)
            self.world = World(self.sscale,False)
            self.canvas = Canvas(window, width=650, height=650, background="#000000")
            self.printBoard()
            self.addButtons(window, self.world)
            self.addText(window)
            input.destroy()

        b = Button(input, text="Confirm", command=callback)
        b.pack()


    def addText(self,window):
        font = ("Comic Sans MS", 10, "bold")
        self.text = Text(window, height=650, width=400)
        self.text.configure(font=font)

        self.text.insert(END,self.world.comment.getText())
        self.text.place(y=self.SCALE + 10, x=20 + 650, height=650, width=400)

    def arrowUp(self):
        human=self.world.getHuman().getPosition()
        if human.getY()!=0:
            self.world.setHumanMove(Point(0,-1))

    def arrowDown(self):
        human = self.world.getHuman().getPosition()
        if human.getY() != self.world.worldHeight-1:
            self.world.setHumanMove(Point(0, 1))

    def arrowRight(self):
        human = self.world.getHuman().getPosition()
        if human.getX() != self.world.worldWidth-1:
            self.world.setHumanMove(Point(1, 0))

    def arrowLeft(self):
        human = self.world.getHuman().getPosition()
        if human.getX() != 0:
            self.world.setHumanMove(Point(-1, 0))
    def humanAbility(self):
        if self.world.getCoolDown()==5:
            self.world.setHumanAbility(True)
            self.world.getHuman().setRange(2)

    def nextTurn(self):
        self.world.comment.removeComment()
        self.world.makeTurn()
        self.printBoard()

    def quitGame(self, window):
        window.destroy()

    def saveGame(self):
        input=Tk()
        e=Entry(input)
        e.pack()
        def callback():
            name=e.get()
            self.world.saveWorld(name)
            input.destroy()
        b=Button(input,text="Confirm",command=callback)
        b.pack()

    def loadGame(self,window):
        input = Tk()
        e = Entry(input)
        e.pack()

        def callback():
            name = e.get()
            self.loadParamets(name)
            self.world = World(self.sscale, True)
            self.world.loadFile(name)
            self.canvas = Canvas(window, width=650, height=650, background="#000000")
            self.printBoard()
            self.addButtons(window, self.world)
            self.addText(window)
            input.destroy()

        b = Button(input, text="Confirm", command=callback)
        b.pack()

    def loadParamets(self,name):
        file = open(name + ".txt", "r")
        for line in file:
            x = line.split()
            if x[0] == "#":
                self.sscale = int(x[1])
            break

    def addButtons(self, window, world):
        newGame = Button(window, text="New Game", command=lambda: self.addNewWorld(window), bg="#000000", fg="#FFFFFF")
        load = Button(window, text="Load",command=lambda: self.loadGame(window), bg="#000000", fg="#FFFFFF")
        save = Button(window, text="Save",command=lambda: self.saveGame(), bg="#000000", fg="#FFFFFF")
        quit = Button(window, text="Quit", command=lambda: self.quitGame(window), bg="#000000", fg="#FFFFFF")
        nextTurn = Button(window, text="Next Turn",command=lambda: self.nextTurn(), bg="#000000", fg="#FFFFFF")

        newGame.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=0, y=0, )
        load.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=2 * self.SCALE, y=0)
        save.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=2 * 2 * self.SCALE, y=0)
        quit.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=3 * 2 * self.SCALE, y=0)
        if world != None:
            nextTurn.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=self.WIDTH - 3 * self.SCALE,
                           y=self.HEIGHT - self.SCALE, )
            window.bind('<Left>', lambda ev: self.arrowLeft())
            window.bind('<Right>', lambda ev: self.arrowRight())
            window.bind('<Up>', lambda ev: self.arrowUp())
            window.bind('<Down>', lambda ev: self.arrowDown())
            window.bind('<r>', lambda ev: self.humanAbility())