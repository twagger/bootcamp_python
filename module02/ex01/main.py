"""Main module"""


def what_are_the_vars(*args, **kwargs):
    """Creates and returns an ObjectC instance from args"""
    # Check if one of the kwarg can conflict with an arg
    max_i = len(args)
    for key, _ in kwargs.items():
        if key.startswith('var_') and key[4:].isdigit():
            if int(key[4:]) < max_i:
                return None
    return ObjectC(*args, **kwargs)


class ObjectC(object):
    """ObjectC class"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        for idx, attr in enumerate(args):
            setattr(self, 'var_' + str(idx), attr)
        for key, value in kwargs.items():
            setattr(self, key, value)


def doom_printer(obj):
    """Doom printer"""
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print(f"{attr}: {value}")
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
