"""GOT module"""


class GotCharacter:
    """GOT character class"""

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family. \
Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def __str__(self):
        card = (f'Name: {self.first_name} {self.family_name}\n'
                f'Status: {"alive" if self.is_alive else "dead"}\n'
                f'Words: {self.house_words}')
        return card

    def print_house_words(self):
        """Prints the words of a house"""
        print(self.house_words)

    def die(self):
        """Kills a character"""
        self.is_alive = False
