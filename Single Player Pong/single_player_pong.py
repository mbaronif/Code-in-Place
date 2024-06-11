from tkinter import Canvas

# Canvas's size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

# Ball dimension
BALL_SIZE = 20

# Paddle dimensions
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 20

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Canvas's dimensions
    middle_x = CANVAS_WIDTH/2
    middle_y = CANVAS_HEIGHT/2

    # Ball
    ball = canvas.create_rectangle(0, 0,
        BALL_SIZE, BALL_SIZE, "blue")
    
    # Paddle
    paddle = canvas.create_rectangle(
        (middle_x-(PADDLE_WIDTH/2)),
        (CANVAS_HEIGHT-PADDLE_HEIGHT),
        (middle_x-(PADDLE_WIDTH/2))+PADDLE_WIDTH,
        CANVAS_HEIGHT,
        "white", "navy")


if __name__ == '__main__':
    main()

# Milestones:
# 1 Set up the game canvas - OK
# 2 Create the ball and paddle - OK
# 3 Implement paddle movement
# 4 Animate the ball
# 5 Handle ball-paddle collision
# 6 Implement game over
# 7 Add rounds and display rounds left
# 8 Prompt to start the game
# 9 Test and debug
# Bonus (if there's time): add background color