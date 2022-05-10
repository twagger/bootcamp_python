from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce

print("\033[1;35m# Test 1 : ft_map\033[0m")
x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
print(ft_map(None, x))
print(list(ft_map(lambda dum: dum + 1, x)))
# Expected output : [2, 3, 4, 5, 6]

print("\n\033[1;35m# Test 2 : ft_filter\033[0m")
print(ft_filter(lambda dum: not (dum % 2), x))
print(list(ft_filter(lambda dum: not (dum % 2), x)))
#Expected output : [2, 4]

print("\n\033[1;35m# Test 3 : ft_reduce\033[0m")
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
# Expected output : Hello world
