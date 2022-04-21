import time
def delay_decorator(function):
    def wrapper_function():
        #do somethinf before function call
        time.sleep(2)
        function()
        function()
        #do seomthing adter
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")

def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello()
