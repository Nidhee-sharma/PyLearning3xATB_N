#hierarchical inheritance

#father - multiple childern

class Father:
    def BHK1(self):
        print("BHK1")


class pramod(Father):

    def bHK2(self):
        print("BHK2")

class Amit(Father):

    def BHK3(self):
        print("BHK3")

class Lucky(Father):

    def no_house(self):
        print("No house")

pramod = pramod()
pramod.BHK1()
pramod.bHK2()

amit = Amit()
amit.BHK1()
amit.BHK3()

lucky =Lucky()
lucky.BHK1()
lucky.no_house()





