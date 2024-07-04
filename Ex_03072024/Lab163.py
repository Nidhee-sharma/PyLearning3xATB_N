#custom exception

class MyClassException(Exception):
    def __init__(self,message):
        self.message =message +"lol"
        super().__ini__(message)

balance =100
withdraw =int(input("enter the amount!"))
if withdraw >balance:
    raise MyClassException("balance is low!")
else:
    print("Remain bal" ,(balance-withdraw  ))