"""Test module"""
from generator import generator


def main():
    """Main program"""
    print("\n\033[1;35m--Test 0: Text is not string--\033[0m")
    text = 42
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)

    text = "Le Lorem Ipsum est simplement du faux texte."

    print("\n\033[1;35m--Test 1: Text with sep ' ' and no option--\033[0m")
    for word in generator(text, sep=" "):
        print(word)

    print("\n\033[1;35m--Test 2: Text with sep ' ' and shuffle option--\033[0m")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    
    print("\n\033[1;35m--Test 3: Text with sep ' ' and ordered option--\033[0m")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)

    text = "Le Le Lorem Ipsum est simplement du du Ipsum faux texte."
# Pas dans le bon ordre
    print("\n\033[1;35m--Test 4: Text with sep ' ' and unique option--\033[0m")
    for word in generator(text, sep=" ", option="unique"):
        print(word)


main()
