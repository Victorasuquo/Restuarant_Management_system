import random
random_number = random.randint(1, 9)
print(random_number)
menu_box = False


class Restaurant:
    def __init__(self, company_name, company_slogan):
        self.company_name = company_name
        self.company_slogan = company_slogan
        self.menus = []
        self.cutomer_feed = []

    def add_menu(self, menu):
        self.menus.append(menu)

    def remove_menu(self, menu):
        self.menus.remove(menu)

    def add_feed(self, feed):
        self.cutomer_feed.append(feed)

    def display_company_details(self):
        print('----------- ` COMPANY DETAILS  `-------------')
        print(f"Welcome to {self.company_name} Restaurant!")
        print(f"...{self.company_slogan}")
        print("We have a list of options you can choose from\n")

    def display_menus(self):
        for menu in self.menus:
            print("--------------------------------")
            menu.display()

    def display_cutomer_feedback(self):
        for feeds in self.cutomer_feed:
            print('` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ` ')
            feeds.display_customer_feed()
        


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

    def display_customer_feed(self):
        print("\n")
        print("--------Customer feedback------------")
        print(self.customer_feedback, " - ananymous")
        print("your feedback has been received")


print("*********************************************")
restaurant_name = input("Enter your Restaurant Name: ").title() 
restaurant_sogan = input("Enter your company slogan: ").lower()



restaurant = Restaurant(restaurant_name, restaurant_sogan)
print()
restaurant.display_company_details()
menu_box = True

if menu_box:
    one = "1. Create Menu "
    two = "2. Add Menu "
    three = "3. Remove Menu"
    four = "4. Add item"
    five = "5. Remove item"
    six = "6. Order "
    seven = "7. View Restuarant"
    eight = "8. Feedback "
    nine = "9. Feedback "
    decorator = "-------------------------------------"
    print(one, two, three, four, five, six, seven,eight, nine,decorator, sep = "\n")

while True:
        # try:
    response = int(input("Select Number to Proceed:  "))
    # except ValueError:
    #     print("Please make sure you Enter a Number to proceed !")
    if response == "exit":
        break
    if response == 1:
        while True:
            menu_name = input("what should your menu sound like: ")
            if menu_name == "done":
                options = "1.Exit \n2.View menu "
                print(options)
                view_menu = int(input())
                if view_menu == 1:
                   break
                menu_box = True
                if view_menu == 2:
                    restaurant.display_menus()
                    break
                menu_box = True
            menuss = Menu(menu_name)
            restaurant.add_menu(menuss)
            

    if response == 2:
        while True:
            ad_name = input("what would you like The Menu to be called like: ")
            if ad_name == "done":
                add_options = "1.Exit \n2.View added Menu "
                print(add_options)
                view_added_menu = int(input())
                if view_added_menu == 1:
                   break
                menu_box = True
                if view_added_menu == 2:
                    restaurant.display_menus()
                    break
                menu_box = True
            else:    
                ad_m_name = Menu(ad_name)
                restaurant.add_menu(ad_m_name)
            
    if response == 3:
        remove = input("Which Menu do you want to remove: ")
        if remove == "done" :
            remove_options = "1.Exit \n2.View Menu Removed: "
            print(remove_options)
            view_removed_reponse = int(input())
            if view_removed_reponse == 1:
                menu_box = True
               
            if view_removed_reponse == 2:
                restaurant.display_menus()
                menu_box = True
                
        else:
            try:
                removed_menu = None
                for menu in restaurant.menus:
                    if menu.name == remove:
                        removed_menu = menu
                        break

                if removed_menu is not None:
                    restaurant.remove_menu(removed_menu)
                    print(f"The menu {remove} has been succesfully removed ! ")
                else:
                    print("please make sure the Menu you wish to remove is in the menu list already! \nClick 2 to add to Menu ")
            
            except ValueError:
                print("please make sure the Menu you wish to remove is in the menu list already! \nClick 2 to add to Menu ")
                menu_box = True
       

    if response == 4:
        while True:
            print("Check out the available menu and add items to them \nSelect menu: ")
            restaurant.display_menus()
            add_item_menu  = input("")
            if add_item_menu == "done":
                break
            adding_item = None
            for item_x in restaurant.menus:
                if item_x.name == add_item_menu:
                    adding_item = item_x
                    break
            if adding_item is not None:
                let_item = input("Enter item name: ")
                let_item_price = int(input("Enter item amount in $: "))
                let_item_time = input("Enter item delivery time: ")
                adding_instance = MenuItem(let_item,let_item_price, let_item_time)
                adding_item.add_item(adding_instance)
            # restaurant.display_menus()
                print("Enter Menu Name to add to menu !")
            menu_box = True


    if response == 5:
        while True:
            print("Check out The available Menu and remove items from it \nSelect menu to Remove Item: ")
            restaurant.display_menus()
            remove_item_menu = input("")
            if remove_item_menu == "done":
                break
            removing_item = None
            for items_z in restaurant.menus:
                if items_z.name == remove_item_menu:
                    removing_item = items_z
                    break
            if removing_item is not None:
                listings = None
                re_items = ("Enter the Item name you want to remove: ")
                for item in removing_item:
                    if item.food_name == re_items:
                        listings = re_items
                        removing_item.remove_item(listings)
                        break

            menu_box = True
    if response == 6:
        while True:
            print(f"Here are the items availble at {restaurant_name} Restuarant. \nOrder now ! at 30%  discount :) ")
            more_order_details = "1.Add Order \n2.Remove Order \n3.View order\n4.Pay bills \n5.Exit"

            print(more_order_details)
            print("--------------------------------")
            choice  = input()
            if choice == 1:
                restaurant.display_menus()
                treat = input("select item to order: ")
                if treat == "done":
                    break
                else:
                    ordering = Order()
                    ordering.add_item(treat)
            
            total = ordering.calculate_total()











    if response == 7:
        print("\n")
        restaurant.display_company_details()
        restaurant.display_menus()
        restaurant.display_cutomer_feedback()


    if response == 8:
        message = input("Do you wish to give a feedback: ").lower()
        if message == "yes":
            customer_message = input("Enter your feedback: ").lower()
            print("We have recieved your message and it wil be delivered")
            print("- - - - - - - - - - - - - - - - - - - - - -")
            person = Feedback(customer_message)
            restaurant.add_feed(person)
            person.display_customer_feed()
            menu_box = True

    if menu_box:
            print("\n")
            one = "1. Create Menu "
            two = "2. Add Menu "
            three = "3. Remove Menu"
            four = "4. Add item"
            five = "5. Remove item"
            six = "6. Pay bills "
            seven = "7. Order"
            eight = "8. View Restuarant "
            nine = "9. Feedback "
            decorator = "-------------------------------------"
            print(one, two, three, four, five, six, seven,eight, nine,decorator, sep = "\n")

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


order = Order()
order.add_item(food1)
order.add_item(food2)

total = order.calculate_total()

order.view_order()
print("\nYour total bill is: ", total)
order.pay_bills()


