
import time

def note_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Time taken - "+str(end_time - start_time))
        return result
    return wrapper


@note_time_decorator
def my_function():
    time.sleep(2)  # Simulating a delay
    print("This is my function.")


my_function()

@note_time_decorator
def logs_function():
    time.sleep(5)  # Simulating a delay
    print("print the logs of time taken.")

logs_function()

@note_time_decorator
def reporting_function():
    time.sleep(5)  # Simulating a delay
    print("This is my function.")

reporting_function()