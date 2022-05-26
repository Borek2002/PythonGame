from tkinter import *
from world import World

class MainWindow(Frame):

    SCALE = 50
    HEIGHT = 700
    WIDTH = 1300
    sscale = 50

    def __init__(self):
        print("Okienczko")
        self.world = None
        self.screenBoard = None
        self.canvas = None
        self.text = None
        self.sccrollBar = None
        self.window=None

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
        self.world = World(self.sscale)
        self.canvas = Canvas(window, width=650, height=650,background="#000000")
        self.printBoard()
        self.addButtons(window, self.world)
        self.addText(window)

    def addText(self,window):
        font = ("Comic Sans MS", 10, "bold")
        self.text = Text(window, height=650, width=400)
        self.text.configure(font=font)

        self.text.insert(END,self.world.comment.getText())
        self.text.place(y=self.SCALE + 10, x=20 + 650, height=650, width=400)

    def nextTurn(self):
        self.world.comment.removeComment()
        self.world.makeTurn()
        self.printBoard()

    def quit(self, window):
        window.destroy()

    def addButtons(self, window, world):
        newGame = Button(window, text="New Game", command=lambda: self.addNewWorld(window), bg="#000000", fg="#FFFFFF")
        load = Button(window, text="Load", bg="#000000", fg="#FFFFFF")
        save = Button(window, text="Save", bg="#000000", fg="#FFFFFF")
        quit = Button(window, text="Quit", command=lambda: self.quit(window), bg="#000000", fg="#FFFFFF")
        nextTurn = Button(window, text="Next Turn",command=lambda: self.nextTurn(), bg="#000000", fg="#FFFFFF")

        newGame.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=0, y=0, )
        load.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=2 * self.SCALE, y=0)
        save.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=2 * 2 * self.SCALE, y=0)
        quit.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=3 * 2 * self.SCALE, y=0)
        if world != None:
            nextTurn.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=self.WIDTH - 3 * self.SCALE,
                           y=self.HEIGHT - self.SCALE, )
