import turtle
import random

t_screen = turtle.Screen()
t_screen.bgcolor("light blue")
t_screen.title("Catching the Turtle")
turtle_list = []
score = 0
game_over = False
# time turtle
t_t = turtle.Turtle()


# title
def turtle_title():
    turtle_title = turtle.Turtle()
    turtle_title.hideturtle()
    turtle_title.penup()
    turtle_title.color("black")
    turtle_title.setpos(0, 300)
    turtle_title.write("Erva'nın Oyunu", align="center", font=("Verdana",
                                                               15, "normal"))


# score
turtle_score = turtle.Turtle()


def turt_score():
    turtle_score.penup()
    turtle_score.color("black")
    turtle_score.hideturtle()
    turtle_score.setpos(0, 250)
    turtle_score.write("Score: 0", align="center", font=("Verdana", 15, "normal"))


def make_turtle(x, y):
    t_turtle = turtle.Turtle()
    hide_turtle()
    def click_turtle(x, y):
        global score
        score += 1
        turtle_score.clear()
        turtle_score.write(f"Score: {score} ", align="center", font=("Verdana", 15, "normal"))

    t_turtle.onclick(click_turtle)
    t_turtle.penup()
    t_turtle.shape("turtle")
    t_turtle.shapesize(2)
    t_turtle.goto(x, y)
    turtle_list.append(t_turtle)


x_c = [-300, -200, -100, 0, 100, 200, 300]
y_c = [-300, -200, -100, 0, 100, 200]


def setup_turtle():
    for x in x_c:
        for y in y_c:
            make_turtle(x, y)


def hide_turtle():
    for t_turtle in turtle_list:
        t_turtle.hideturtle()


def turtle_random():
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        t_screen.ontimer(turtle_random, 500)


def timer(time):
    global game_over
    t_t.penup()
    t_t.color("black")
    t_t.hideturtle()
    t_t.setpos(0, 230)
    if time > 0:
        t_t.clear()
        t_t.write("Time: {}".format(time), align="center", font=("Verdana", 15, "normal"))
        t_screen.ontimer(lambda: timer(time - 1), 1000)
    else:
        game_over = True
        hide_turtle()
        t_t.clear()
        t_t.write("Game Over!", align="center", font=("Verdana", 15, "normal"))


turtle.tracer(0)
turtle_title()
turt_score()
setup_turtle()
hide_turtle()
turtle_random()
timer(10)
turtle.tracer(1)

turtle.mainloop()
