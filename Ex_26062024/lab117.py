class calc:

    def __init__(self):
        print("default constructor")
    def sum(self,a,b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b

object_ref = calc()
print(object_ref.sum(10, 20))