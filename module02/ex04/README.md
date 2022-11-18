# Minipack library

## Included functions

### Loading bar

The loading bar print a loading bar, including progression percentage, elapsed and remaning time, estimated time, number of items.

Usage :
```python
any_list = range(1000)
for elem in ft_progress(any_list):
    # You code here
    # ...
```

### logguer

This is a specific decorator you can add to your function to log their execution time in a file.

The log is located in the current directory with the name `trace.log`.

Usage :
```python
class CoffeeMachine():
    """Coffe machine"""
    water_level = 100

    @log
    def start_machine(self):
        """Start machine"""
        # Your code here
        # ...
```
