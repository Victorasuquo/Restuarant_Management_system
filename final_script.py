class Restaurant:
    def __init__(self, company_name, company_slogan):
        self.company_name = company_name
        self.company_slogan = company_slogan
        self.menus = []

    def add_menu(self, menu):
        self.menus.append(menu)

    def remove_menu(self, menu):
        self.menus.remove(menu)

    def display_company_details(self):
        print(f"Welcome to {self.company_name} Restaurant!")
        print(f"{self.company_slogan}")
        print("We have a list of menus you can choose from\n")

    def display_menus(self):
        for menu in self.menus:
            print("--------------------------------")
            menu.display()


class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display(self):
        print(f"Menu: {self.name}")
        for item in self.items:
            print("`````````````````")
            item.display()


class Order:

    order_id = 13466

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 2.2
        for item in self.items:
            total += item.food_price
        return total

    def view_order(self):
        print("\n")
        print("Here is your Order Details:")
        for item in self.items:
            print("Food Name:", item.food_name)
            print("Food Price: $", item.food_price)
            print("-----------------------------------")
        print(f"your orer Id is {self.order_id + 19} and you have been charged $2.2 VAT ")
              
    def pay_bills(self):
        self.acount_balance = 100
        payment = self.acount_balance - total
        if payment > 0:
            print(f"Congratulations your payment have been made. \nYour balance is  {payment}")
        else:
            print(f"you have more ${payment} to complete your payment")
        

class MenuItem:
    def __init__(self, food_name, food_price, food_time):
        self.food_name = food_name
        self.food_price = food_price
        self.food_time = food_time

    def display(self):
        print("Food Name:", self.food_name)
        print("Food Price: $", (self.food_price) )
        print("Food Delivery Time:", self.food_time, "minutes")


class Feedback:
    def __init__(self, customer):
        self.customer_feedback = ""
        self.cutomer = customer
        self.customer_feedback +=customer

    def display_cutomer_feed(self):
        print("\n")
        print("--------Customer feedback------------")
        print(self.customer_feedback, " - ananymous")
        print("your feedback has been received")


print("*********************************************")
restaurant = Restaurant("Tasty", "We deliver the best taste")
restaurant.display_company_details()

menu1 = Menu("Breakfast Menu")
menu2 = Menu("Lunch Menu")
menu3 = Menu("Dinner Menu")
menu4 = Menu("snacks Menu")

restaurant.add_menu(menu1)
restaurant.add_menu(menu2)
restaurant.add_menu(menu3)
restaurant.add_menu(menu4)

food1 = MenuItem("Pizza", 15, 45)
food2 = MenuItem("Chicken Sandwich", 7, 35)
food3 = MenuItem("Rice", 24, 5)
food4  = MenuItem("egg sauce", 5, 23)

menu1.add_item(food1)
menu2.add_item(food2)
menu3.add_item(food3)
menu4.add_item(food4)

menu1.display()

restaurant.display_menus()

order = Order()
order.add_item(food1)
order.add_item(food2)

total = order.calculate_total()

order.view_order()
print("\nYour total bill is: ", total)
order.pay_bills()

message = input("Do you wish to give a feedback ").lower()
if message == "yes":
    customer_message = input("Enter your feedback: ").lower()
else:
    print('thanks for purchasing with us')
person = Feedback(customer_message)
person.display_cutomer_feed()