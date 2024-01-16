import turtle
import random

# Set up screen dimensions and game parameters
screen_width = 500
screen_height = 500
food_size = 10
delay = 100

# Define movement offsets for the snake in different directions
movement_offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset_game():
    global snake, snake_direction, food_pos, pen

    # Initialize snake starting position and direction
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_direction = "up"
    
    # Set initial food position and update its location on screen
    food_pos = get_random_food_position()
    food.goto(food_pos)

    # Move the snake
    move_snake()

def move_snake():
    global snake_direction

    # Calculate new head position based on current direction
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + movement_offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + movement_offsets[snake_direction][1]

    # Check for collision with itself
    if new_head in snake[:-1]:
        reset_game()
    else:
        snake.append(new_head)

        # Check for collision with food
        if not food_collision():
            snake.pop(0)

        # Handle screen boundaries
        handle_screen_boundaries()

        # Update snake segments on the screen
        update_snake_segments()

        # Update screen
        screen.update()

        # Schedule the next move
        turtle.ontimer(move_snake, delay)

def food_collision():
    global food_pos

    # Check if the snake head collides with the food
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_position()
        food.goto(food_pos)
        return True
    return False

def get_random_food_position():
    # Generate a random position for the food within the screen boundaries
    x = random.randint(-screen_width / 2 + food_size, screen_width / 2 - food_size)
    y = random.randint(-screen_height / 2 + food_size, screen_height / 2 - food_size)
    return (x, y)

def get_distance(pos1, pos2):
    # Calculate Euclidean distance between two positions
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def handle_screen_boundaries():
    # Handle screen boundaries for the snake's head
    if snake[-1][0] > screen_width / 2:
        snake[-1][0] -= screen_width
    elif snake[-1][0] < -screen_width / 2:
        snake[-1][0] += screen_width
    elif snake[-1][1] > screen_height / 2:
        snake[-1][1] -= screen_height
    elif snake[-1][1] < -screen_height / 2:
        snake[-1][1] += screen_height

def update_snake_segments():
    # Update snake segments on the screen using turtle stamps
    pen.clearstamps()
    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

# Input handling functions for snake direction
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Set up the game window
screen = turtle.Screen()
screen.setup(screen_width, screen_height)
screen.title("Snake Game")
screen.bgcolor("white")
screen.setup(500, 500)
screen.tracer(0)

# Set up turtle for drawing snake segments
pen = turtle.Turtle("square")
pen.penup()

# Set up turtle for drawing food
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.shapesize(food_size / 20)
food.penup()

# Set up event listeners for arrow key input
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

# Initialize and start the game
reset_game()
turtle.done()
