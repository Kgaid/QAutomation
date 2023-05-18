import datetime

def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        current_time = datetime.datetime.now()
        log_message = f"Function launched at {current_time} with result {result}\n"

        with open("info.txt", "a") as log_file:
            log_file.write(log_message)

        return result
    return wrapper

@log_result
def sum_args2(*args):
    total_sum = sum(args)
    return total_sum

sum_args2(7,45,98,24)