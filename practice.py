# CLASS
class Shirt:
  def __init__(self, shirt_color, shirt_size, shirt_price):
    self.color = shirt_color
    self.size = shirt_size
    self.price = shirt_price


  def change_price(self,new_price):
    self.price = new_price

  def discount(self, discount):
    return self.price* (1 - discount)


new_shirt = Shirt('blue','s', 15)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.price)

new_shirt2 = Shirt('off_white', 'xl', 25)

print(new_shirt2.color)
