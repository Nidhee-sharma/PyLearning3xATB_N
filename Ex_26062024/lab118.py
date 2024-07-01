class calc:

    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("default constructor")
    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self,):
        return self.a/self.b


object_ref =calc(10,20)
print(object_ref.sum())