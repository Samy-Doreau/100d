from art import logo
from data import MENU, resources


def ask_question_with_set_answers(question_text, expected_answers):
    question_cleared = False
    while not question_cleared:
        answer = input(f"{question_text} \n > ")
        if answer.lower() in expected_answers:
            question_text = True
            return answer.lower()
        else:
            print("Incorrect input \n")


def ask_question_with_int_answer_type(question_text):
    question_cleared = False
    while not question_cleared:
        answer = input(f"{question_text} \n > ")
        if answer.isnumeric():
            question_text = True
            return int(answer)
        else:
            print("Incorrect input \n")


def print_report(resources):
    output_text = ""
    for key in resources:
        if resources[key]['unit_position'] == "aft":
            output_text += f"{key.capitalize()} : {resources[key]['amount']}{resources[key]['unit']} \n"
        else:
            output_text += f"{key.capitalize()} : {resources[key]['unit']}{resources[key]['amount']} \n"
    return print(output_text)


def sufficient_funds_provided(amount_provided, item_requested):
    # Fetch value of requested item
    item_cost = MENU[item_requested]['cost']
    return item_cost <= amount_provided


def sufficient_resources_available(resources, item_requested):
    # Fetch resources required to make item
    item_receipe = MENU[item_requested]['ingredients']
    # Define criteria
    criteria = (
        item_receipe['water'] <= resources['water']['amount'] and
        item_receipe['milk'] <= resources['milk']['amount'] and
        item_receipe['coffee'] <= resources['coffee']['amount']
    )

    return criteria


def take_payment(amount):
    number_of_quarters = 0
    number_of_dimes = 0
    number_of_nickels = 0
    number_of_pennies = 0

    number_of_quarters = ask_question_with_int_answer_type(
        'Number of quarters \n > ')
    print(
        f"\n Amount provided: ${amount + 0.25 * number_of_quarters + 0.1 * number_of_dimes + 0.05 * number_of_nickels + 0.01 * number_of_pennies}")
    number_of_dimes = ask_question_with_int_answer_type(
        'Number of dimes \n > ')
    print(
        f"\n Amount provided: ${amount + 0.25 * number_of_quarters + 0.1 * number_of_dimes +0.05 * number_of_nickels + 0.01 * number_of_pennies}")
    number_of_nickels = ask_question_with_int_answer_type(
        'Number of nickels \n > ')
    print(
        f"\n Amount provided: ${amount + 0.25 * number_of_quarters + 0.1 * number_of_dimes +0.05 * number_of_nickels + 0.01 * number_of_pennies}")
    number_of_pennies = ask_question_with_int_answer_type(
        'Number of pennies \n > ')
    print(
        f"\n Amount provided: ${amount + 0.25 * number_of_quarters + 0.1 * number_of_dimes +0.05 * number_of_nickels + 0.01 * number_of_pennies}")

    return amount + 0.25 * number_of_quarters + 0.1 * number_of_dimes + 0.05 * number_of_nickels + 0.01 * number_of_pennies


def register_paid_amount(resources, paid_amount, requested_item):
    requested_item_cost = MENU[requested_item]['cost']
    if paid_amount > requested_item_cost:
        resources['money']['amount'] = resources['money'].get(
            'amount', 0) + requested_item_cost
        print(
            f"Purchase successful, refunding {paid_amount - requested_item_cost}")


def make_item(requested_item, resources):
    # Only run if resources are sufficient
    item_recipe = MENU[requested_item]['ingredients']
    resources['milk']['amount'] = resources['milk'].get(
        'amount', 0) - item_recipe['milk']
    resources['water']['amount'] = resources['water'].get(
        'amount', 0) - item_recipe['water']
    resources['coffee']['amount'] = resources['coffee'].get(
        'amount', 0) - item_recipe['coffee']

    print(f"Enjoy your {requested_item}")


def replenish_stocks(resources):
    amount_of_water = ask_question_with_int_answer_type(
        'How much water do you want to add (in ml) ? \ > ')
    amount_of_milk = ask_question_with_int_answer_type(
        'How much milk do you want to add (in ml) ? \ > ')
    amount_of_coffee = ask_question_with_int_answer_type(
        'How much coffee do you want to add (in g) ? \ > ')
    restock_summary = f"Please confirm the following restock plan : \n Water : + {amount_of_water} ml \n Milk : + {amount_of_milk} ml \n Coffee : {amount_of_coffee} g \n y/n \ > "
    restock_confirm_answer = ask_question_with_set_answers(
        restock_summary, ['y', 'n'])
    if restock_confirm_answer == 'y':
        resources['water'] = resources.get('water', 0) + amount_of_water
        resources['milk'] = resources.get('milk', 0) + amount_of_milk
        resources['coffee'] = resources.get('coffee', 0) + amount_of_coffee

        print("Many thanks, the current inventory is : \n")
        print_report(resources)


def coffee_machine():
    print(logo)
    machine_off = False
    item_selection_promt = "Welcome to our coffee machine, please enter your selection (espresso / latte / capuccino) \n > "
    while not machine_off:

        selected_item = ask_question_with_set_answers(
            item_selection_promt, ['espresso', 'latte', 'cappuccino', 'add_stuff', 'report', 'off'])
        if selected_item == 'add_stuff':
            replenish_stocks(resources)
        elif selected_item == 'report':
            print_report(resources)
        elif selected_item == 'off':
            machine_off = True
        else:
            is_sufficient_resources = sufficient_resources_available(
                resources, selected_item)
            if is_sufficient_resources:

                print(
                    f"You have selected : {selected_item} \n | cost : {MENU[selected_item]['cost']} \n Please provide payment")
                amount_paid = take_payment(0)
                is_sufficient_funds_provided = sufficient_funds_provided(
                    amount_paid, selected_item)
                while not is_sufficient_funds_provided:
                    print("insufficient funds provided, please provide more funds \n")
                    amount_paid = take_payment(amount_paid)
                register_paid_amount(resources, amount_paid, selected_item)
                make_item(selected_item, resources)

            else:
                print(
                    "Unfortunately, we are unable to make this for you at the moment ! \n Sorry !! ")


coffee_machine()
