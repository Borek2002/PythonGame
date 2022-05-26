from Projekt3.organism import Organism


class Animal(Organism):

    def __init__(self,world,point,initiative,strenght,range,age,newBorn):
        super().__init__(world,point,initiative,strenght,range,age,newBorn)