import pygame # contains modules for writing games
import random # generates random numbers in given range

# initialised pygame also setted up display for the game 
pygame.init()
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# setting up game clock  
clock = pygame.time.Clock()

# Set up the snake and food
snake_x = screen_width // 4
snake_y = screen_height // 2
snake = [
    [snake_x, snake_y],
    [snake_x - 20, snake_y],
    [snake_x - 40, snake_y]
] # 2D arrays are being used here to picture initial image of snake

food = [random.randrange(1, screen_width // 20) * 20,
        random.randrange(1, screen_height // 20) * 20] # using array with two elements which represents x 
# and y coordinate of the food

# Setting up the initial direction
direction = 'RIGHT'

# Setting up the game fonts
font_style = pygame.font.SysFont(None, 30)

#setting bg music
pygame.mixer.music.load('SnakeTone.mp3')
pygame.mixer.music.play(-1) # -1 loops the tone indefinetly

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))


def draw_food(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 20, 20))


def show_score(score):
    score_text = font_style.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, [0, 0])


# Starting the game loop
game_over = False
score = 0
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_SPACE:
                pygame.quit()

    # Moving the snake
    if direction == 'RIGHT':
        snake_x += 20
    elif direction == 'LEFT':
        snake_x -= 20
    elif direction == 'UP':
        snake_y -= 20
    elif direction == 'DOWN':
        snake_y += 20
    snake_head = [snake_x, snake_y]
    snake.insert(0, snake_head)

    # Checking for game over
    if snake_x < 0 or snake_x >= screen_width or snake_y < 0 or snake_y >= screen_height:
        game_over = True
    for block in snake[1:]:
        if block == snake[0]: # iteration starting from index 1 uptill end of snake, checks if have 
            #collided with snakes head that is index 0
            game_over = True

    # Checking if the snake has eaten the food
    if snake_x == food[0] and snake_y == food[1]:
        food = [random.randrange(1, screen_width // 20) * 20,
                random.randrange(1, screen_height // 20) * 20]
        score += 1
    else:
        snake.pop() # the starting position of snake is increasing every instant and
        # the end is not being reduced only when the snake eats the food

    # Drawing the screen
    screen.fill((0, 0, 0))
    draw_snake(snake)
    draw_food(food[0], food[1])
    show_score(score)
    pygame.display.update()

    # Setting the game clock
    clock.tick(15)

# showing game over 
game_over_font = pygame.font.SysFont(None, 50)
game_over_text = game_over_font.render("GAME OVER :|", True, (255, 255, 255))
screen.blit(game_over_text, (screen_width // 3, screen_height // 2))
pygame.display.update()
pygame.time.wait(1500) # Wait for 1.5 seconds before quitting the game
pygame.quit()

# Quit the game
