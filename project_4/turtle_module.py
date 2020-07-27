import turtle
import random
import pickle


def get_results():
    """
    This function opens the users file, reads it and returns its content
    :return: A dictionary with details about the users
    """
    infile = open("results", 'rb')
    results = pickle.load(infile)
    infile.close()
    return results


def finish_line():
    fl = turtle.Turtle()
    fl.shape("circle")
    fl.pensize(5)
    fl.penup()
    fl.goto(250, 300)
    fl.pendown()
    fl.goto(250, -300)


def t_attributes(t, y, c):
    """
    :param t: Turtle object
    :param y: y value of the turtle's starting point (-300, y)
    :param c: turtle's pen color
    :return: None
    """
    t.shape("turtle")
    t.shapesize(3, 3, 3)
    t.color(c, c)
    t.penup()
    t.goto(-300, y)
    t.pendown()
    t.pensize(5)
    t.pencolor(c)


def game_loop():
    red_tot = green_tot = blue_tot = yellow_tot = black_tot = 0

    # The turtles will travel from the starting point (-300, y) to the point (250, y), thus the distance is 550
    while all([red_tot < 550, green_tot < 550, blue_tot < 550, yellow_tot < 550, black_tot < 550]):
        red_rand = random.randint(1, 100)
        red_turtle.fd(red_rand)
        red_tot += red_rand

        green_rand = random.randint(1, 100)
        green_turtle.fd(green_rand)
        green_tot += green_rand

        blue_rand = random.randint(1, 100)
        blue_turtle.fd(blue_rand)
        blue_tot += blue_rand

        yellow_rand = random.randint(1, 100)
        yellow_turtle.fd(yellow_rand)
        yellow_tot += yellow_rand

        black_rand = random.randint(1, 100)
        black_turtle.fd(black_rand)
        black_tot += black_rand

    max_tot = max([red_tot, green_tot, blue_tot, yellow_tot, black_tot])
    if max_tot == red_tot:
        results_dict["Winners"].append("Red turtle")
        print("\033[31mThe red turtle won!")
    elif max_tot == green_tot:
        results_dict["Winners"].append("Green turtle")
        print("\033[32mThe green turtle won!")
    elif max_tot == blue_tot:
        results_dict["Winners"].append("Blue turtle")
        print("\033[34mThe blue turtle won!")
    elif max_tot == yellow_tot:
        results_dict["Winners"].append("Yellow turtle")
        print("\033[33mThe yellow turtle won!")
    else:
        results_dict["Winners"].append("Black turtle")
        print("\033[30mThe black turtle won!")

    outfile = open("results", 'wb')       # Opens the results file in the writing mode
    pickle.dump(results_dict, outfile)    # Updates the results file with the new result
    outfile.close()


try:
    results_dict = get_results()
except:
    # If the users file does not exist, the program will create it and insert an empty dictionary on it
    empty_dict = {"Winners": list()}
    outfile = open("results", 'wb')
    pickle.dump(empty_dict, outfile)
    outfile.close()
    results_dict = get_results()

screen = turtle.Screen()

screen.title("Turtle Race Game")

finish_line()

red_turtle = turtle.Turtle()
t_attributes(red_turtle, 250, "red")

green_turtle = turtle.Turtle()
t_attributes(green_turtle, 125, "green")

blue_turtle = turtle.Turtle()
t_attributes(blue_turtle, 0, "blue")

yellow_turtle = turtle.Turtle()
t_attributes(yellow_turtle, -125, "yellow")

black_turtle = turtle.Turtle()
t_attributes(black_turtle, -250, "black")

screen.onkey(game_loop, "space")
screen.listen()

turtle.done()
