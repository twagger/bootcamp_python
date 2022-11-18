"""Logguer module
This module is about decorators.
A nice tutorial is available here :
https://realpython.com/primer-on-python-decorators/
"""


import time
import os


def log(func):
    """Log decorator"""
    def wrapper(*args, **kwargs):
        # Start timer
        start_time = time.perf_counter()
        # Run function
        res = func(*args, **kwargs)
        # Stop timer and compute exec time
        end_time = time.perf_counter()
        run_time = end_time - start_time
        exec_time = f'{run_time:.3f} ms'
        if run_time >= 1:
            exec_time = f'{run_time:.3f} s'
        # Save log in the file
        line = (f'({os.environ["USER"]})Running: '
                f'{func.__doc__:<19}[ exec-time = {exec_time} ]\n')
        if os.path.isfile('./trace.log'):
            with open('./trace.log', 'a') as log_file:
                log_file.write(line)
        else:
            with open('./trace.log', 'x') as log_file:
                log_file.write(line)
        return res
    return wrapper
