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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1: prompt user by asking what they want
# TODO 2: turn off coffee machine
# TODO 3: print report
# TODO 4: check if resources are sufficient
# TODO 5: process coins
# TODO 6: check if transaction is successful

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry, there is not enough {item}")
            return False
        return True

def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns true if payment is accepted or false if insufficient"""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        profit += drink_cost
        return True
    else:
        print("Sorry, That's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


coffee_machine_on = True
while coffee_machine_on:
    coffee_type = input("What would you like? (espresso/latte/cappuccino)\n")
    coffee_machine_on = True
    if coffee_type == "off":
        coffee_machine_on = False
    elif coffee_type == "report":
        for key, value in resources.items():
            print(key, ":", value)
        print(f"Money : ${profit}")
    else:
        drink = MENU[coffee_type]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_type, drink["ingredients"])










