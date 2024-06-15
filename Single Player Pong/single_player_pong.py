from graphics import Canvas
import time

# Canvas's size
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

BALL_SIZE = 20

PADDLE_WIDTH = 60
PADDLE_HEIGHT = 20

INITIAL_PADDLE_SPEED = 1

MAX_ROUND = 3

# Delay of the objects' movement
DELAY = 0.001

def main():
    # Sets the canvas edges
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Canvas's center
    center_x = CANVAS_WIDTH/2
    center_y = CANVAS_HEIGHT/2

    # Paddle's start coordinates
    paddle_left_x = center_x - PADDLE_WIDTH / 2
    paddle_start_y = CANVAS_HEIGHT - PADDLE_HEIGHT

    # Paddle's start speed
    paddle_x_speed = INITIAL_PADDLE_SPEED
    paddle_y_speed = 0

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
    
    game_round = 0 # The initial count of game rounds.

    while True:
        # Defines the paddle's keyboard movement
        current_location = canvas.move(paddle, paddle_x_speed, paddle_y_speed)

        # Makes the paddle move with key press command 
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft' and paddle_left_x > 0:
            paddle_x_speed = -INITIAL_PADDLE_SPEED
            paddle_y_speed = 0
        if key == 'ArrowRight' and paddle_right_x < CANVAS_WIDTH:
            paddle_x_speed = INITIAL_PADDLE_SPEED
            paddle_y_speed = 0
        if key == 'ArrowUp':
            paddle_y_speed = 0
            paddle_x_speed = 0
        if key == 'ArrowDown':
            paddle_y_speed = 0
            paddle_x_speed = 0

        # Delay rate to make it possible to see the paddle in movement.    
        time.sleep(DELAY)
        
        # Ball's current coordinates
        ball_left_x = canvas.get_left_x(ball)
        ball_top_y = canvas.get_top_y(ball)
        ball_bottom_y = ball_top_y + BALL_SIZE

        # Paddle's current location
        paddle_left_x = canvas.get_left_x(paddle)
        paddle_top_y = canvas.get_top_y(paddle)
        paddle_right_x = paddle_left_x + PADDLE_WIDTH

        # Stops the paddle when it hits the side walls.
        if paddle_left_x <= 0 and paddle_x_speed <0:
            paddle_x_speed = 0
        elif paddle_right_x >= CANVAS_WIDTH and paddle_x_speed > 0:
            paddle_x_speed = 0

        # Checks if the ball hits the side walls
        if ball_left_x < 0 or ball_left_x + BALL_SIZE >= CANVAS_WIDTH:
            change_ball_x = -change_ball_x
        
        # Checks if the ball hits the top wall.
        if ball_top_y < 0:
            change_ball_y = -change_ball_y
        
        #Checks if the ball hits the bottom line, then ends the game.
        if ball_bottom_y > CANVAS_HEIGHT:
            game_round +=1 # Adds 1 to game_round.
            round_left = MAX_ROUND - game_round
            print("Rounds left:", str(round_left)) # Print the number of the round   
            canvas.moveto(ball, 0, 0)
        
        if round_left == 0:
            print("Game over")
        

        #canvas.create_text(55, 180, font_size = 50, text="GAME OVER", color="red")
        #break # to exit the while loop and end the game    
        
        
        # Checks if the ball hits the paddle and bounces.   
        if (paddle_top_y <= ball_bottom_y) and (paddle_left_x <= ball_left_x <= paddle_right_x):
            change_ball_y = -change_ball_y   
        

        canvas.move(ball, change_ball_x, change_ball_y)
        time.sleep(DELAY)
       

#canvas.wait_for_click() - útil para quando for iniciar o jogo
if __name__ == '__main__':
    main()

# Milestones:
# 1 Set up the game canvas - DONE
# 2 Create the ball and paddle - DONE
# 3 Implement paddle movement - DONE
# 4 Animate the ball - DONE
# 5 Handle ball-paddle collision - DONE
# 6 Implement game over
    #6.1 Condition to end the game when the ball hits the bottom of the screen - DONE
    #6.2.1 Display a 'Game Over' message centered on the canvas. - DONE
        #6.2.1.1 Display a 'Game Over' message only after the 3rd chance.
# 7 Add rounds and display rounds left
    #7.1 Track the number of rounds left - 3 chances. - DONE
    #7.2 Display the count on the bottom-left corner of the screen.
# 8 Prompt to start the game
    #8.1 Prompt 'Round 1" at the beginning of the game.
    #8.2 Display 'Round 2' and 'Round 3' in the beginning of the 2 and 3 chances.
# 9 Test and debug
# Bonus (if there's time): add background color