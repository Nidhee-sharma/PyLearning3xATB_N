#multiple condition
#switch in java
#match case

def switch_example(x):
    """
    This function takes an integer input x and returns a string
    based on the value of x.
    """
    return {
        0: "x is 0",
        1: "x is 1",
        2: "x is 2",
        3: "x is 3",
        4: "x is 4",
    }.get(x, "x is not between 0 and 4")


print(switch_example(2))

numbers = int(input("Enter a number between 0 and 4:\n"))
match numbers:
    case 0:
        print("x is 0")
        print("second line also")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case _:
        print("x is not between 0 and 4")

numbers = int(input("Enter a number between 0 and 4:\n"))
match numbers:
    case  0 | 1 | 2 | 3 | 4:
        print("x is between 0 and 4")
    case _:
        print("x is not between 0 and 4")

name = input("Enter a number between 0 and 4:\n")
match name:
    case "nidhee" | "Nidhee" | "NIDHEE":
        print("You are Nidhee")
        print("second line also")