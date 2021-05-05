from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    my_coffee_machine = CoffeeMaker()
    my_money_machine = MoneyMachine()
    my_menu = Menu()
    machine_off = False
    while not machine_off:
        options = my_menu.get_items()
        choice = input(f"Which drink would you like ({options}) ? \n > ")
        if choice == 'report':
            my_coffee_machine.report()
            my_money_machine.report()
        elif choice == 'off':
            machine_off = True
        else:
            selected_drink = my_menu.find_drink(choice)
            if selected_drink is not None:
                # Check if sufficient resources
                is_resource_sufficient = my_coffee_machine.is_resource_sufficient(
                    selected_drink)
                if is_resource_sufficient:
                    # Take payment
                    is_paid_amount_sufficient = False
                    while not is_paid_amount_sufficient:
                        is_paid_amount_sufficient = my_money_machine.make_payment(
                            selected_drink.cost)

                    # Once enough money provided, and transaction registered, make coffee
                    my_coffee_machine.make_coffee(selected_drink)


coffee_machine()
