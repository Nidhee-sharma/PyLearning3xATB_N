
class XYZ:

    def f1(self):
        try:
            a= int(input("enter a number\n"))
        except Exception as e:
            print("enter int value of a ")
        else:
            print(a)
        finally:
            print("anyhow i will printed")

x =XYZ()
x.f1()