import random

from .animal import Animal
from Projekt3.point import Point
class Human (Animal):

    def __init__(self,world,point,strenght=5,age=1):
        super().__init__(world, point, 4, strenght, 1, age, True)
        self.newPosition=Point(0,0)

    def getColor(self):
        return "#000000"

    def getName(self):
        return "Human"

    def clone(self,p):
        return Human(self.world,p)

    def action(self):
        self.age+=1
        self.specialAbility()
        for i in range(self.range):
            self.newPosition = Point(self.point.getX() + self.world.getHumanMove().getX(),self.point.getY() + self.world.getHumanMove().getY())
            if self.world.getBoard()[self.newPosition.getY()][self.newPosition.getX()]==None:

                self.world.comment.addComment(self.getName()+" move from (x: "+str(self.point.getX())+", y: "+str(self.point.getY())+") to (x: "+str(self.newPosition.getX())+", y: "+str(self.newPosition.getY())+")")
                self.makeMove(self.newPosition)
            elif self.world.getBoard()[self.newPosition.getY()][self.newPosition.getX()].getName()!="Human":
                super(Human,self).collision(self.world.getBoard()[self.newPosition.getY()][self.newPosition.getX()])
            if self.world.getBoard()[self.point.getY()][self.point.getX()]!=self:
                break
        self.world.setHumanMove(Point(0,0))

    def specialAbility(self):
        if self.world.getHumanAbility()==True and self.world.getCoolDown()==0:
            self.range=1
            self.world.setHumanAbility(False)
        elif self.world.getHumanAbility()==True and self.world.getCoolDown()<=2 and self.world.getCoolDown()!=0:
            chance=random.randint(1,2)
            if chance==1:
                self.range=1
        if self.world.getHumanAbility()==True:
            self.world.comment.addComment("Round with special skills "+str(self.world.getCoolDown()))
        elif (self.world.getHumanAbility() == False and self.world.getCoolDown() == 5):
            self.world.comment.addComment("Ready. Your cooldown is " + str(self.world.getCoolDown()))
        elif(self.world.getHumanAbility()==False):
            self.world.comment.addComment("Too low cool down. Your cooldown is " + str(self.world.getCoolDown()))


    def setNewPosition(self,point):
        self.newPosition=point

    def getPosition(self):
        return self.point