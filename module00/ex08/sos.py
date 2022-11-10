"""This module encodes a string into Morse code"""
import sys


# Morse dictionnary
morse = {
    "A": ".-",
    "B": "----",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}

def main():
    """Main program"""
    if len(sys.argv) >= 2:
        message = ' '.join(sys.argv[1:])
        morsed = [morse[letter.upper()]
                for letter in message if letter.upper() in morse]
        wrong_char = [char for char in message if char.upper() not in morse]
        if len(wrong_char) > 0:
            print("ERROR")
        else:
            print(*morsed, sep=' ')


main()
