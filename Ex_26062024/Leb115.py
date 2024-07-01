class dog:
    name =None
#constorcture is used to initialize the value

    def sleep(self):
        print("������")

    def eat(self):
        print("������")

dog1 = dog()
print(dog1.name)
dog1.name="dog1"
print(dog1.name)
dog1.sleep()
print("*********")

dog2 =dog()
print(dog2.name)
dog2.name ="bye"
print(dog2.name)
dog2.eat()
print("*********")