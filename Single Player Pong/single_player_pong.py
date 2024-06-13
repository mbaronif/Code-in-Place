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
    paddle_left_x = middle_x - PADDLE_WIDTH / 2
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
        paddle_left_x,
        paddle_start_y,
        paddle_left_x + PADDLE_WIDTH,
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
        
        # Ball's current coordinates
        ball_left_x = canvas.get_left_x(ball)
        ball_top_y = canvas.get_top_y(ball)
        ball_bottom_y = ball_top_y + BALL_SIZE

        # Paddle's current location
        paddle_left_x = canvas.get_left_x(paddle)
        paddle_top_y = canvas.get_top_y(paddle)
        paddle_right_x = paddle_left_x + PADDLE_WIDTH

        # It should reverse direction on x=0, but it's skipping
        # x=1 direct to x=-1.
        if paddle_left_x < 0:
            paddle_left_x += INITIAL_PADDLE_SPEED
        elif paddle_left_x >= CANVAS_WIDTH:
            paddle_left_x -= INITIAL_PADDLE_SPEED

        print("x:", paddle_left_x) 
        
        # Checks if the ball hits the side walls
        if ball_left_x < 0 or ball_bottom_y >= CANVAS_WIDTH:
            change_ball_x = -change_ball_x
        
        # Checks if the ball hits the up and bottom walls.
        if ball_top_y < 0 or ball_bottom_y >= CANVAS_HEIGHT:
            change_ball_y = -change_ball_y

        # Checks if the ball hits the paddle and bounces.   
        # But now, after that, it doesn't bounces in the side walls.
        if (paddle_top_y <= ball_bottom_y) and (paddle_left_x <= ball_left_x):
            change_ball_y = -change_ball_y   
        
        
        
        # If the ball reaches the bottom wall, the game is over.

        canvas.move(ball, change_ball_x, change_ball_y)
        time.sleep(DELAY)
       

#canvas.wait_for_click() - útil para quando for iniciar o jogo
if __name__ == '__main__':
    main()

# Milestones:
# 1 Set up the game canvas - OK
# 2 Create the ball and paddle - OK
# 3 Implement paddle movement - Keybord paddle moving working, but the paddle is going off the canvas, not stopping in the side walls.
# 4 Animate the ball - OK
# 5 Handle ball-paddle collision - OK - but after hitting the paddle, the ball doesn't bounce off the side walls anymore. Soving this may solve the paddle border issue too.
# 6 Implement game over
# 7 Add rounds and display rounds left
# 8 Prompt to start the game
# 9 Test and debug
# Bonus (if there's time): add background color