class Food:

    # Keep Track of the Menu
    full_menu = set()

    def __init__(self, food_name, price):
        self.food_name = food_name
        self.price = price

        if self.food_name not in Food.full_menu:
            Food.full_menu.add(self.food_name)

    # No need for this. full_menu is already a variable of entire class.
    # @property
    # def full_menu(self):
    #     pass


food1 = Food("Ice Cream", 5)
print(list(Food.full_menu))
