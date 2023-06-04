# class Resturant:
#     def __init__(self):
#         pass
#         # self.name = name
#         # self.amount =

    

#     def Display_Dictionary(self ):
#         self.food1 = Pizza.food_name
#         self.amount1 = Pizza.Amount
#         self.available1 = Pizza.available
#         self.delivery_time1 = Pizza.delivery_time
        

#         self.food2 = Burger.food_name
#         self.amount2 = Burger.Amount
#         self.available2 = Burger.available
#         self.delivery_time2 = Burger.delivery_time
            
#         Pizza_details =  ("{food} : ${amount}\
#         \nQuantity Left:{available} \nDelivery Time:{time} minutes\n ".format(food = Pizza.food_name, amount = Pizza.Amount, available = Pizza.available, time = Pizza.delivery_time))
        

#         burger_details = ("{food} : ${amount}\
#         \nQuantity Left:{available} \nDelivery Time:{time} minutes\n".format(food = self.food2, amount = self.amount2, available = self.available2, time = self.delivery_time2))
        
#         White_soup_details = ("{food} : ${amount}\
#         \nQuantity Left:{available} \nDelivery Time:{time} minutes\n".format(food = WhiteSoup.food_name, amount = WhiteSoup.Amount, available = WhiteSoup.available, time = WhiteSoup.delivery_time))
        
#         Coconut_Rice_details = ("{food} : ${amount}\
#         \nQuantity Left:{available} \nDelivery Time:{time} minutes\n".format(food = CocoNutRice.food_name, amount = CocoNutRice.Amount, available = CocoNutRice.available, time = CocoNutRice.delivery_time))
        
#         Egusi_soup_details = ("{food} : ${amount}\
#         \nQuantity Left:{available} \nDelivery Time:{time} minutes\n".format(food = EgusiSoup.food_name, amount = EgusiSoup.Amount, available = EgusiSoup.available, time = EgusiSoup.delivery_time))
#         print( Pizza_details, burger_details, White_soup_details, Coconut_Rice_details, Egusi_soup_details, sep= "\n")

       
        
#     # Display_Dictionary()




# class User(Resturant):
#     def __init__(self):
#         self.food_choice = self.food_choice()


#     def food_choice(self, choice):
#         self.food_choice = choice

#     def User_quantity(self, quantity):
#         self.quantity = quantity


# class Food(Resturant):
#     def __init__(self):
#         self.choice  = User.food_choice()
#         self.quanity = User.amount()
#         self.quantity = User.quantity()


# class Pizza(Food):
#     food_name = "Pizza"
#     Amount = 15
#     available = 7
#     delivery_time = 30


# class Burger(Food):
#     food_name = "Burger"
#     Amount = 17
#     available = 5
#     delivery_time = 20

# class CocoNutRice(Food):
#     food_name = "Coconut Rice"
#     Amount = 45
#     available = 10
#     delivery_time = 45


# class EgusiSoup(Food):
#     food_name = "Egusi Soup"
#     Amount = 65
#     available = 15
#     delivery_time = 39

# class WhiteSoup(Food):
#     food_name = "White Soup"
#     Amount = 95
#     available = 15
#     delivery_time = 45

# print(Resturant.Display_Dictionary(Resturant))