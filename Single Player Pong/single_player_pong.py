from tkinter import Canvas
import time

# Canvas's size
CANVAS_WIDTH = 350
CANVAS_HEIGHT = 350

BALL_SIZE = 20

PADDLE_WIDTH = 60
PADDLE_HEIGHT = 20

INITIAL_PADDLE_SPEED = 1

# Delay of the objects' movement
DELAY = 0.001

def main():
    # Sets the canvas edges
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Canvas's dimensions
    middle_x = CANVAS_WIDTH/2
    middle_y = CANVAS_HEIGHT/2

    # Paddle's start coordinates
    paddle_start_x = middle_x - PADDLE_WIDTH / 2
    paddle_start_y = CANVAS_HEIGHT - PADDLE_HEIGHT

    # Start speed
    x_speed = INITIAL_PADDLE_SPEED
    y_speed = 0

    # Ball
    ball = canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, 'blue')
    change_ball_x = 1 #increment in ball's x coordinate
    change_ball_y = 1 #increment in ball's y coordinate
    
    # Paddle
    paddle = canvas.create_rectangle(
        paddle_start_x,
        paddle_start_y,
        paddle_start_x + PADDLE_WIDTH,
        CANVAS_HEIGHT,
        "white", "navy")

    #Defines the paddle's movement
    while True:
        current_location = canvas.move(paddle, x_speed, y_speed)

        # Makes the paddle move with key press command 
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            x_speed = -INITIAL_PADDLE_SPEED
            y_speed = 0
        if key == 'ArrowRight':
            x_speed = INITIAL_PADDLE_SPEED
            y_speed = 0
        if key == 'ArrowUp':
            y_speed = 0
            x_speed = 0
        if key == 'ArrowDown':
            y_speed = 0
            x_speed = 0
            
        time.sleep(DELAY)
        
        # Tracks the directions of the paddle
        paddle_x = canvas.get_left_x(paddle)
        paddle_y = canvas.get_top_y(paddle)

        # It should reverse direction on x=0, but it's skipping
        # x=1 direct to x=-1.
        if paddle_start_x < 0:
            paddle_start_x += INITIAL_PADDLE_SPEED
        elif paddle_start_x >= CANVAS_WIDTH:
            paddle_start_x -= INITIAL_PADDLE_SPEED

        print("x:", paddle_x) 
        
        # Defines the ball's movement
        
        # Ball's current coordinates
        ball_left_x = canvas.get_left_x(ball)
        ball_top_y = canvas.get_top_y(ball)
        # Changes the direction in the coordinates

        # Detects if the ball hits the side walls
        if ball_left_x < 0 or ball_left_x + BALL_SIZE >= CANVAS_WIDTH:
            change_ball_x = -change_ball_x
        
        # Detects if the ball hits the up and bottom walls.
        # It's stuck in the corner.
        if ball_top_y < 0 or ball_top_y + BALL_SIZE >= CANVAS_HEIGHT:
            change_ball_y = -change_ball_y
        # If it reaches the bottom wall, the game is over.

        canvas.move(ball, change_ball_x, change_ball_y)
        time.sleep(DELAY)
       

#canvas.wait_for_click() - útil para quando for iniciar o jogo
if __name__ == '__main__':
    main()

# Milestones:
# 1 Set up the game canvas - OK
# 2 Create the ball and paddle - OK
# 3 Implement paddle movement - Consegui fazer o movimento do teclado, mas não o limite das bordas laterais.
# 4 Animate the ball - OK - but, the game still not ends when the ball hits the bottom, and the ball doesn't hit the paddle
# 5 Handle ball-paddle collision
# 6 Implement game over
# 7 Add rounds and display rounds left
# 8 Prompt to start the game
# 9 Test and debug
# Bonus (if there's time): add background color