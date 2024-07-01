class bankAccount:

    def __init__(self):
        self.balance =0
        self.__private_var =100

    def public_Fn(self):
        print(self.__private_var)

    def deposite(self,amount):
        self.balance +=  amount

    def __withdraw(self,amount):
        self.balance -= amount

    def __show_balance(self):
        print("you balance is" , self.balance)

    def if_you_are_authenticate_function(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("not allowed")

    def if_youauthenticate_user(self,auth,amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("not allowed")

jp_chase = bankAccount()
jp_chase.deposite(100)

secret_pass =input("enter your pin to see balance")
if secret_pass =="1234":
    jp_chase.if_you_are_authenticate_function(True)
else:
    jp_chase.if_you_are_authenticate_function(False)


secret_pass =input("enter your pin to withdraw")
your_amounnt = int(input("enter your amount to withdraw"))
if secret_pass =="1234":
    jp_chase.if_youauthenticate_user(True,your_amounnt )
else:
    jp_chase.if_youauthenticate_user(False)


jp_chase.if_you_are_authenticate_function(True)
jp_chase.if_youauthenticate_user(True,99)
jp_chase.if_you_are_authenticate_function(True)
