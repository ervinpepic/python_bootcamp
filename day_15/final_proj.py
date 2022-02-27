from resources import resources
from menu import MENU

machine_earn = 0
machine_offline = False


def print_report():
    resources_values = resources.values()
    resources_list = list(resources_values)

    water = f"{resources_list[0]}ml"
    milk = f"{resources_list[1]}ml"
    coffee = f"{resources_list[2]}g"

    format_report = f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nEarn: {machine_earn}"
    print(format_report)


def enter_coins():
    print("Please insert coins.")
    result = int(input("How many quarters? => ")) * 0.25
    result += int(input("How many dimes? => ")) * 0.10
    result += int(input("How many nickles? => ")) * 0.05
    result += int(input("How many pennies? => ")) * 0.01
    return result


def check_resoruces(drink_ingredinet):
    for quantity in drink_ingredinet:
        if drink_ingredinet[quantity] > resources[quantity]:
            print(f"Sorry there is not enough {quantity} :(")
            return False
    return True


def check_price(money_insreted, drink_price):
    if money_insreted >= drink_price:
        result = (money_insreted - drink_price)
        print(f"Here is your ${round(result, 2)} in change.")
        global machine_earn
        machine_earn += drink_price
        return True
    else:
        print("Not enough money.")
        return False


def coffe_serve(drink_name, drink_ingredients):
    for quantity in drink_ingredients:
        resources[quantity] -= drink_ingredients[quantity]
    print(f"Here is your {drink_name} ☕️. Take it!")


while not machine_offline:
    choice = input(
        "What would you like? (espresso/latte/cappuccino) => ").lower()
    if choice == "report":
        print_report()
    elif choice == "off":
        print("Goodbye!")
        machine_offline = True
    else:
        drink = MENU[choice]

        if check_resoruces(drink_ingredinet=drink["ingredients"]):
            price = enter_coins()
            if check_price(money_insreted=price, drink_price=drink["cost"]):
                coffe_serve(choice, drink_ingredients=drink["ingredients"])
