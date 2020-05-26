import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Santanu")
wn.bgcolor("black")
wn.setup(width=600 , height= 600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("light green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  High Score: 0", align="center", font=("Ariel", 24, "normal"))


# functions
def go_up() :
    if head.direction != "down" :
        head.direction = "up"

def go_down() :
    if head.direction != "up":
        head.direction = "down"

def go_left() :
    if head.direction != "right":
        head.direction = "left"

def go_right() :
    if head.direction != "left":
        head.direction = "right"

def move() :
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down" :
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left" :
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right" :
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindibgs
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True :
    wn.update()

    # check for a collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        time.sleep(0.5)
        head.goto(0,0)
        head.direction = "stop"

        # hide the segments

        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segment list
        segments.clear()

        #Reset score
        score = 0

        delay = 0.1

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Ariel", 24, "normal"))



    #check for collision with the food

    if head.distance(food) < 20 :
        #move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay

        delay -= 0.01

        #increase the score

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Ariel", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1) :
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment zero to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #check for head collision with body segments
    for segment in segments :
        if segment.distance(head) < 20 :
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"

            # hide the segments

            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segment list
            segments.clear()

            # Reset score
            score = 0

            #reset the delay
            delay = 0.1

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Ariel", 24, "normal"))

    time.sleep(delay)




wn.mainloop()