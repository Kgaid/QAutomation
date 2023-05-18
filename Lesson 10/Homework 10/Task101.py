import time

def measure_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function executed for  {execution_time} seconds.")
        return result
    return wrapper

@measure_time
def sum_args(*args):
    total_sum = sum(args)
    return total_sum

sum_args(5,10,95,454,684,384,5)


