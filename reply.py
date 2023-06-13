class Restaurant:
    def __init__(self, company_name, company_slogan):
        self.__company_name = company_name
        self.__company_slogan = company_slogan
        self.__menus = []

    def add_menu(self, menu):
        self.__menus.append(menu)

    def remove_menu(self, menu):
        self.__menus.remove(menu)

    def display_company_details(self):
        print(f"Welcome to {self.__company_name} Restaurant!")
        print(f"{self.__company_slogan}")
        print("We have a list of menus you can choose from\n")

    def display_menus(self):
        for menu in self.__menus:
            print("--------------------------------")
            menu.display()


class Menu:
    def __init__(self, name):
        self.__name = name
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def display(self):
        print(f"Menu: {self.__name}")
        for item in self.__items:
            print("`````````````````")
            item.display()


class Order:
    __order_id = 13466

    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def calculate_total(self):
        total = 2.2
        for item in self.__items:
            total += item.food_price
        return total

    def view_order(self):
        print("\n")
        print("Here is your Order Details:")
        for item in self.__items:
            print("Food Name:", item.food_name)
            print("Food Price: $", item.food_price)
            print("-----------------------------------")
        print(f"Your order Id is {self.__order_id + 19} and you have been charged $2.2 VAT")

    def pay_bills(self):
        account_balance = 100
        payment = account_balance - self.calculate_total()
        if payment > 0:
            print(f"Congratulations! Your payment has been made.\nYour balance is {payment}")
        else:
            print(f"You have a balance of ${payment} to complete your payment")


class MenuItem:
    def __init__(self, food_name, food_price, food_time):
        self.__food_name = food_name
        self.__food_price = food_price
        self.__food_time = food_time

    @property
    def food_name(self):
        return self.__food_name

    @property
    def food_price(self):
        return self.__food_price

    @property
    def food_time(self):
        return self.__food_time

    def display(self):
        print("Food Name:", self.__food_name)
        print("Food Price: $", self.__food_price)
        print("Food Delivery Time:", self.__food_time, "minutes")


class Feedback:
    def __init__(self, customer):
        self.__customer_feedback = ""
        self.__customer = customer
        self.__customer_feedback += customer

    def display_customer_feedback(self):
        print("\n")
        print("--------Customer feedback------------")
        print(self.__customer_feedback, "- anonymous")
        print("Your feedback has been received")


print("*********************************************")
restaurant = Restaurant("Tasty", "We deliver the best taste")
restaurant.display_company_details()

menu1 = Menu("Breakfast Menu")
menu2 = Menu("Lunch Menu")
menu3 = Menu("Dinner Menu")
menu4 = Menu("Snacks Menu")

restaurant.add_menu(menu1)
restaurant.add_menu(menu2)
restaurant.add_menu(menu3)
restaurant.add_menu(menu4)

food1 = MenuItem("Pizza", 15, 45)
food2 = MenuItem("Chicken Sandwich", 7, 35)
food3 = MenuItem("Rice", 24, 5)
food4 = MenuItem("Egg Sauce", 5, 23)

menu1.add_item(food1)
menu2.add_item(food2)
menu3.add_item(food3)
menu4.add_item(food4)
restaurant.display_menus()
# menu1.display()
restaurant.remove_menu(menu1)

restaurant.display_menus()

order = Order()
order.add_item(food1)
order.add_item(food2)

total = order.calculate_total()

order.view_order()
print("\nYour total bill is:", total)
order.pay_bills()

message = input("Do you wish to give feedback: ").lower()
if message == "yes":
    customer_message = input("Enter your feedback: ").lower()
else:
    print('Thanks for purchasing with us')
person = Feedback(customer_message)
person.display_customer_feedback()
