from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
my_menu = Menu()
m_machine = MoneyMachine()

latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)

is_running = True

# TODO : 1 prompt user for choice of drink
while is_running:
    choice = input("What would you like? (espresso/latte/cappuccino/):").lower()
    if choice == "off":
        is_running = False
    elif choice == "report":
        cm.report()
    elif choice == "cash":
        m_machine.report()
    elif my_menu.find_drink(choice):
        if cm.is_resource_sufficient(my_menu.find_drink(choice)):
            if m_machine.make_payment(my_menu.find_drink(choice).cost):
                cm.make_coffee(my_menu.find_drink(choice))



