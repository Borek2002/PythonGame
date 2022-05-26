from tkinter import *
from world import World


class MainWindow(Frame):
    world = None
    screenBoard = None
    canvas = None
    SCALE = 50
    HEIGHT = 750
    WIDTH = 1300
    sscale = 25

    def __init__(self):
        print("Okienczko")

    def addWindow(self):
        window = Tk()
        window.geometry("1300x750")
        self.addButtons(window, self.world)
        window.mainloop()

    def printBoard(self):
        self.canvas.delete("all")
        for i in range(self.world.worldHeight):
            for j in range(self.world.worldWidth):
                if self.world.board[i][j] == None:
                    self.canvas.create_rectangle(j * self.sscale, self.SCALE + i * self.sscale,
                                                 self.SCALE + self.sscale * self.world.worldWidth,
                                                 self.SCALE + self.sscale * self.world.worldWidth, fill="#DF9800")
                else:
                    self.canvas.create_rectangle(j * self.sscale, self.SCALE + i * self.sscale,
                                                 self.SCALE + self.sscale * self.world.worldWidth,
                                                 self.SCALE + self.sscale * self.world.worldWidth, fill=self.world.board[i][j].getColor())
        self.canvas.place(height=700, width=700, x=10, y=10, )

    def addNewWorld(self, window):
        self.world = World(self.sscale)
        self.canvas = Canvas(window, width=700, height=700)
        self.printBoard()
        self.addButtons(window, self.world)

    def quit(self, window):
        window.destroy()

    def addButtons(self, window, world):
        newGame = Button(window, text="New Game", command=lambda: self.addNewWorld(window), bg="#000000", fg="#FFFFFF")
        load = Button(window, text="Load", bg="#000000", fg="#FFFFFF")
        save = Button(window, text="Save", bg="#000000", fg="#FFFFFF")
        quit = Button(window, text="Quit", command=lambda: self.quit(window), bg="#000000", fg="#FFFFFF")
        nextTurn = Button(window, text="Next Turn", bg="#000000", fg="#FFFFFF")

        newGame.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=0, y=0, )
        load.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=2 * self.SCALE, y=0)
        save.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=2 * 2 * self.SCALE, y=0)
        quit.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=3 * 2 * self.SCALE, y=0)
        if world != None:
            nextTurn.place(bordermode=OUTSIDE, height=self.SCALE, width=2 * self.SCALE, x=self.WIDTH - 2 * self.SCALE,
                           y=self.HEIGHT - self.SCALE, )
