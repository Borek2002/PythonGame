
class Comment:
    def __init__(self):
        self.text=""

    def addComment(self,comment):
        self.text+=comment+"\n"

    def getText(self):
        return self.text

    def removeComment(self):
        self.text=""
