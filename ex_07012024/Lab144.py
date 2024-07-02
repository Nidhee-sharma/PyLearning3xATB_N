#method overriding - same name in the parent class
#child always override the parent functions
#super means call my parent function

class Father:
    def home(self):
        print("1BHK")

class Son(Father):

    def home(self):
        super().home()
        print("3BHK")


pramod = Son()
print(pramod.home())
