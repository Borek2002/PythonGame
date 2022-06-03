from point import Point
import random
from Projekt3.organism.animal import Wolf, Sheep, Fox, Turtle, Antylope, Human,CyberSheep
from Projekt3.organism.plant import Grass, Dandelion, Guarana, PineBorscht, WolfBerries
from point import Point

from comment import Comment


class World:
    SCALE = 4

    def __init__(self, scale, loadFromFile):
        self.scale = scale
        self.worldHeight = int(650/self.scale)
        self.worldWidth = int(650/self.scale)
        self.loadFromFile = loadFromFile
        self.board = [[None for i in range(self.worldHeight)] for j in range(self.worldWidth)]
        self.organismList = []
        self.turn = 1
        self.coolDown = 1
        self.humanAbility = False
        self.humanMove = Point(0, 0)
        self.human = None
        self.comment = Comment()
        if loadFromFile == False:
            self.randomPlace(Wolf(self, Point(-1, -1)))
            self.randomPlace(Sheep(self, Point(-1, -1)))
            self.randomPlace(Fox(self, Point(-1, -1)))
            self.randomPlace(Turtle(self, Point(-1, -1)))
            self.randomPlace(Antylope(self, Point(-1, -1)))
            self.randomPlace(CyberSheep(self, Point(-1, -1)))
            self.randomPlace(Grass(self, Point(-1, -1)))
            self.randomPlace(Dandelion(self, Point(-1, -1)))
            self.randomPlace(Guarana(self, Point(-1, -1)))
            self.randomPlace(PineBorscht(self, Point(-1, -1)))
            self.randomPlace(WolfBerries(self, Point(-1, -1)))
            self.randomPlace(Human(self, Point(-1, -1)))

    def makeTurn(self):
        self.turn += 1
        for i in range(len(self.organismList)):
            if self.organismList[i].getNewBorn == True:
                self.organismList[i].setNewBorn(False)
            if self.organismList[i].getName() == "Human":
                self.human = self.organismList[i]
        i = 0
        if self.humanAbility == False and self.coolDown < 5:
            self.coolDown += 1
        elif self.humanAbility == True and self.coolDown > 0:
            self.coolDown -= 1
        while (i != len(self.organismList)):
            if self.organismList[i].getDie() == False:
                self.organismList[i].action()
            i += 1
        self.removeDieOrgnism()
        # dodac zmienna czy zyje i na konie ctury usuwac zabite ogrganismy zapsane w drugim pliku

    def addOrganism(self, other):
        i = 0
        while (i != len(self.organismList)):
            if self.organismList[i].getInitiative() < other.getInitiative():
                self.organismList.insert(i, other)
                break
            elif self.organismList[i].getInitiative() == other.getInitiative():
                if self.organismList[i].getAge() <= other.getAge():
                    self.organismList.insert(i, other)
                    break
            i += 1
        if i == len(self.organismList):
            self.organismList.insert(i, other)
        if other.getName() == "Human":
            self.human = other

    def removeOrganism(self, other):
        i = 0
        self.board[other.point.getY()][other.point.getX()] = None
        while (i != len(self.organismList)):
            if self.organismList[i] == other:
                self.organismList[i].setDie(True)
                break
            i += 1

    def removeDieOrgnism(self):
        for i in range(len(self.organismList) - 1, -1, -1):
            if self.organismList[i].getDie() == True:
                self.organismList.pop(i)

    def randomPlace(self, newone):
        while (True):
            newX = random.randint(0, self.worldWidth - 1)
            newY = random.randint(0, self.worldHeight - 1)
            if self.board[newY][newX] == None:
                newone.point.setXY(newX, newY)
                self.board[newY][newX] = newone
                self.addOrganism(newone)
                self.comment.addComment(
                    "New " + newone.getName() + " born on (x: " + str(newone.point.getX()) + ", y: " + str(
                        newone.point.getY()) + ")")

                break

    def place(self, newone, point):
        newone.point.set(point)
        self.board[point.getY()][point.getX()] = newone
        self.addOrganism(newone)
        self.comment.addComment(
            "New " + newone.getName() + " born on (x: " + str(point.getX()) + ", y: " + str(point.getY()) + ")")

    def saveWorld(self, name):
        file = open(name + ".txt", "w")
        file.write("# " + str(self.scale) + " " + str(int(self.humanAbility)) + " " + str(self.coolDown) + " " + str(self.turn) + "\n")
        i = 0
        while (i != len(self.organismList)):
            if self.organismList[i].getDie() == False:
                file.write(
                    str(self.organismList[i].getName()) + " " + str(self.organismList[i].getPoint().getX()) + " " +
                    str(self.organismList[i].getPoint().getY()) + " " + str(
                        self.organismList[i].getStrenght()) + " " + str(self.organismList[i].getAge()) + "\n")
            i += 1
        file.close()

    def loadFile(self, name):
        file = open(name + ".txt", "r")
        for line in file:
            x = line.split()
            if x[0] == "#":
                self.humanAbility=bool(int(x[2]))
                print(self.humanAbility)
                self.coolDown=int(x[3])
                self.turn=int(x[4])
            else:
                if x[0]=="Fox":
                    self.place(Fox(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0]=="Wolf":
                    self.place(Wolf(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0]=="Sheep":
                    self.place(Sheep(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0] == "CyberSheep":
                    self.place(CyberSheep(self, Point(int(x[1]), int(x[2])), int(x[3]), int(x[4])),Point(int(x[1]), int(x[2])))
                elif x[0]=="Turtle":
                    self.place(Turtle(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0]=="Antylope":
                    self.place(Antylope(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0]=="Dandelion":
                    self.place(Dandelion(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0]=="Grass":
                    self.place(Grass(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0]=="Guarana":
                    self.place(Guarana(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0]=="Borscht":
                    self.place(PineBorscht(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0]=="Berries":
                    self.place(WolfBerries(self,Point(int(x[1]),int(x[2])),int(x[3]),int(x[4])),Point(int(x[1]),int(x[2])))
                elif x[0] == "Human":
                    self.place(Human(self, Point(int(x[1]), int(x[2])), int(x[3]), int(x[4])),Point(int(x[1]), int(x[2])))

    def getBoard(self):
        return self.board

    def setHumanAbility(self, humanAbility):
        self.humanAbility = humanAbility

    def getHumanAbility(self):
        return self.humanAbility

    def setCoolDown(self, coolDown):
        self.coolDown = coolDown

    def getCoolDown(self):
        return self.coolDown

    def getHumanMove(self):
        return self.humanMove

    def setHumanMove(self, move):
        self.humanMove = move

    def getHuman(self):
        return self.human
