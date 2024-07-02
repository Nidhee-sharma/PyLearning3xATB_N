#hybrid
class A:
    def methodA(self):
        return "Method A"

class B(A):

    def methodB(self):
        return "Method B"

class C(A):

    def methodC(self):
        return "Method C "


class D(B,C,A): #:Multiple , multilevel ....
    def methodD(self):
        return "metjod D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())


