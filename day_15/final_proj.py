
from resources import resources
from menu import MENU    

def print_report():
    resource_keys = resources.keys()
    resource_keys_list = list(resource_keys)
    resources_values = resources.values()
    resources_list = list(resources_values)
    water = f"{resources_list[0]}ml"
    milk = f"{resources_list[1]}ml"
    coffee = f"{resources_list[2]}g"
    format_report = f"{resource_keys_list[0]}: {water}\n{resource_keys_list[1]}: {milk}\n{resource_keys_list[2]}: {coffee}"
    print(format_report)

def enter_coins():
    quareters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    print("Please insert coins.")
    q = int(input("How many quarters? => "))
    d = int(input("How many dimes? => "))
    n = int(input("How many nickles? => "))
    p = int(input("How many pennies? => "))
    result = quareters * q + dimes * d + nickles * n + pennies * p
    return result

def check_resoruces(drink, resoruces):
    if drink["ingredients"]["water"] > resoruces["water"]:
        print("Sorry there is not enough water :(")
        return False
    else:
        resources["water"] -= drink["ingredients"]["water"]
    if "milk" in drink["ingredients"]:
        if drink["ingredients"]["milk"] > resoruces["milk"]:
            print("Sorry there is not enough milk :(")
            return False
        else:
            resources["milk"] -= drink["ingredients"]["milk"]
    if drink["ingredients"]["coffee"] > resoruces["coffee"]:
        print("Sorry there is not enough coffee :(")
        return False
    else:
        resources["coffee"] -= drink["ingredients"]["coffee"]
        return True

def check_price(drink, price):
    if drink["cost"] > price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        result = price - drink["cost"]
        print(f"Here is your change: {round(result, 2)}")
        return True

machine_offline = False


while not machine_offline:
    choice = input("What would you like? (espresso/latte/cappuccino) => ").lower()
    if choice == "report":
        print_report()
    elif choice == "off":
        print("Goodbye!")
        machine_offline = True
    else:
        drink = MENU[choice]

        drink_resource = check_resoruces(drink=drink, resoruces=resources)
        if drink_resource:
            drink_price = check_price(drink=drink, price=enter_coins())
            if drink_price:
                print(f"Here is your {choice}. Enjoy!")
            else:
                machine_offline = True
        else:
            machine_offline = True

