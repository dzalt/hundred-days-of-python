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

profit = 0


def check_resource(ingredients):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            print(f"Sorry there's not enough {i}.")
            return False
    
    return True

def insert_coin():
    # quarters = 0.25, dimes = 0.10, nickles = 0.05, pennies = 0.01
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def check_coin(cost, paid):
    if cost > paid:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif cost < paid:
        print(f"Here's ${paid - cost} in change.")
    
    return True

def make_coffee(ingredients, resources):
    for i in ingredients:
        resources[i] -= ingredients[i]
    
    print("Enjoy your coffee.")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]

        # check ingredient -> insert money -> check money -> make coffee

        if check_resource(drink["ingredients"]):
            coins = insert_coin()
            if check_coin(drink["cost"], coins):
                profit += drink["cost"]
                make_coffee(drink["ingredients"], resources)
