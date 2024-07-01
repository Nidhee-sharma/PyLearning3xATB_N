class bankAccount:

    def __init__(self):
        self.balance =0
        self.__private_var =100

    def public_Fn(self):
        print(self.__private_var)

    def deposite(self,amount):
        self.balance +=  amount

    def withdraw(self,amount):
        self.balance -= amount

    def show_balance(self):
        print("you balance is" , self.balance)


jp_chase = bankAccount()
print(jp_chase.balance)
jp_chase.deposite(101)
print(jp_chase.show_balance())
jp_chase.deposite(99)
jp_chase.show_balance()
jp_chase.withdraw(199)
jp_chase.show_balance()