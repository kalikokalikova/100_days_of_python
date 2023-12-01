from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""
while not off
    if drink
        check sufficient resources
        process coins
        if transanction succussful
            add money to profit
            adjust resources
            give back change if necessary
            dispense drink
    if report
        print report
    if off
        exit loop
"""

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    user_input = input(f"What would you like? {menu.get_items()}: ")
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        machine_on = False
    else:
        drink = menu.find_drink(user_input)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)