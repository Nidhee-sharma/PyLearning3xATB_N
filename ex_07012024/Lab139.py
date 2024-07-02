class A:
    def method(self):
        return "metod A"

class B:

    def method(self):
        return "method B"

class c(A,B): #call first A
    pass

class D(B,A): #call first B
    pass

c=c()
print(c.method())
d=D()
print(d.method())