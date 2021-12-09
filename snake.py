# importing libraries
import pygame
import time
import random
import os


snake_speed = 5

# Window size
WINDOWX = 720
WINDOWY = 480

# defining colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game - Group 2')
game_window = pygame.display.set_mode((WINDOWX, WINDOWY))

# FPS (frames per second) controller
fps = pygame.time.Clock()


# get high score function


def get_high_score():

    # checking if file exists
    if not os.path.exists('high_score.txt'):

        # if not create the file
        with open('high_score.txt', 'w') as f:
            f.write('0')

            # return 0
            return 0

    else:
        # if file exists
        with open('high_score.txt', 'r') as f:
            high_score = f.read()

            # return high score
            return high_score



# saving high score function
def save_high_score(new_high_score):

    # open file in write mode
    with open('high_score.txt', 'w') as f:
        f.write(str(new_high_score))


# displaying Score function


def show_score(choice, color, font, size, score):
    high_score = get_high_score()

    if score > int(high_score):
        high_score = score

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    high_s_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    high_s_surface = high_s_font.render('High Score : ' + str(high_score), True, color)
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # show high score below score
    high_s_rect = high_s_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)
    game_window.blit(high_s_surface, [WINDOWX - high_s_rect.width - 10, 10])

# game over function


def game_over_func(high_score, score):
    # stop background music
    pygame.mixer.music.stop()
    # creating font object my_font
    my_font = pygame.font.SysFont('consolas', 50)
    instruction_font = pygame.font.SysFont('consolas', 30)
    score_font = pygame.font.SysFont('consolas', 30)

    # game over text
    game_over_surface = my_font.render('Game Over', True, RED)

    # score text and high score text
    new_high_score_surface = score_font.render('High Score : ' + str(high_score), True, RED)
    new_score_surface = score_font.render('Your Score : ' + str(score), True, RED)

    # instructing user to press R to restart or Q to quit
    press_r_surface = instruction_font.render('Press R to Restart or Q to Quit', True, RED)

    #  display text
    game_window.blit(game_over_surface, (WINDOWX//2 - game_over_surface.get_width()//2, WINDOWY//2 - game_over_surface.get_height()//2))
    game_window.blit(new_high_score_surface, (WINDOWX//2 - new_high_score_surface.get_width()//2, WINDOWY//2 - new_high_score_surface.get_height()//2 + 50))
    game_window.blit(new_score_surface, (WINDOWX//2 - new_score_surface.get_width()//2, WINDOWY//2 - new_score_surface.get_height()//2 + 100))
    game_window.blit(press_r_surface, (WINDOWX//2 - press_r_surface.get_width()//2, WINDOWY//2 - press_r_surface.get_height()//2 + 150))
    
    # updating display
    pygame.display.flip()

    # after 10 seconds listen for key press
    # check if user pressed R or Q
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    # restart the game
                    main()

# pause function
def pause():
    # stop background music
    pygame.mixer.music.stop()
    # creating font object my_font
    my_font = pygame.font.SysFont('consolas', 50)
    instruction_font = pygame.font.SysFont('consolas', 30)

    # pause text
    pause_surface = my_font.render('Paused', True, RED)

    # instructing user to press P to unpause, Q to quit
    press_p_surface = instruction_font.render('Press P to Unpause or Q to Quit', True, RED)

    #  display text
    game_window.blit(pause_surface, (WINDOWX//2 - pause_surface.get_width()//2, WINDOWY//2 - pause_surface.get_height()//2))
    game_window.blit(press_p_surface, (WINDOWX//2 - press_p_surface.get_width()//2, WINDOWY//2 - press_p_surface.get_height()//2 + 50))

    # updating display
    pygame.display.flip()

    # listen for key press
    # check if user pressed P or Q
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_p:
                    # unpause the game
                    # pygame.mixer.music.play(-1)
                    return
            # if user clicks on the window, quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def welcome():
    # creating font object my_font
    my_font = pygame.font.SysFont('consolas', 50)
    instruction_font = pygame.font.SysFont('consolas', 30)

    # welcome text
    welcome_surface = my_font.render('Welcome to Snake Game', True, RED)

    # instructing user to press P to start the game
    press_p_surface = instruction_font.render('Press P to Start the Game', True, RED)
    press_q_surface = instruction_font.render('Press Q to Quit', True, RED)
    #  display text
    game_window.blit(welcome_surface, (WINDOWX//2 - welcome_surface.get_width()//2, WINDOWY//2 - welcome_surface.get_height()//2))
    game_window.blit(press_p_surface, (WINDOWX//2 - press_p_surface.get_width()//2, WINDOWY//2 - press_p_surface.get_height()//2 + 50))
    game_window.blit(press_q_surface, (WINDOWX//2 - press_q_surface.get_width()//2, WINDOWY//2 - press_q_surface.get_height()//2 + 100))

    # updating display
    pygame.display.flip()

    # listen for key press
    # check if user pressed P
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            # exit the game if user clicks on the window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
# main game loop
def main():

    # pygame.init()
    # # play background music
    # pygame.mixer.music.load('sounds/background.mp3')
    # pygame.mixer.music.play(-1)
    # # set volume to 50%
    # pygame.mixer.music.set_volume(0.3)

    # set game over to false
    game_over = False

    # set game exit to false
    game_exit = False

    # set initial score to 0
    score = 0
    high_score = get_high_score()

    # set initial speed to 5
    snake_speed = 5

    # set initial fruit spawn to true
    fruit_spawn = True

    # set initial fruit position to random
    fruit_position = [random.randrange(1, (WINDOWX//10)) * 10,
                      random.randrange(1, (WINDOWY//10)) * 10]

    # set initial snake direction to right
    direction = 'RIGHT'

    # set initial change to direction to right
    change_to = direction

    # set initial snake position to 100, 50
    snake_position = [100, 50]

    # set initial snake body
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]]

    # game loop
    while not game_exit:
        
        # check if game is over
        if game_over:
            # if game is over, call game over function
            game_over_func(high_score, score)

        # check if game is not over
        else:
            # check if user pressed R or Q
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
                        direction = 'RIGHT'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                        direction = 'LEFT'
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                        direction = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                        direction = 'DOWN'
                    # if user pressed p pause the game and resume when p is pressed again
                    if event.key == pygame.K_p:
                        pause()
                    if event.key == pygame.K_q:
                        game_exit = True
                        pygame.quit()
                        quit()

            # check if direction is not equal to change to
            if direction != change_to:
                # change direction
                direction = change_to

            # check if direction is right
            if direction == 'RIGHT':
                # move right
                snake_position[0] += 10
            if direction == 'LEFT':
                # move left
                snake_position[0] -= 10
            if direction == 'UP':
                # move up
                snake_position[1] -= 10
            if direction == 'DOWN':
                # move down
                snake_position[1] += 10

            # check if snake head touches border
            if snake_position[0] > WINDOWX - 10 or snake_position[0] < 0 or snake_position[1] > WINDOWY - 10 or snake_position[1] < 0:
                # game over
                game_over = True
                game_over_func(high_score, score)

            # check if snake head touches body
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    # game over
                    game_over = True
                    game_over_func(high_score, score)

            # check if snake head touches fruit
            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                # increase score
                score += 10
                # if score is greater than high score, set high score to score
                if score > int(high_score):
                    high_score = score
                    save_high_score(high_score)
                    # play high score sound for 1 second
                    # pygame.mixer.Sound('sounds/high_score.mp3').play()
                    # time.sleep(1)
                    # pygame.mixer.Sound('sounds/high_score.mp3').stop()
                # increase speed
                snake_speed += 5
                # spawn new fruit
                fruit_spawn = False
                # increase length of snake
                snake_body.append([0, 0])

            # check if fruit spawn is false
            if not fruit_spawn:
                # spawn fruit
                fruit_position = [random.randrange(1, (WINDOWX//10)) * 10,
                                  random.randrange(1, (WINDOWY//10)) * 10]
                # set fruit spawn to true
                fruit_spawn = True

            # move snake body
            for index in range(len(snake_body) - 1, 0, -1):
                # move body
                snake_body[index] = [snake_body[index - 1][0], snake_body[index - 1][1]]

            # move snake head
            snake_body[0] = [snake_position[0], snake_position[1]]

            # draw background
            game_window.fill(BLACK)

            # draw score
            show_score(1, WHITE, "times new roman", 20, score)

            # draw snake
            for block in snake_body:
                pygame.draw.rect(game_window, WHITE, [block[0], block[1], 10, 10])

            # draw fruit
            pygame.draw.rect(game_window, RED, [fruit_position[0], fruit_position[1], 10, 10])

            # update display
            pygame.display.update()

            # set game loop to 60 frames per second
            fps.tick(snake_speed)


# call main function
if __name__ == '__main__':
    welcome()


# end of game