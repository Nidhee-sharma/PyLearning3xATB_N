
class person:

    #class variable/instance variable
    name = "amit"
    age = None

    def walk(self):
        a =10 #local variable
        print("I am a method")
        print("Hi", self.age)


amit = person()
amit.walk()