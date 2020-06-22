class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color= shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self,new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


# shirt_one = Shirt('red', 'M', 'long_sleeved', 45)
# shirt_two = Shirt('orange', 'S', 'short_sleeved', 30)
#
#
# print(shirt_two.price)
# print(shirt_one.color)
