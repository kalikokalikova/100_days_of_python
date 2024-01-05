import turtle
import pandas

# screen setup
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

# create states dictionary with state name as key and state coordinates as value in tuple
data = pandas.read_csv('50_states.csv')

states = {}
for state in data.iterrows():
    states[state[1][0].lower()] = (state[1][1], state[1][2])

# label state


def label_state(state_name, coordinates):
    label = turtle.Turtle()
    label.ht()
    label.up()
    label.goto(coordinates)
    label.write(state_name.capitalize(), align='center',
                font=('Arial', 8, 'normal'))


def show_winner_message():
    message = turtle.Turtle()
    message.ht()
    message.up()
    message.goto(0, 275)
    message.write("WOW you got all the states! You must have been home-schooled. Well done.",
                  align='center', font=('Arial', 20, 'normal'))


# game set up and run
counter = 0

while counter < 50:
    answer = screen.textinput(
        title=f"{counter}/50 states correct", prompt="Enter a state name")
    answer = answer.lower()
    if answer == "exit":
        break
    if answer in states:
        label_state(answer, states[answer])
        del states[answer]
        counter += 1
    else:
        print("nope")

if counter == 50:
    show_winner_message()
else:
    df = pandas.DataFrame(states.keys(), columns=['Missed States'])
    df.to_csv('missed_states', index=False)

screen.exitonclick()
