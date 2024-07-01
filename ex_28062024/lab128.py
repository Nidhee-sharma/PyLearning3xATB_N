 #bank
class MyClass:
     def __init__(self):
         self.name ="amit"
         self.email ="nidhee@gmail.com"

     def public_function(self):
         print("public_function()")

     def __private_function(self):
         print("I am private function")
         print("you can only access via a another method")

     def public_function_private(self):
         print("we can call private function in the public function")
         self.__private_function()
         print(self.email)

#security no everyone can acces the variables/methods
a= MyClass()
a.public_function_private()
a.public_function()

