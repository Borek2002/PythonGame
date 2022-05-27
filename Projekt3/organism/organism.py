import random
from abc import abstractmethod

from Projekt3.point import Point


class Organism:
    def __init__(self,world,point,initiative,strenght,range,age,newBorn):
        self.world=world
        self.point=point
        self.initiative=initiative
        self.strenght=strenght
        self.range=range
        self.age=age
        self.newBorn=newBorn
        self.die=False

    def makeMove(self,point):
        self.world.getBoard()[self.point.getY()][self.point.getX()]=None
        self.world.getBoard()[point.getY()][point.getX()]=self
        self.point.set(point)

    def newPosition(self):
        p = Point(self.point.getX(), self.point.getY())
        canMove = [True, True, True, True]
        if self.point.getY() == 0:
            canMove[0] = False
        if self.point.getY() == (self.world.worldHeight-1):
            canMove[1] = False
        if self.point.getX() == 0:
            canMove[2] = False
        if self.point.getX() == (self.world.worldWidth-1):
            canMove[3] = False
        while(True):
            direction=random.randint(0,3)
            if direction == 0 and canMove[direction] == True: # up
                p.y-=1
                return p

            elif direction == 1 and canMove[direction] == True: #down
                p.y +=1
                return p

            elif direction == 2 and canMove[direction] == True: #left
                p.x -=1
                return p

            elif direction == 3 and canMove[direction] == True: #right
                p.x+=1
                return p



    def findFreeField(self,organism):
        chance=-1
        p=Point(organism.point.getX(),organism.point.getY())
        canMove=[True,True,True,True]
        if self.point.getY()==0:
            canMove[0]=False
        if self.point.getY()==(self.world.worldHeight-1):
            canMove[1]=False
        if self.point.getX()==0:
            canMove[2]=False
        if self.point.getX()==(self.world.worldWidth-1):
            canMove[3]=False
        while chance!=3:
            chance=random.randint(0,3)
            if chance >= 3 and canMove[0] == True and self.world.getBoard()[p.getY() - 1][p.getX()] == None:
                p.y-=1
                return p
            elif chance >= 2 and canMove[1] == True and self.world.getBoard()[p.getY() + 1][p.getX()] == None:
                p.y+=1
                return p
            elif chance >= 1 and canMove[2] == True and self.world.getBoard()[p.getY()][p.getX()-1] == None:
                p.x -=1
                return p
            elif chance >= 1 and canMove[3] == True and self.world.getBoard()[p.getY()][ p.getX()-1] == None:
                p.x+=1
                return p
        return p


    def getInitiative(self):
        return self.initiative

    def getStrenght(self):
        return self.strenght

    def getAge(self):
        return self.age

    def getRange(self):
        return self.range

    def getPoint(self):
        return self.point

    def getNewBorn(self):
        return self.newBorn

    def setNewBorn(self,born):
        self.newBorn=born

    def setRange(self,range):
        self.range=range

    def getDie(self):
        return self.die

    def setStrenght(self,strenght):
        self.strenght=strenght

    def setDie(self,die):
        self.die=die
    @abstractmethod
    def getColor(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self,oc):
        pass

    @abstractmethod
    def clone(self,p):
        pass