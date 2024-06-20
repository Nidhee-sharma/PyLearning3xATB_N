
#lamda expression:arguments

def find_odd_even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

check_even_odd =  lambda num: "even" if num%2==0 else "odd"
print(check_even_odd(11))