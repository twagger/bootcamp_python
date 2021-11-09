t = (19, 42, 21)
string = "The " + str(len(t)) + " numbers are: "
nb = len(t)
for num in t:
    string += str(num)
    if (nb != 1):
        string += ', '
    nb -= 1
print(string)
