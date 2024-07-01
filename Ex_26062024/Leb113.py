class person:

     Id = None
     Name = None
     Age = None
     Phone = None

     #behaviour
     def eat(self):  #No argument no return type
         print("I am eating")

     def sleep(self,name): #argument with return type
         return name

     def walk(self): #No argument with return type
         return "I am walking"

     def run(self): #No argument no return type
         print("I am running")

     def talk(self, text): #argument with return type
         return text



#craete object of person class
#objectref = object () -ClassName()

surya = person()
surya.Id = 1
surya.Name = "Surya"
surya.Age = 21
surya.Phone = 1234567890
surya.eat()
print(surya.sleep("Surya"))
print(surya.walk())






