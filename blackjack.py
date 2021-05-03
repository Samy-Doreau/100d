from art import logo
import random
print(logo)


def ask_question(question_text, expected_answer):
    question_cleared = False

    while question_cleared == False:
        answer = input(f"{question_text} \n > ")
        if answer.lower() in expected_answer:
            question_cleared = True
            return answer
        else:
            print('Invalid input \n')

# Tests
# Create deck of cards


def build_deck():
    deck = []
    suites = ['hearts', 'spades', 'diamonds', 'clubs']
    cards = ['ace', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'jack', 'queen', 'king']
    deck_index = 1
    for s in suites:
        for c in cards:
            card_data = {}
            card_data['id'] = deck_index
            card_data['name'] = f"{s} - {c}"
            if c == 'ace':
                card_data['value'] = {'low': 1, 'high': 11}
            elif len(c) <= 2:
                card_data['value'] = int(c)
            else:
                card_data['value'] = 10
            deck.append(card_data)
            deck_index += 1
    return deck

# Randow draw


def random_draw(available_deck):
    draw = random.choice(available_deck)
    # print(
    #     f"The card with ID = {draw['id']} of type {type(draw['id'])} was selected.")
    # update available deck :
    updated_available_deck = [
        c for c in available_deck if c['id'] != draw['id']]
    return {'selected_card': draw, 'deck': updated_available_deck}


def draw_cards(n, deck, hand, player, verbose):
    for i in range(n):
        draw_results = random_draw(deck)
        selected_card = draw_results['selected_card']
        if verbose:
            print(f"{player} - card selected : {selected_card['name']} \n")

        if selected_card['name'][-3:] == 'ace':
            if sum(hand) <= 10:
                hand.append(selected_card['value']['high'])
            else:
                hand.append(selected_card['value']['low'])
        else:
            hand.append(selected_card['value'])

        deck = draw_results['deck']
    return {'hand': hand, 'deck': deck}


def init_game(verbose):
    current_deck = build_deck()
    computer_hand = []
    player_hand = []

    # Intial draw - 2 cards for player
    draw_results = draw_cards(2, current_deck, player_hand, 'Player', verbose)
    player_hand = draw_results['hand']
    current_deck = draw_results['deck']

    # Intial draw - 2 cards for computer
    draw_results = draw_cards(
        2, current_deck, computer_hand, 'Computer', verbose)
    computer_hand = draw_results['hand']
    current_deck = draw_results['deck']
    print(
        f'Player hand : \n {player_hand}  / Score = {sum(player_hand)}; \n Computer hand : \n {computer_hand}  / Score = {sum(computer_hand)}')

    return {'player_hand': player_hand, 'computer_hand': computer_hand, 'deck': current_deck}


def is_game_over(computer_hand, player_hand, is_first_round):
    if is_first_round:
        if sum(player_hand) == 21:
            return {'outcome': True, 'message': 'You win'}
        elif sum(computer_hand) == 21:
            return {'outcome': True, 'message': 'You lose'}
        else:
            return {'outcome': False, 'message': 'Game continues'}

    else:
        if sum(player_hand) > 21:
            return {'outcome': True, 'message': 'You lose (You bust)'}
        elif sum(player_hand) == 21:
            return {'outcome': True, 'message': 'You win'}
        elif sum(computer_hand) > 21:
            return {'outcome': True, 'message': 'You win (Computer busts)'}
        elif sum(computer_hand) == 21:
            return {'outcome': True, 'message': 'You lose'}
        else:
            return {'outcome': False, 'message': 'Game continues'}


def game():

    # Init stuff
    game_over = False
    game_rounds = 0
    initial_game = init_game(True)
    current_deck = initial_game['deck']
    computer_hand = initial_game['computer_hand']
    player_hand = initial_game['player_hand']
    game_over_results = is_game_over(computer_hand, player_hand, True)
    game_over = game_over_results['outcome']
    if game_over:
        print(game_over_results['message'])

    while game_over == False:
        # Player plays
        input_hit_stand = ask_question('Hit or stand ? (h/s)', ['h', 's'])
        if input_hit_stand == 'h':
            action_result = draw_cards(
                1, current_deck, player_hand, 'Player', True)
            player_hand = action_result['hand']
            current_deck = action_result['deck']
            game_over_results = is_game_over(computer_hand, player_hand, False)
            game_over = game_over_results['outcome']
            if game_over:
                print(game_over_results['message'])

        # Dealer plays
        if game_over == False:
            action_result = draw_cards(
                1, current_deck, computer_hand, 'Computer', True)
            computer_hand = action_result['hand']
            current_deck = action_result['deck']
            game_over_results = is_game_over(computer_hand, player_hand, False)
            game_over = game_over_results['outcome']
            if game_over:
                print(game_over_results['message'])

        print(
            f'Player hand : \n {player_hand}  / Score = {sum(player_hand)}; \n Computer hand : \n {computer_hand}  / Score = {sum(computer_hand)}')


game()
