
# Import the pgzrun module (needed for Pygame Zero)
import pgzrun

# Define the window size
WIDTH = 800
HEIGHT = 600

# Define the ball's properties
ball = Actor('ball')  # Make sure to have a 'ball.png' image in the images folder
ball.pos = 400, 300  # Start in the center of the screen
ball_speed_x = 3
ball_speed_y = 3

def draw():
    # Clear the screen and draw the ball
    screen.clear()
    screen.fill((0, 0, 0))  # Fill background with black color
    ball.draw()

def update():
    global ball_speed_x, ball_speed_y

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce off the walls
    if ball.left < 0 or ball.right > WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed_y = -ball_speed_y

# Run the game
pgzrun.go()
