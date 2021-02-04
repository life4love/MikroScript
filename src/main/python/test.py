class Parent:
    def makeChildrenStopCry(self):
        if self.cry():
            self.doWhateverToStopCry()

class Children(Parent):
    crying = False
    def makeCry(self):
        self.crying = True
    def doWhateverToStopCry(self):
        self.crying = False
    def cry(self):
        return self.crying


child = Children()
child.makeCry()
print(child.crying)
child.makeChildrenStopCry()
print(child.crying)
