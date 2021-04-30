class Category :
    

    def __init__ (self,category,amount):
        self.category = category
        self.amount = amount
      
      #methods
     
    def deposit (self,amount):
        self.amount += amount 
        return "You have successfully deposited: {} in {} category".format(self,amount,self.category)


    def budget_balance (self):
        return "This is the current balance: {} ".format(self.amount,self.amount) 


    def check_balance (self,amount):
        return False
         
         
    def withdrawal (self):
       # reverse of deposit
        self.amount - self.amount 
        return " you have successfully withdrew {} in {} category".format(self.amount, self.category)

    def transfer (self,amount,deposit):
        #transfer between two instantiated categories
        return self.withdrawal (amount) + " " + self.deposit(amount)


food_category = Category("Food", 1000)
clothing_category = Category("Clothing", 20)
car_expenses_category = Category("Car expenses", 75000)
appliances_category = Category("Appliances", 6000)

print(food_category.deposit(250))
print(food_category.withdrawal())
print(food_category.budget_balance())
