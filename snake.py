#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
wall_color = "midnightblue"

snake_segments = []
snake_head_color = "green"
snake_direction = ""

fruit_color = ["blue", "yellow", "red", "orange", "blueviolet"]

score_num = 0

#-----initialize/configuration turtle-----
wn = trtl.Screen()
wn.setup (width=1000, height=1000, startx=0, starty=0)
wn.bgcolor("silver")

fruit = trtl.Turtle(shape="circle")
fruit.hideturtle()
fruit.penup()
fruit.speed(1)

walls = trtl.Turtle()
walls.hideturtle()
walls.penup()
walls.pencolor(wall_color)
walls.speed("fastest")
walls.pensize(15)

snake_head = trtl.Turtle(shape="square")
snake_head.penup()
snake_head.color(snake_head_color)
snake_head.speed("fastest")

title = trtl.Turtle()
title.hideturtle()
title.penup()
title.pencolor(wall_color)
title.goto(0, -400)
title.pendown()
title.write("SNAKE", align="center", font=("Arial", 45, "bold"))

score = trtl.Turtle()
wn.tracer(False)
score.penup()
score.hideturtle()
score.pencolor(wall_color)
score.goto(0, 375)
score.pendown()
score.write(("Score: "+ str(score_num)), align="center", font=("Arial", 45, "bold"))
wn.tracer(True)

#-----game functions--------
# Function fruit_loc() makes the fruit object go to a random location on the map
def fruit_loc():
  fruit_x = rand.randint(-285, 285)
  fruit_y = rand.randint(-185, 185)

  wn.tracer(False)
  fruit.color(rand.choice(fruit_color))
  fruit.goto(fruit_x, fruit_y)
  wn.tracer(True)
  fruit.showturtle()

# Function draw_walls() draws the 4 walls that encloses the snake and fruit
def draw_walls():
  walls.goto(300, 200)
  walls.pendown()

  for i in range(2):
    walls.right(90)
    walls.forward(400)
    walls.right(90)
    walls.forward(600)

# Function type_setup() is just to use less lines since all the type functions do the same thing, but different values
def type_setup(condition, condition2):
  global snake_direction
  if (snake_direction != condition):
    snake_direction = condition2

# These type functions change the value of the snake_direction variable, that is used to store the value of the direction of the snake
def type_up():
  type_setup("down", "up")

def type_down():
  type_setup("up", "down")

def type_left():
  type_setup("right", "left")

def type_right():
  type_setup("left", "right")

# Function snake_movement() is used to move the snake
def snake_movement():
  global snake_direction
  if (snake_direction == "up"):
    snake_head.sety(snake_head.ycor() + 4)
  elif (snake_direction == "down"):
    snake_head.sety(snake_head.ycor() - 4)
  elif (snake_direction == "left"):
    snake_head.setx(snake_head.xcor() - 4)
  elif (snake_direction == "right"):
    snake_head.setx(snake_head.xcor() + 4)

# Function score_reset() is used to update the score everytime the snake eats or dies
def score_reset():
  wn.tracer(False)
  score.clear()
  score.penup()
  score.hideturtle()
  score.pencolor(wall_color)
  score.goto(0, 375)
  score.pendown()
  score.write(("Score: "+ str(score_num)), align="center", font=("Arial", 45, "bold"))
  wn.tracer(True)

#-----events----------------
wn.listen()
draw_walls()
fruit_loc()

wn.onkeypress(type_up, "Up")
wn.onkeypress(type_down, "Down")
wn.onkeypress(type_left, "Left")
wn.onkeypress(type_right, "Right")

while True:
  wn.update()
  wn.tracer(False)

  # If statement used to restart the snake to the middle of the map, after hitting the wall
  if ((snake_head.xcor() >= 295) or (snake_head.xcor() <= -295) or (snake_head.ycor() >= 195) or (snake_head.ycor() <= -195)):
    for index in range(len(snake_segments)):
      snake_segments[index - 1].hideturtle()
    snake_segments.clear() 
    snake_head.goto(0, 0)
    snake_direction = ""
    score_num = 0
    score_reset()

  # If statement used to place the fruit at a random location after the snake head touches it and adds a segment to the snake
  if (abs(snake_head.xcor() - fruit.xcor()) <= 17) and (abs(snake_head.ycor() - fruit.ycor()) <= 17):
    score_num += 1
    score_reset()
    wn.tracer(False)
    temp_turtle = trtl.Turtle(shape="square")
    temp_turtle.speed("fastest")
    temp_turtle.color(snake_head_color)
    temp_turtle.penup()
    snake_segments.append(temp_turtle)
    wn.tracer(True)
    fruit_loc()
  wn.tracer(False)

  # This for loop and if statement causes the new the segment to go behind the head and follow it delayed
  for index in range((len(snake_segments)-1), -1, -1):
    snake_segments[index].goto(snake_segments[index - 1].xcor(), snake_segments[index - 1].ycor())
  if (len(snake_segments) > 0):
    snake_segments[0].goto(snake_head.xcor(), snake_head.ycor())
  
  wn.tracer(True)
  snake_movement()

  # This If statement and for loop is when the snake head touches its body, it resets
  for index in (snake_segments):
    if ((abs(snake_head.xcor() - index.xcor()) <= 0) and (abs(snake_head.ycor() - index.ycor()) <= 0)):
      for index in range(len(snake_segments)):
        snake_segments[index - 1].hideturtle()
      snake_head.goto(0, 0)
      snake_direction = ""
      snake_segments.clear()
      score_num = 0
      score_reset()

wn.mainloop()