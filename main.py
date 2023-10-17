import pandas
import turtle
from draw import Marker

marble = Marker()
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("usstates.csv")
all_states = data["state"].tolist()
allx = data["x"].tolist()
ally = data["y"].tolist()

guessed = []

game = True

while game:
    answer_state = screen.textinput(title=f"{len(guessed)}/ 50 Guess the state", prompt="Name an U.S State").title()
    if answer_state == "Exit":
        missing_states = [name for name in all_states if name not in guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing States.csv")
        break

    for state in all_states:
        if state == answer_state:
            guessed.append(answer_state)
            index = all_states.index(state)
            marble.paint(allx[index], ally[index], state)
