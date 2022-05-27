import random

from Projekt3.organism import Organism

class Plant(Organism):

    def __init__(self,world,point,initiative,strenght,range,age,newBorn):
        super().__init__(world,point,initiative,strenght,range,age,newBorn)

    def action(self):
        self.age+=1
        chance=random.randint(0,10)
        if chance==1:
            for i in range(self.getRange()):
                p=self.newPosition()
                if self.world.getBoard()[p.getY()][p.getX()]==None:
                    self.world.place(self.clone(p),p)
