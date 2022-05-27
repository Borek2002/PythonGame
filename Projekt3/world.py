from point import Point
import random
from Projekt3.organism.animal import Wolf, Sheep, Fox, Turtle,Antylope
from Projekt3.organism.plant import Grass, Dandelion, Guarana, PineBorscht, WolfBerries
from point import Point

from comment import Comment
class World:
    SCALE=4
    def __init__(self,scale):
        self.worldHeight=int(650/scale)
        self.worldWidth=int(650/scale)
        self.board=[[None for i in range(self.worldHeight)]for j in range(self.worldWidth)]
        self.organismList=[]
        self.turn=1
        self.comment=Comment()
        self.randomPlace(Wolf(self,Point(-1,-1)))
        self.randomPlace(Sheep(self,Point(-1,-1)))
        self.randomPlace(Fox(self,Point(-1,-1)))
        self.randomPlace(Turtle(self,Point(-1,-1)))
        self.randomPlace(Antylope(self,Point(-1,-1)))
        self.randomPlace(Grass(self,Point(-1,-1)))
        self.randomPlace(Dandelion(self,Point(-1,-1)))
        self.randomPlace(Guarana(self,Point(-1,-1)))
        self.randomPlace(PineBorscht(self,Point(-1,-1)))
        self.randomPlace(WolfBerries(self,Point(-1,-1)))

    def makeTurn(self):
        self.turn+=1
        for i in range(len(self.organismList)):
            if self.organismList[i].getNewBorn==True:
                self.organismList[i].setNewBorn(False)
        i=0
        while (i!=len(self.organismList)):
            if self.organismList[i].getDie()==False:
                self.organismList[i].action()
            i+=1
        self.removeDieOrgnism()
        #dodac zmienna czy zyje i na konie ctury usuwac zabite ogrganismy zapsane w drugim pliku

    def addOrganism(self, other):
        i=0
        while(i!=len(self.organismList)):
            if self.organismList[i].getInitiative()<other.getInitiative():
                self.organismList.insert(i,other)
                break
            elif self.organismList[i].getInitiative()==other.getInitiative():
                if self.organismList[i].getAge()<=other.getAge():
                    self.organismList.insert(i,other)
                    break
            i+=1
        if i==len(self.organismList):
            self.organismList.insert(i,other)

    def removeOrganism(self,other):
        i=0
        self.board[other.point.getY()][other.point.getX()]=None
        while(i!=len(self.organismList)):
            if self.organismList[i]==other:
                self.organismList[i].setDie(True)
                break
            i+=1

    def removeDieOrgnism(self):
        for i in range(len(self.organismList)-1,-1,-1):
            if self.organismList[i].getDie()==True:
                self.organismList.pop(i)


    def randomPlace(self,newone):
            while(True):
                newX=random.randint(0,self.worldWidth-1)
                newY=random.randint(0,self.worldHeight-1)
                if self.board[newY][newX]==None:
                    newone.point.setXY(newX,newY)
                    self.board[newY][newX] =newone
                    self.addOrganism(newone)
                    self.comment.addComment(
                        "New " + newone.getName() + " born on (x: " + str(newone.point.getX()) + ", y: " + str(
                            newone.point.getY()) + ")")

                    break

    def place(self,newone,point):
        newone.point.set(point)
        self.board[point.getY()][point.getX()]=newone
        self.addOrganism(newone)
        self.comment.addComment("New " + newone.getName() + " born on (x: " + str(point.getX()) + ", y: " + str(point.getY()) + ")")

    def getBoard(self):
        return self.board