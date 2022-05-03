from generator import generator

print("\n\033[1;35m--{}: {}--\033[0m".format("Test 0", "Text is not string"))
text = 42
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

text = "Le Lorem Ipsum est simplement du faux texte."

print("\n\033[1;35m--{}: {}--\033[0m".format("Test 1", "Text with sep ' ' and no option"))
for word in generator(text, sep=" "):
    print(word)

print("\n\033[1;35m--{}: {}--\033[0m".format("Test 2", "Text with sep ' ' and shuffle option"))
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print("\n\033[1;35m--{}: {}--\033[0m".format("Test 3", "Text with sep ' ' and ordered option"))
for word in generator(text, sep=" ", option="ordered"):
    print(word)

text = "Le Le Lorem Ipsum est simplement du du Ipsum faux texte."

print("\n\033[1;35m--{}: {}--\033[0m".format("Test 4", "Text with sep ' ' and unique option"))
for word in generator(text, sep=" ", option="unique"):
    print(word)