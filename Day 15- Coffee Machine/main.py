MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "coffee": 100
}

money = 0

is_on = True


def get_coffee(coffee, choice):
    for ingredient in resources:
        if resources[ingredient] < coffee["ingredients"][str(ingredient)]:
            print(f"There is not enough {ingredient}.")
            return
    total_paid = get_coins()
    if total_paid == coffee["cost"]:
        print(f"Here is your {choice} ☕")
        print("Enjoy!\n")
    elif total_paid > coffee["cost"]:
        print("Here is $" + str(total_paid - coffee["cost"]) + " in change.")
        print(f"Here is your {choice} ☕")
        print("Enjoy!\n")
    elif total_paid < coffee["cost"]:
        print(f"Sorry, that is not enough money. The {choice} you are trying to buy costs ${coffee['cost']}"
              f". Money refunded.")
        return
    global money
    money += coffee["cost"]
    for ingredient in resources:
        resources[ingredient] -= coffee["ingredients"][str(ingredient)]
    print(money)


def get_coins():
    print("Please insert coins.")
    five_cent_pieces = int(input("How many 5c pieces: "))
    ten_cent_pieces = int(input("How many 10c pieces: "))
    twenty_cent_pieces = int(input("How many 20c pieces: "))
    fifty_cent_pieces = int(input("How many 50c pieces: "))
    dollar_pieces = int(input("How many $1 pieces: "))
    two_dollar_pieces = int(input("How many $2 pieces: "))
    total = (five_cent_pieces * 0.05) + (ten_cent_pieces * 0.1) + (twenty_cent_pieces * 0.2) + \
            (fifty_cent_pieces * 0.5) + dollar_pieces + (two_dollar_pieces * 2)
    return total


while is_on:
    user_choice = input("What coffee would you like? (Espresso/Latte/Cappuccino): ")
    if user_choice.lower() == "off":
        print("Powering down.")
        is_on = False
    elif user_choice.lower() == "report":
        print("Water: " + str(resources["water"]) + "mL")
        print("Milk: " + str(resources["milk"]) + "mL")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: $" + str(money))
    elif (user_choice.lower() == "espresso") or (user_choice.lower() == "latte") or (user_choice.lower() == "cappuccino"):
        drink = MENU[user_choice.lower()]
        get_coffee(drink, user_choice)
