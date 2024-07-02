
class parent:
    gold = "2kg"

    def BHK2(self):
        print("2bhk")

class child(parent):

    def BHK3(self):
        print("3BHK")

Child = child()
Child.BHK3()
print(Child.BHK3())
print(Child.BHK2())
print(Child.gold)

father = parent()
