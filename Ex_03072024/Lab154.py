print("start of the program")
try:

    a = int(input("Enter the num1"))
    b = int(input("Enter the num1"))
    c = a / b
    print("Result div is", c)
except Exception as e:
    print(e)
    print("Please enter integer")

print("end of the program")