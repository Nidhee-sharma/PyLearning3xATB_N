#enacapsulation
#wraaping of data
#hiding of data
#Data binding
#bind the data variables with the methods
#Data members/ class variables
#method def fi=unction with class
#wrapping or binding the data variables with the method -encapsulation
#hide the data members(class variables , instance variables) by using only the methods


class Car:
    name = None
    password=123

    def __init__(self):
        print("i am called when object is created")


    def change_password(self):
        self.password = "5677"
        print(self.password)

suv = Car()
suv.change_password()