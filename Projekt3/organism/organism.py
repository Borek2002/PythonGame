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

    def makeMove(self,point):
        self.world.getBoard()[self.point.getY()][self.point.getX()]=None
        self.world.getBoard()[point.getY()][point.getX()]=None
        self.point.set(point)

    def newPosition(self):
        p=Point(self.point.getX(),self.point.getY())
        



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
    @abstractmethod
    def getColor(self):
        pass

    @abstractmethod
    def action(self):
        pass