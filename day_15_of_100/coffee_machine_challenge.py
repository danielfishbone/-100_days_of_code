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
liquid_unit = "mL"
solid_unit = "g"
available_water = 1000
available_milk = 500
available_coffee = 300
is_running = True


# TODO: 1 print report of all coffee machine resources
def prompt():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice


def show_resources():
    print(
        f'You have {resources["water"]}{liquid_unit} of water, {resources["milk"]}{liquid_unit} of milk and {resources["coffee"]}{solid_unit} of coffee left')
def compare_resources(_drink):
    _drink_water = _drink["ingredients"]["water"]
    _drink_milk = _drink["ingredients"]["milk"]
    _drink_coffee = _drink["ingredients"]["coffee"]
    

def check_cash(cost):
    quarters = int(input("How many quarters($0.25)?: ")) * 0.25
    dimes = int(input("How many dimes($0.10)?: ")) * 0.1
    nickels = int(input("How many nickels($0.0.05)?: ")) * 0.05
    pennies = int(input("How many pennies($0.01)?: ")) * 0.01
    total_amount = quarters + dimes + nickels + pennies
    if total_amount >= cost:
        return total_amount-cost


print(show_resources())
