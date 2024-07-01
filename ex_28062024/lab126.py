# example of create claass and object
# real time example of selenium automation
# page you are going to automate
# can create tuple and set

class VWoLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        print("email  " + self.email)
        if self.email == "nidhee.sharma@gmail.com" and self.password == 'password123':
            print("allowed")

        else:
            print("not ALLOWED")
    # this is end of the class

email = input("enter the email \n")
password = input("enter the password \n")
hi = VWoLoginPage('nidhee.sharma@gmail.com', "password123")
hi.login_confirm()

hi = VWoLoginPage('nidhee.sharma@gmail.com', "password125")
hi.login_confirm()
