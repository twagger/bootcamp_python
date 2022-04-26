class Recipe:

    def __init__(self, name, cooking_lvl, ingredients,
                 recipe_type, description=''):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        if type(self.ingredients) is not list:
            raise TypeError
        txt = ""
        txt += "{}: \n".format(self.name)
        txt += "> Level : {} / Type : {}\n".format(self.cooking_lvl,
                                                 self.recipe_type)
        txt += "> Ingredients : \n"
        for ingredient in self.ingredients:
            txt += "  - {}\n".format(ingredient)
        txt += "> Description : \n - {}".format(self.description)
        return txt
