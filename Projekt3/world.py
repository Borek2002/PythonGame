from point import Point
import random
from Projekt3.organism.animal import Wolf, Sheep
from point import Point

class World:
    SCALE=4
    def __init__(self,scale):
        self.worldHeight=int(700/scale)
        self.worldWidth=int(700/scale)
        self.board=[[None for i in range(self.worldHeight)]for j in range(self.worldWidth)]
        self.organismList=[]
        self.randomPlace(Wolf(self,Point(-1,-1),1))
        self.randomPlace(Sheep(self,Point(-1,-1),1))
        self.place(Sheep(self,Point(-1,-1),1),Point(0,0))

    def makeTurn(self):
        for i in range(len(self.organismList)):
            if self.organismList[i].getNewBorn==True:
                self.organismList[i].setNewBorn(False)
        i=0
        while (i!=len(self.organismList)):
            self.organismList[i].action()
            i+=1

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
                self.organismList.pop(i)
            i+=1

    def randomPlace(self,newone):
            while(True):
                newX=random.randint(0,self.worldWidth-1)
                newY=random.randint(0,self.worldHeight-1)
                if self.board[newY][newX]==None:
                    newone.point.setXY(newX,newY)
                    self.board[newY][newX] =newone
                    self.addOrganism(newone)
                    break

    def place(self,newone,point):
        newone.point.set(point)
        self.board[point.getY()][point.getX()]=newone
        self.addOrganism(newone)

    def getBoard(self):
        return self.board