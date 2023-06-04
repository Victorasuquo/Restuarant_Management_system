

#restuarant class
class Restuarant:
    def __init__(self, company_name):
        self.company_name = company_name
        Restuarant.company_name = ""
        self.foods_items = {}

    def details(self):
        self.company_name += comp_name
        return self.Display_details(Restuarant)


    def Display_details(self):
        print(self.foods_items)
        return "{name} Company Restuarant !  \ncheck out our food menu \n".format(name = self.company_name).upper()

class Menu(Restuarant):
    def __init__(self, food_name, amount, time):
        self.food_name = food_name
        self.amount = amount
        self.quantity = time
        

    def add_Menu(self, new_menu):
        self.new_menu = new_menu



    def remove_Remove(self, new_menu):
        self.new_menu = new_menu
        
            
# class Item():



 





class Order(Menu):
    def __init__(self):
        pass


comp_name = input("Enter your company Name: ")
company = Restuarant(comp_name)

print(Restuarant.details(Restuarant))

while True:
    food_name = input("Enter food name: ")
    if food_name == "done":
        break
    food_amount = input("Enter food amount: ")
    food_time = input("Enter the food Delivery time in minutes: ")

food = Menu(food_name, food_amount, food_time)
