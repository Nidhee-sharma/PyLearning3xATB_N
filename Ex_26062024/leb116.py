class dog:
    name =None
    id =None

   # def __init__(self):
      #  print("I am an empty without arguments")
#constorcture is used to initialize the value
    def __init__(self,name,id):
        self.name = name
        self.id = id
        print("constorcture is used to initialize the value")
    def sleep(self):
        print("who is sleeping ---"+self.name)

dog1 =dog("sai",1)
dog2 =dog("bye", 2)
print(f' {dog1.name} has {dog1.id}')
print(f'{dog2.name} have {dog2.id}')

dog1.sleep()
dog2.sleep()
#dog3 = dog()  dog.__init__() missing 2 required positional arguments: 'name' and 'id'

