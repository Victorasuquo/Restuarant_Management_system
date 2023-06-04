class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menus = []

    def add_menu(self, menu):
        self.menus.append(menu)

    def remove_menu(self, menu):
        self.menus.remove(menu)


class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


# Create a restaurant
restaurant = Restaurant("My Restaurant")

# Create menus
menu1 = Menu("Breakfast Menu")
menu2 = Menu("Lunch Menu")

# Add menus to the restaurant
restaurant.add_menu(menu1)
restaurant.add_menu(menu2)

# Create items
item1 = Item("Eggs and Bacon", 10)
item2 = Item("Sandwich", 8)
item3 = Item("Burger", 12)

# Add items to menus
menu1.add_item(item1)
menu1.add_item(item2)
menu2.add_item(item3)

# Create an order
order = Order(restaurant)

# Add items to the order
order.add_item(item1)
order.add_item(item3)

# Calculate the total bill
total = order.calculate_total()
print("Total Bill:", total)
