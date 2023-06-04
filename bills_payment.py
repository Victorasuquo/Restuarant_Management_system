

#restuarant class
class Restuarant:
    def __init__(self, company_name):
        self.company_name = company_name
        self.food_menu  = []
    
    def add_f_menu(self, menu):
        # self.menu = menu
        self.food_menu.append(menu)

    # def add_menu(self, menu):
    #     self.food_menu.append(menu)

    def remove_menu(self, menu):
        self.food_menu.remove(menu)

    # def details(self):
    #     # self.company_name
    #     return self.Display_details(self)


    # def Display_details(self):
    #     pass
    #     # print(food_menu)
        # return "{name} Company Restuarant !  \ncheck out our food menu \n".format(name = Restuarant.company_name).upper()

class Menu(Restuarant):
    def __init__(self, name):
        self.m_name = name
        self.foods_items = []
        

    def add_Menu(self, new_menu):
        self.new_menu = new_menu


    def remove_Remove(self, new_menu):
        self.new_menu = new_menu
        
            
class Food(Restuarant):
    def __init__(self, food_name, food_price, food_delivery_time):
        self.food_name = food_name
        self.food_price = food_price
        self.time = food_delivery_time

class Order(Menu):
    def __init__(self, Restuarant):
        self.restuarant = Restuarant
        self.Food_items = []

    def add_food_item(self, food_item):
        self.Food_items.append(food_item)

    def remove_food_item(self, food_item):
        self.Food_items.remove(food_item)

    def calculate_total(self):
        total_cost = 0
        for food in self.Food_items():
            total_cost += food.food_price
        return total_cost



#object of the Restuarant class
comp_name = input("Enter your company Name: ")
company = Restuarant(comp_name)

# print(Restuarant.details(Restuarant))

# create menu
menu_numb = int(input("How many menu does your Restuarant have: "))
x = 1
while  x <= menu_numb:
    menu_name = input(f"Enter Menu {x} name: example 'breakfast Menu: ")
    menu_create = "menu"+str(menu_numb)
    menu_creates = Menu(menu_name)

    x += 1
    company.add_f_menu(menu=menu_creates)
# print(company.food_menu)
    while True:
        food_name = input("Enter food name: ")
        if food_name.lower() == "done":
            break
        food_amount = input("Enter food amount: ")
        food_time = input("Enter the food Delivery time in minutes: ")

        food = Food(food_name, food_amount, food_time)
        menu_creates.add_Menu(food)