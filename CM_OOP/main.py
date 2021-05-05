from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    my_coffee_machine = CoffeeMaker()
    my_money_machine = MoneyMachine()
    my_menu = Menu()

    my_coffee_machine.report()


coffee_machine()
