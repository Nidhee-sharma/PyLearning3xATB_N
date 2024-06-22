#decorator
#what is decorator?
#A decorator is a function that takes another function and extends its functionality.
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Before calling the function')
        result = func(*args, **kwargs)
        print('After calling the function')
        return result
    return wrapper


@my_decorator
def say_hello():
    print('Hello')

say_hello()
