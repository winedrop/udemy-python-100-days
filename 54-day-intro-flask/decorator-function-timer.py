import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(time_elapsed)
    return wrapper
    pass

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
   
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()