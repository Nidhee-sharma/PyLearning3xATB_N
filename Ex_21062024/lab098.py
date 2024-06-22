def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
        print("Decorator bye")
    return wrapper


@decorator2
@decorator1
def say_hello():
    print("Hello!")

say_hello()