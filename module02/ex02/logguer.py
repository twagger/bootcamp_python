"""Logguer module
This module is about decorators.
A nice tutorial is available here :
https://realpython.com/primer-on-python-decorators/
"""


import time
from random import randint
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
        if os.path.isfile('./machine.log'):
            with open('./machine.log', 'a') as log_file:
                log_file.write(line)
        else:
            with open('./machine.log', 'x') as log_file:
                log_file.write(line)
        return res
    return wrapper


class CoffeeMachine():
    """Coffe machine"""
    water_level = 100

    @log
    def start_machine(self):
        """Start machine"""
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        """Boil water"""
        return "boiling..."

    @log
    def make_coffee(self):
        """Make coffee"""
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
        print(self.boil_water())
        print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        """Add water"""
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
