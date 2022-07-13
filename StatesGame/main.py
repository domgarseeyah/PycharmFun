import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. State Naming Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
state_listing = states_data.state.to_list()
guessed_states = []

#click image to get x and y coordinates

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state name? ")
    answer_state = user_answer.title()
    if answer_state == "Exit":
        missing_states = [state for state in state_listing if state not in answer_state]
        # missing_states = []
        # for state in answer_state:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    #check answer against state list
    if answer_state in state_listing:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row_value = states_data[states_data.state == answer_state]
        t.goto(int(state_row_value.x), int(state_row_value.y))
        t.write(state_row_value.state.item())


turtle.mainloop()
# screen.exitonclick()
