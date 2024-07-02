#overloading   not supported
#overloading does not support overloading in tradition sense

class MathUtils(object):
    def add(self,a,b=0,c=0):
        return a+b+c

   # def add(self,a,b,c):
     #   return a+c

math =MathUtils()
opt1 =math.add(a=3,b=4)
opt2 =math.add(a=3,b=4,c=5)
opt3 =math.add(1)
print(opt1)
print(opt2)
print(opt3)


