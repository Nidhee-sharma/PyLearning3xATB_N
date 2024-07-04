try:
    num1  =int(input("enter a number 1\n"))
    num2 = int(input("enter a number 2\n"))
    result =num1/num2
    print(result)
except ValueError as e1:
    print(e1)
    print("i am in except")
except ZeroDivisionError as e2:
    print(e2)
    print("10/0")
else:
    print(f'Result is {result}')
finally:
    print("i will be executed anyhow")