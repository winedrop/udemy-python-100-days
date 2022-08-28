import time

#decorator function is a way to add functionality to many things without repeating/copying code
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #do something before function you are decorating
        function()
        #function() could also run the function more than once
        #do something after function you are decorating
    return wrapper_function

#will print after a delay
@delay_decorator 
def say_hello():
    print("Hello")

#will print after a delay
@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("how are you?")

#decorator modifies the functionality or adds functionality to an existing function

#can use @ as a way to simplify the calling of decorator functions
##@delay_decorator equivalent to below, but will also allow you to trigger the function by the original function name, and better formatting 
decorated_function = delay_decorator(say_greeting)
decorated_function()