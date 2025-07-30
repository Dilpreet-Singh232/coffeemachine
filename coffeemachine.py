MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on=True


choice=input("what would you like to have ? espresso/latte/cappucino").lower()
    

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def pay(cost):
      print("please insert coins:")
      quarter= int(input("how many quarters:"))
      dimes=int(input("how many dimes:"))
      nickles= int(input("how many nickles:"))
      pennies=int(input("how many pennies:"))
      calculate = ((quarter*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01))

      if calculate>=cost:
            change = calculate-cost
            print(f"Here is your CHANGE: {change:.2f}")
            return True
      else :
            print(f"not enough money BRO,{calculate}")
            return False
        


def makecoffee(drink_name,order_ingredients):
         for item in order_ingredients:
            resources[item] -= order_ingredients[item]
         print(f"Here is your {drink_name} ☕️. Enjoy!")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            
            if pay(drink["cost"]):
                makecoffee(choice, drink["ingredients"])




      
      


