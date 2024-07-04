
#custom exception

class Parent:
    def __init__(self):
        print("i am paremt")

class Son(Parent):

    def __init__(self):
        super().__init__()

s =Son()
