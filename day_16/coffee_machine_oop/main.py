from random import choice
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_offline = False


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while not is_offline:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}): ")
    if choice == "report":
        money_machine.report()
        coffee_maker.report()
    elif choice == "off":
        is_offline = True
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            cost = drink.cost
            money_machine.make_payment(cost)
            if money_machine:
                coffee_maker.make_coffee(drink)