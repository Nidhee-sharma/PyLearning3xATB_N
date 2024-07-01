class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._public_var = "public"  #it is not allowed outsid of the cllass directly
        self.__private_var = "public"  #it is not allowed outsid of the cllass directly

    def __private_method(self):  #private method
        print("protected")

    def printName(self): #public
        self.__private_method()
        if self.__private_var == "123":
            print("hi","123")
        print("I am allowed from alto public")

alto = Car()   #alto can access public it ca not access private
alto.printName()
