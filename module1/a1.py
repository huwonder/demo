class Parent:
    parentAttr = 100
    def __init__(self):
        print("call parent struct function")

    def parentmethod(self):
        print("parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("parent attribute", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("child struct function")

    def childmethod(self):
        print("child method")

c = Child()
c.childmethod()
c.parentmethod()
c.setAttr(200)
c.getAttr()
