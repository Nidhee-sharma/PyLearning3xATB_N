# functions
# bock of code - which can executed or reused
# define
# call
# built in functiion
# which are created by the python contributers
result = max(2, 3)


# user defined
# They can return something
# they can not return something -non return
# they have parameter
# They have paarameters/arguments


def say_helllo():  # No Return Type and No parameter/ Arguments
    print("Hello")


result = say_helllo()
print(result)


def say_hello_arg(name):
    print("Hello", name)


say_hello_arg("bye")
say_hello_arg("sharma")


def say_helloargs(name="Bye"):  # no return type with defauly arguments
    # write the code
    print("hello", name)


say_helloargs()
say_helloargs("sharma1")
say_helloargs(name="Nidhee2")


def say_hello_argument_returntype(a, b):  # argumnets+ return type
    c = a + b
    return c


result = say_hello_argument_returntype(2, 4)
result = say_hello_argument_returntype(a=4, b=6)
result = say_hello_argument_returntype(b=6, a=5)
print(result)

