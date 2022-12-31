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
    "coffee": 100,
}
liquid_unit = "mL"
solid_unit = "g"
available_water = 1000
available_milk = 500
available_coffee = 300
available_cash = 0

is_running = True


# TODO: 1 print report of all coffee machine resources
def prompt():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return choice


def show_resources():
    return (
        f'You have {resources["water"]}{liquid_unit} of water, {resources["milk"]}{liquid_unit} of milk and {resources["coffee"]}{solid_unit} of coffee and ${available_cash}left')


def compare_resources(_coffee):
    statement = ""
    if resources["water"] < MENU[_coffee]["ingredients"]["water"]:
        statement += "insufficient water"
    if resources["milk"] < MENU[_coffee]["ingredients"]["milk"]:
        if len(statement) > 0:
            statement += ", "
        statement += "insufficient milk"
    if resources["coffee"] < MENU[_coffee]["ingredients"]["coffee"]:
        if len(statement) > 0:
            statement += ", "
        statement += "insufficient coffee"
    if len(statement) <= 0:
        return True, "available"
    else:
        return False, statement


def check_cash(_coffee):
    _cost = MENU[_coffee]["cost"]
    quarters = int(input("How many quarters($0.25)?: ")) * 0.25
    dimes = int(input("How many dimes($0.10)?: ")) * 0.1
    nickels = int(input("How many nickels($0.0.05)?: ")) * 0.05
    pennies = int(input("How many pennies($0.01)?: ")) * 0.01
    total_amount = quarters + dimes + nickels + pennies
    if total_amount >= _cost:
        return _cost, (total_amount - _cost)
    else:
        return -1, (total_amount - _cost)


def sell_coffee(_coffee):
    global available_cash
    proceed_flag, statement = compare_resources(_coffee)
    if not proceed_flag:
        print(f"I'm sorry we have {statement} at the moment")
    else:
        cost, change = check_cash(_coffee)
        if cost >= 0:
            available_cash += cost
            resources["water"] -= MENU[_coffee]["ingredients"]["water"]
            resources["milk"] -= MENU[_coffee]["ingredients"]["milk"]
            resources["coffee"] -= MENU[_coffee]["ingredients"]["coffee"]
            print(f'Here is your {_coffee}, you have a change of ${"%.2f"%change}')
        else:
            print(f"Oops!, insufficient funds, you're short by ${abs(change)}")


while is_running:
    selection = prompt()
    if selection == "report":
        print(show_resources())
    elif selection == "off":
        is_running = False
    else:
        sell_coffee(selection)
