import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Read state data

state_data = pd.read_csv('50_states.csv')
state_data['lowercase_state_name'] = state_data.state.str.lower()
print(state_data)


def display_state_name(state_name, state_position):
    # Create a turtle
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.color('black')
    state_turtle.goto(state_position)
    state_turtle.write(state_name)


game_over = False
score = 0
guessed_states = []
while game_over is False:

    answer_state = screen.textinput(
        title=f'Guess the state {score}/50 correct', prompt="What's another state name?").lower()

    if answer_state == 'exit':
        all_states = state_data.lowercase_state_name.to_list()
        states_to_learn = [
            state for state in all_states if state not in guessed_states]
        print(states_to_learn)
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv('states_to_learn.csv')

    else:
        filtered_df = state_data[state_data.lowercase_state_name ==
                                 answer_state]

        if len(filtered_df.index) > 0:
            state_name = answer_state.capitalize()
            print(filtered_df)
            state_position = (filtered_df['x'].iloc[0],
                              filtered_df['y'].iloc[0])
            display_state_name(state_name, state_position)
            score += 1
            guessed_states.append(answer_state)


screen.exitonclick()
