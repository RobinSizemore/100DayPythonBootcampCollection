import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Name Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)
screen.setup(width=750, height=750, startx=2750, starty=1500)
turtle.shape(image_path)
draw_turtle = turtle.Turtle()
draw_turtle.hideturtle()
draw_turtle.penup()

states_data_frame = pandas.read_csv("50_states.csv")
states_dict = states_data_frame.to_dict()

guessed = []
while len(guessed) < 50:
    answer_state = screen.textinput(title="Guess A State", prompt="Enter the name of another state.")
    result = states_data_frame[states_data_frame.state == answer_state.title()]
    print(result)
    if answer_state.title() in guessed:
        print("You already guessed that.")
    elif len(result) < 1:
        print("Not a state.")
    else:
        guessed.append(answer_state.title())
        draw_turtle.goto(int(result.x.iloc[0]), int(result.y.iloc[0]))
        draw_turtle.write(answer_state.title(), False, "left", ("Arial", 7, "normal"))

print("You got them all!")


turtle.mainloop()
