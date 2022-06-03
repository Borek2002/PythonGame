from .animal import Animal

class Fox (Animal):

    def __init__(self,world,point,strenght=3,age=1):
        super().__init__(world, point, 7, strenght, 1, age, True)

    def getColor(self):
        return "#BF4400"

    def getName(self):
        return "Fox"

    def clone(self,p):
        return Fox(self.world,p)

    def action(self):
        self.age+=1
        while(True):
            p=self.newPosition()
            if self.world.getBoard()[p.getY()][p.getX()]==None:
                self.world.comment.addComment(self.getName()+" move from (x: "+str(self.point.getX())+", y: "+str(self.point.getY())+") to (x: "+str(p.getX())+", y: "+str(p.getY())+")")
                self.makeMove(p)
                break
            elif self.world.getBoard()[p.getY()][p.getX()].getStrenght()<=self.getStrenght():
                self.collision(self.world.getBoard()[p.getY()][p.getX()])
                break