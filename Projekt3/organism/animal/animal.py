from Projekt3.organism import Organism


class Animal(Organism):

    def __init__(self,world,point,initiative,strenght,range,age,newBorn):
        super().__init__(world,point,initiative,strenght,range,age,newBorn)

    def breed(self,org):
        newPos=self.findFreeField(org)
        if newPos!=org.point:
            self.world.place(self.clone(newPos),newPos)


    def action(self):
        self.age+=1
        for i in range(self.range):
            p=self.newPosition()
            if self.world.getBoard()[p.getY()][p.getX()]==None:
                self.world.comment.addComment(self.getName()+" move from (x: "+str(self.point.getX())+", y: "+str(self.point.getY())+") to (x: "+str(p.getX())+", y: "+str(p.getY())+")")
                self.makeMove(p)
            else:
                self.collision(self.world.getBoard()[p.getY()][p.getX()])

    def collision(self,oc):
        if oc.getName()=="Turtle" and self.getStrenght()<5:
            self.world.comment.addComment(oc.getName()+" fight off the "+self.getName()+" atack")
        elif oc.getName()==self.getName() and oc!=self:
            if oc.getAge()<=6 and self.getAge()<=6:
                self.world.comment.addComment(oc.getName() + " too young to breed")
            elif self.findFreeField(self)!=self.point:
                self.breed(self)
            elif self.findFreeField(oc)!=oc.point:
                self.breed(oc)
            else:
                self.world.comment.addComment("There's no open field to give birth "+oc.getName())

        elif oc.getName()=="Guarana":
            self.setStrenght(self.getStrenght()+3)
            self.world.removeOrganism(oc)
            self.world.comment.addComment(self.getName() + " move from (x: " + str(self.point.getX()) + ", y: " + str(
                self.point.getY()) + ") to (x: " + str(oc.point.getX()) + ", y: " + str(oc.point.getY()) + ")")
            self.makeMove(oc.getPoint())
            self.world.comment.addComment(self.getName()+" eat Guarana, new strenght "+str(self.getStrenght()))

        elif (oc.getName()=="Borscht" and self.getName()!="CyberSheep") or oc.getName()=="Berries":
            self.world.comment.addComment(oc.getName() + " kill " + self.getName())
            self.world.removeOrganism(self)

        else:
            self.fight(oc)


    def fight(self,oc):
        if oc.getStrenght() > self.getStrenght():
            self.world.comment.addComment(self.getName()+" move from (x: "+str(self.point.getX())+", y: "+str(self.point.getY())+") to " +
            "(x: "+str(oc.point.getX())+", y: "+str(oc.point.getY())+")")
            self.world.comment.addComment(oc.getName()+" kill "+self.getName())
            self.world.removeOrganism(self)
        elif oc.getStrenght() <= self.getStrenght():
            self.world.comment.addComment(self.getName()+" move from (x: "+str(self.point.getX())+", y: "+str(self.point.getY())+") to " +
            "(x: "+str(oc.point.getX())+", y: "+str(oc.point.getY())+")")
            self.world.comment.addComment(self.getName()+" kill "+oc.getName())
            self.world.removeOrganism(oc)
            self.makeMove(oc.point)
