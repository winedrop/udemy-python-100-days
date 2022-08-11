import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "25_day_states/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("25_day_states/50_states.csv")
answer_list = []
while 1:
    answer_state = screen.textinput(title=f"{len(answer_list)}/50 States", prompt="Enter a state")
    if answer_state not in data.state and answer_state in answer_list:
        continue
    
    state = data[data.state == answer_state.title()]
    turt = turtle.Turtle()
    turt.hideturtle()
    turt.penup()
    turt.setposition(int(state.x),int(state.y))
    turt.write(state.state.values[0])
    answer_list.append(answer_state.title())







turtle.mainloop()

screen.exitonclick()