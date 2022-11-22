"""Test module"""
from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce
from functools import reduce

# MAP - Test 01
print("\033[1;35m#MAP - Test 1 : ft_map\033[0m")
x = [1, 2, 3, 4, 5]
print(f"{'Standard function':<20}: {list(map(lambda dum: dum + 1, x))}")
print(f"{'Custom function':<20}: {list(ft_map(lambda dum: dum + 1, x))}")

# MAP - Test 02
print("\n\033[1;35m#MAP - Test 2 : ft_map wrong type inside the list\033[0m")
x = [1, 2, 'wrong', 4, 5]
try:
    print(f"{'Standard function':<20}: {list(map(lambda dum: dum + 1, x))}")
except TypeError as exc:
    print(f"{'Error from standard':<20}: {exc}")
try:
    print(f"{'Custom function':<20}: {list(ft_map(lambda dum: dum + 1, x))}")
except TypeError as exc:
    print(f"{'Error from custom':<20}: {exc}")

# MAP - Test 03
print("\n\033[1;35m#MAP - Test 3 : ft_map wrong type instead of list\033[0m")
x = 42
try:
    print(f"{'Standard function':<20}: {list(map(lambda dum: dum + 1, x))}")
except TypeError as exc:
    print(f"{'Error from standard':<20}: {exc}")
try:
    print(f"{'Custom function':<20}: {list(ft_map(lambda dum: dum + 1, x))}")
except TypeError as exc:
    print(f"{'Error from custom':<20}: {exc}")

# MAP - Test 04
print("\n\033[1;35m#MAP - Test 4 : ft_map empty list\033[0m")
x = []
print(f"{'Standard function':<20}: {list(map(lambda dum: dum + 1, x))}")
print(f"{'Custom function':<20}: {list(ft_map(lambda dum: dum + 1, x))}")

# FILTER - Test 01
print("\n\033[1;35m#FILTER - Test 1 : ft_filter\033[0m")
x = [1, 2, 3, 4, 5]
print(f"{'Standard function':<20}: {list(filter(lambda dum: not (dum % 2), x))}")
print(f"{'Custom function':<20}: {list(ft_filter(lambda dum: not (dum % 2), x))}")

# FILTER - Test 02
print("\n\033[1;35m#FILTER - Test 2 : ft_filter wrong type inside the list\033[0m")
x = [1, 2, 3, 'wrong', 5]
try:
    print(f"{'Standard function':<20}: {list(filter(lambda dum: not (dum % 2), x))}")
except TypeError as exc:
    print(f"{'Error from standard':<20}: {exc}")
try:
    print(f"{'Custom function':<20}: {list(ft_filter(lambda dum: not (dum % 2), x))}")
except TypeError as exc:
    print(f"{'Error from custom':<20}: {exc}")

# FILTER - Test 03
print("\n\033[1;35m#FILTER - Test 3 : ft_filter wrong type instead of the list\033[0m")
x = 42
try:
    print(f"{'Standard function':<20}: {list(filter(lambda dum: not (dum % 2), x))}")
except TypeError as exc:
    print(f"{'Error from standard':<20}: {exc}")
try:
    print(f"{'Custom function':<20}: {list(ft_filter(lambda dum: not (dum % 2), x))}")
except TypeError as exc:
    print(f"{'Error from custom':<20}: {exc}")

# FILTER - Test 04
print("\n\033[1;35m#FILTER - Test 4 : ft_filter empty list\033[0m")
x = []
print(f"{'Standard function':<20}: {list(filter(lambda dum: not (dum % 2), x))}")
print(f"{'Custom function':<20}: {list(ft_filter(lambda dum: not (dum % 2), x))}")

# REDUCE - Test 01
print("\n\033[1;35m#REDUCE - Test 1 : ft_reduce\033[0m")
x = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(f"{'Standard function':<20}: {reduce(lambda u, v: u + v, x)}")
print(f"{'Custom function':<20}: {ft_reduce(lambda u, v: u + v, x)}")

# REDUCE - Test 02
print("\n\033[1;35m#REDUCE - Test 2 : ft_reduce with wrong type inside the list\033[0m")
x = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 3.14, 'r', 'l', 'd']
try:
    print(f"{'Standard function':<20}: {reduce(lambda u, v: u + v, x)}")
except TypeError as exc:
    print(f"{'Error from standard':<20}: {exc}")
try:
    print(f"{'Custom function':<20}: {ft_reduce(lambda u, v: u + v, x)}")
except TypeError as exc:
    print(f"{'Error from custom':<20}: {exc}")

# REDUCE - Test 03
print("\n\033[1;35m#REDUCE - Test 2 : ft_reduce with wrong type instead of the list\033[0m")
x = 42
try:
    print(f"{'Standard function':<20}: {reduce(lambda u, v: u + v, x)}")
except TypeError as exc:
    print(f"{'Error from standard':<20}: {exc}")
try:
    print(f"{'Custom function':<20}: {ft_reduce(lambda u, v: u + v, x)}")
except TypeError as exc:
    print(f"{'Error from custom':<20}: {exc}")

# REDUCE - Test 04
print("\n\033[1;35m#REDUCE - Test 2 : ft_reduce empty list\033[0m")
x = []
try:
    print(f"{'Standard function':<20}: {reduce(lambda u, v: u + v, x)}")
except TypeError as exc:
    print(f"{'Error from standard':<20}: {exc}")
try:
    print(f"{'Custom function':<20}: {ft_reduce(lambda u, v: u + v, x)}")
except TypeError as exc:
    print(f"{'Error from custom':<20}: {exc}")
