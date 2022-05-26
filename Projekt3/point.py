
class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        return other.x==self.x and other.y==self.y
    def set(self,p):
        self.x=p.x
        self.y=p.y

    def setXY(self, x,y):
        self.x = x
        self.y = y
    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y