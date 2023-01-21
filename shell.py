import pygame
import time
import random


pygame.init() # returns a tuple of successful and unsuccessful initialisations

# SOUNDTRACK

# pygame.mixer.init()
# pygame.mixer.music.load('snake.mp3')
# pygame.mixer.music.play(-1)

#  VARIABLES

# to define colors you give the RGB values, can be given in a list or a tuple

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

 
display_width = 800
display_height = 600
clock = pygame.time.Clock()




# computer screens have a backlight, 

# surface, background or canvas

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')

# ICON

# icon = pygame.image.load('snakehead.png')
# best size for icons is 32 x 32 
# pygame.display.set_icon(icon)


# SPRITES
# img = pygame.image.load('snakehead.png')
# apple_img = pygame.image.load('apple.png')

#  pygame.display.flip() is interchangeable with display.update() when used with no parameters, updates the entire surface

smallfont = pygame.font.SysFont('comicsansms', 25)
mediumfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)




# FUNCTIONS


def pause():

    paused = True

    message_to_screen('Paused', white, -100, size="large")
    message_to_screen('Press C to resume, or Q to quit.', white, 25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        
        
        clock.tick(5)



def score(score):

    text = smallfont.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0, 0])


def game_intro():

    intro = True
    while intro:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks",
                            green,
                            -100,
                            'large')
        message_to_screen('The objective of the game is to shoot and destroy',
                            black,
                            -30)

        message_to_screen('The enemy tank before they destroy you.',
                            black,
                            10)


        message_to_screen('The more enemies you destroy the harder they get.',
                            black,
                            50)

        message_to_screen('Press C to play, P to pause or Q to quit.',
        black,
        180)

        pygame.display.update()
        clock.tick(15)



    

def text_objects(text, color, size):
    if size == 'small':
        text_surface = smallfont.render(text, True, color)

    elif size == 'medium':
        text_surface = mediumfont.render(text, True, color)

    elif size == 'large':
        text_surface = largefont.render(text, True, color)


    return text_surface, text_surface.get_rect()



    

def message_to_screen(msg, color, y_displace=0, size = 'small'): 
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    text_surface, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(text_surface, text_rect)

def game_loop():

    game_exit = False
    game_over = False
    FPS = 15

    #  GAME LOOP
    while not game_exit:

        if game_over == True:
            message_to_screen('Game Over', red, y_displace = -50, size='large')
            message_to_screen("Press C to play again or Q to quit.", white, 5, size='medium')
            pygame.display.update()

        while game_over == True:
            # gameDisplay.fill(white)
          

            # event loop

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    elif event.key == pygame.K_c:
                        game_loop()


        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass

                elif event.key == pygame.K_RIGHT:
                    pass

                elif event.key == pygame.K_UP:
                    pass

                elif event.key == pygame.K_DOWN:
                    pass

                elif event.key == pygame.K_p:
                    pause()


      
            

    # EVENT HANDLING AND THEN A GROUP OF LOGIC STATEMENTS, THEN GRAPHICS RENDERING AND THEN UPDATE THE DISPLAY
    #  THIS ALL HAPPENS EVERY FRAME PER SCOND, SO OPTIMISATION MAKES SENSE


    # LOGIC

        



        # draw everything and then render to save resources
        gameDisplay.fill(black)

        
        
        # draw everything and then render to save resources
        pygame.display.update()


        # COLLISION DETECTION
 

        # specify the frames per second that you want to have
        clock.tick(FPS)
    # use sprites or draw with pygame to put things on the screen (using coordinates)

    #  render font, blit the font, then update the sceen
    message_to_screen('GAME OVER', red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit() # unintialises pygame
    quit() # exits out of python

game_intro()
game_loop()


