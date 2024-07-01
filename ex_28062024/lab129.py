class VWOLogin():

     def __init__(self,email,password):
         self.__email = email
         self.__password= password
         self.name="nidhee"

     def login_confirm(self):
         if self.__email ==  "abc@gmail.com" and self.password == "123":
             print("allowed")
         else:
             print("not allowed")

#this is end of the class
page1 = VWOLogin("xyz",'2')
page1.login_confirm()
#page1.__email ="?"
#page1.__password
print(page1.name)