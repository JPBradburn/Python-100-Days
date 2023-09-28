from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
c_machine = CoffeeMaker()
m_machine = MoneyMachine()

is_on = True
menu_list = menu.get_items_as_list()

while is_on:
    choice = input("What would you like? (" + menu.get_items()[:-1] + "): ").lower()
    if choice == "report":
        c_machine.report()
        m_machine.report()
    elif choice == "off":
        print("Powering down.")
        is_on = False
    elif choice in menu_list:
        drink = menu.find_drink(choice)
        if c_machine.is_resource_sufficient(drink) and m_machine.make_payment(drink.cost):
            c_machine.make_coffee(drink)
    else:
        print("Please choose a valid drink.")
