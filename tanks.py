import pygame
import time
import random


pygame.init() # returns a tuple of successful and unsuccessful initialisations

# --------------------------------------------------------------------------

# SOUNDTRACK

# pygame.mixer.init()
# pygame.mixer.music.load('snake.mp3')
# pygame.mixer.music.play(-1)

fire_sound = pygame.mixer.Sound('fire.mp3')
boom_sound = pygame.mixer.Sound('boom.mp3')


pygame.mixer.music.load('TANKS OST.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


# -------------------------------------------------------------------------

#  VARIABLES

# to define colors you give the RGB values, can be given in a list or a tuple

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 155, 0)
yellow = (200, 200, 0)
light_green = (0, 255, 0)
light_yellow = (255, 255, 0)
light_red = (255, 0, 0)
blue = (0, 0, 255)

ground_height = 35              

 
display_width = 800
display_height = 600
clock = pygame.time.Clock()


# Tank Variables


tank_width = 40
tank_height = 20


turret_width = 5
wheel_width = 5


num_wheels = 7



# barrier variables

x_location = (display_width/2) + random.randint(-0.1*display_width, 0.1*display_width)
barrier_width = 50

random_height = random.randrange(display_height*0.1, display_height*0.6)

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


        button("Play", 150, 500, 100, 50, green, light_green, action="play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, action="controls")
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit")



        pygame.display.update()
        clock.tick(15)


def game_over_1():

    game_over = True
    while game_over:


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

           
            


        gameDisplay.fill(white)
        message_to_screen("GAME OVER",
                            green,
                            -100,
                            'large')
        message_to_screen('You died.',
                            black,
                            -30)

    


        button("Retry", 150, 500, 100, 50, green, light_green, action="play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, action="controls")
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit")



        pygame.display.update()
        clock.tick(15)



def you_win():

    win = True
    while win:


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

           
            


        gameDisplay.fill(white)
        message_to_screen("YOU WON",
                            green,
                            -100,
                            'large')
        message_to_screen('Congratulations!',
                            black,
                            -30)

    


        button("Retry", 150, 500, 100, 50, green, light_green, action="play")
        button("Controls", 350, 500, 100, 50, yellow, light_yellow, action="controls")
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit")



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

# def tank():

#     pygame.draw.rect(gameDisplay, green, (500, 500, 50, 25))

#     pygame.draw.circle(gameDisplay, green, (525, 500), 15, 30)

#     pygame.draw.line(gameDisplay, green, (525, 500), (495, 480), 5)

    



def text_to_button(msg, color, button_x, button_y, btn_width, btn_height, size = "small"):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = ((button_x + (btn_width/2)), (button_y + (btn_height/2)))
    gameDisplay.blit(text_surf, text_rect)

def message_to_screen(msg, color, y_displace=0, size = 'small'): 
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    text_surface, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(text_surface, text_rect)


def get_btn_color(btn_color1, btn_color2, btn_x, btn_y, width, height):

            cursor = pygame.mouse.get_pos()

            if (cursor[0] > btn_x and cursor[0] < (btn_x+width)) and (cursor[1] > btn_y and cursor[1] < (btn_y+height)):

                btn_color = btn_color1
            else:
                btn_color = btn_color2

            return btn_color

def controls():

    gcont = True
    while gcont:


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
        message_to_screen("Controls",
                            green,
                            -100,
                            'large')
        message_to_screen('Fire: SPACEBAR',
                            black,
                            -30)

        message_to_screen('Move Turret: UP AND DOWN ARROWS',
                            black,
                            10)


        message_to_screen('Move Tank: LEFT AND RIGHT ARROWS',
                            black,
                            50)

        message_to_screen('Adjust Fire Power: A AND D KEYS',
                            black,
                            90)

        message_to_screen("Pause: P", black, 130)



        button("Play", 150, 500, 100, 50, green, light_green, action="play")

        button("Main", 350, 500, 100, 50, yellow, light_yellow, action="main")
        
        button("Quit", 550, 500, 100, 50, red, light_red, action="quit")


        pygame.display.update()
        clock.tick(15)


def tank(x, y, turPos):

    x = int(x)
    y = int(y)

    possible_turrets = [(x-27, y-2), 
                        (x-26, y-5), 
                        (x-25, y-8), 
                        (x-23, y-12), 
                        (x-20, y-14),
                        (x-18, y-15),
                        (x-15, y-17),
                        (x-13, y-19),
                        (x-11, y-21),
                        ]
    

    

    

    # tank body
    pygame.draw.circle(gameDisplay, blue, (x, y), int(tank_height/2))
    pygame.draw.rect(gameDisplay, blue, ((x - tank_height), y, tank_width, tank_height))


    # tank gun
    pygame.draw.line(gameDisplay, blue, (x, y), possible_turrets[turPos], turret_width)

    # tank wheels

    wheel_pos = -15

    for i in range(num_wheels):

        pygame.draw.circle(gameDisplay, blue, (x+wheel_pos, y+20), wheel_width)
        wheel_pos += 5

    return possible_turrets[turPos]



def enemytank(x, y, turPos):

    x = int(x)
    y = int(y)

    possible_turrets = [(x+27, y-2), 
                        (x+26, y-5), 
                        (x+25, y-8), 
                        (x+23, y-12), 
                        (x+20, y-14),
                        (x+18, y-15),
                        (x+15, y-17),
                        (x+13, y-19),
                        (x+11, y-21),
                        ]
    

    

    

    # tank body
    pygame.draw.circle(gameDisplay, red, (x, y), int(tank_height/2))
    pygame.draw.rect(gameDisplay, red, ((x - tank_height), y, tank_width, tank_height))


    # tank gun
    pygame.draw.line(gameDisplay, red, (x, y), possible_turrets[turPos], turret_width)

    # tank wheels

    wheel_pos = -15

    for i in range(num_wheels):

        pygame.draw.circle(gameDisplay, red, (x+wheel_pos, y+20), wheel_width)
        wheel_pos += 5

    return possible_turrets[turPos]

def button(text, x, y, width, height, color1, color2, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, color2, (x, y, width, height))
        if click[0] == 1 and action != None: 
            if action == 'quit':
                pygame.quit()
                quit()

            if action == 'controls':
                controls()

            if action == 'play':
                game_loop()

            if action == 'main':
                game_intro()


            
    else:
        pygame.draw.rect(gameDisplay, color1, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)



def barrier(x_location, random_height, barrier_width):


    pygame.draw.rect(gameDisplay, yellow, (x_location, display_height-random_height, barrier_width, random_height))



def explosion(x, y, size=50):


    pygame.mixer.Sound.play(boom_sound)

    explode = True


    while explode:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x, y
        color_choices = [red, light_red, yellow, light_yellow]


        magnitude = 1


        while magnitude < size:

            exploding_bit_x = x + random.randrange(-1*magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude, magnitude)

            pygame.draw.circle(gameDisplay, color_choices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y), random.randrange(1, 5))

            magnitude += 1

            pygame.display.update()
            clock.tick(100)

            explode = False





def e_fire_shell(xy, tankx, tanky, turPos, power, p_tank_x, p_tank_y):


    pygame.mixer.Sound.play(fire_sound)

    damage = 0
    current_power = 1
    power_found = False

    while not power_found:
        current_power += 1

        if current_power>100:
            power_found = True

        fire = True

        starting_shell = list(xy)
        
        while fire:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


          
            # pygame.draw.circle(gameDisplay, blue, (starting_shell[0], starting_shell[1]), 5)

            starting_shell[0] += (12 - turPos)*2

            # y = x**2 most basic quadratic equation

            
            
            starting_shell[1] += int(((starting_shell[0] -xy[0])*(0.015/(current_power/50)))**2) - (turPos+turPos/(12-turPos))

            if starting_shell[1] > display_height-ground_height:

                hit_x = int((starting_shell[0]*display_height-ground_height)/starting_shell[1])
                hit_y = int(display_height-ground_height)
              
                

                #explosion(hit_x, hit_y)

                if (p_tank_x+15) > hit_x > (p_tank_x-15):
                    print("TARGET ACQUIRED...")
                    power_found = True

                fire = False                                                                           

            check_x_1 = starting_shell[0] <= x_location + barrier_width
            check_x_2 = starting_shell[0] >= x_location
            check_y_1 = starting_shell[1] <= display_height
            check_y_2 = starting_shell[1] >= display_height - random_height

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:

                #explosion(starting_shell[0], starting_shell[1])
                fire = False    



    fire = True

    starting_shell = list(xy)
    print("FIRE!", xy)

    while fire:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        # print(starting_shell[0], starting_shell[1])
        pygame.draw.circle(gameDisplay, blue, (starting_shell[0], starting_shell[1]), 5)

        starting_shell[0] += (12 - turPos)*2

        gun_power = random.randrange(int(current_power*0.70), int(current_power*1.30)) 


        # y = x**2 most basic quadratic equation
        starting_shell[1] += int(((starting_shell[0] -xy[0])*(0.015/(gun_power/50 )))**2) - (turPos+turPos/(12-turPos))

        if starting_shell[1] > display_height-ground_height:

            print("Last shell: ", starting_shell[0], starting_shell[1])
            hit_x = int((starting_shell[0]*display_height-ground_height)/starting_shell[1])
            hit_y = int(display_height-ground_height)
            print('Impact:', hit_x, hit_y)


          

            if p_tank_x + 10 > hit_x > p_tank_x - 10:
                print("Critical hit!!")
                damage = 25
            elif p_tank_x + 15 > hit_x > p_tank_x - 15:
                print("Hard hit!!")
                damage = 18
            elif p_tank_x + 25 > hit_x > p_tank_x - 25:
                print("Medium hit!!")
                damage = 10
            elif p_tank_x + 35 > hit_x > p_tank_x - 35:
                print("Light hit!!")
                damage = 5
            
            else:
                print("ENEMY MISS")


            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = starting_shell[0] <= x_location + barrier_width
        check_x_2 = starting_shell[0] >= x_location
        check_y_1 = starting_shell[1] <= display_height
        check_y_2 = starting_shell[1] >= display_height - random_height

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:

            explosion(starting_shell[0], starting_shell[1])
            fire = False

        pygame.display.update()
        clock.tick(60)


    return damage





def fire_shell(xy, tankx, tanky, turPos, power, enemy_tank_x, enemy_tank_y):

    pygame.mixer.Sound.play(fire_sound)

    damage = 0

    fire = True

    starting_shell = list(xy)
    print("FIRE!", xy)

    while fire:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        # print(starting_shell[0], starting_shell[1])
        pygame.draw.circle(gameDisplay, blue, (starting_shell[0], starting_shell[1]), 5)

        

      
        starting_shell[0] -= (12 - turPos)*2


        # y = x**2 most basic quadratic equation
        starting_shell[1] += int(((starting_shell[0] -xy[0])*(0.015/(power/50 )))**2) - (turPos+turPos/(12-turPos))

        if starting_shell[1] > display_height-ground_height:

            print("Last shell: ", starting_shell[0], starting_shell[1])
            hit_x = int((starting_shell[0]*display_height-ground_height)/starting_shell[1])
            hit_y = int(display_height-ground_height)
            print('Impact:', hit_x, hit_y)


            if enemy_tank_x + 10 > hit_x > enemy_tank_x - 10:
                print("Critical hit!!")
                damage = 25
            elif enemy_tank_x + 15 > hit_x > enemy_tank_x - 15:
                print("Hard hit!!")
                damage = 18
            elif enemy_tank_x + 25 > hit_x > enemy_tank_x - 25:
                print("Medium hit!!")
                damage = 10
            elif enemy_tank_x + 35 > hit_x > enemy_tank_x - 35:
                print("Light hit!!")
                damage = 5

            else:
                print("PLAYER MISS")

            explosion(hit_x, hit_y)
            fire = False

        


        check_x_1 = starting_shell[0] <= x_location + barrier_width
        check_x_2 = starting_shell[0] >= x_location
        check_y_1 = starting_shell[1] <= display_height
        check_y_2 = starting_shell[1] >= display_height - random_height

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:

            explosion(starting_shell[0], starting_shell[1])
            fire = False

        pygame.display.update()
        clock.tick(60)

    return damage


        
def power(level):

    text = smallfont.render("Power: " + str(level) + "%", True, white)

    gameDisplay.blit(text, [display_width/2, 0])

    

def health_bars(player_health, enemy_health):

    if player_health>75:
        player_health_color = green
    elif player_health>50:
        player_health_color = yellow
    else:
        player_health_color = red

    if enemy_health>75:
        enemy_health_color = green
    elif enemy_health>50:
        enemy_health_color = yellow
    else:
        enemy_health_color = red




    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))

    pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))



def game_loop():

    game_exit = False
    game_over = False
    FPS = 15

    # TANK

    main_tank_x = display_width * 0.9
    main_tank_y = display_height * 0.9
    tank_move = 0
    current_tur_pos = 0
    change_tur = 0

    # ENEMY

    enemy_tank_x = display_width * 0.1
    enemy_tank_y = display_height * 0.9
    
    player_health = 100
    enemy_health = 100

    


    fire_power = 50
    power_change = 0

    
    
    

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
                    tank_move = -5

                elif event.key == pygame.K_RIGHT:
                    tank_move = 5

                elif event.key == pygame.K_UP:
                    change_tur = 1

                elif event.key == pygame.K_DOWN:
                    change_tur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:

                    # PLAYER FIRES
                    damage = fire_shell(gun, main_tank_x, main_tank_y, current_tur_pos, fire_power, enemy_tank_x, enemy_tank_y)
                    enemy_health -= damage

                    possible_movement = ['f', 'r']
                    move_index = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):
                          if enemy_tank_x > 20 and enemy_tank_x < (display_width-20):
                            if possible_movement[move_index] == 'f':
                                enemy_tank_x += 5
                            elif possible_movement[move_index] == 'r':
                                enemy_tank_x -= 5

                            gameDisplay.fill(black)
                            health_bars(player_health, enemy_health)
                            gun = tank(main_tank_x, main_tank_y, current_tur_pos)
                            enemy_gun = enemytank(enemy_tank_x, enemy_tank_y, 8)
                            fire_power += power_change

                            power(fire_power)

                            barrier(x_location, random_height, barrier_width)
                            gameDisplay.fill(green, rect=[0, display_height-ground_height, display_width, ground_height])
                            pygame.display.update()
                            clock.tick(FPS)

                    # ENEMY FIRES
                    damage = e_fire_shell(enemy_gun, enemy_tank_x, enemy_tank_y, 8, 50, main_tank_x, main_tank_y)
                    player_health -= damage


                    
                elif event.key == pygame.K_a:
                    power_change = -1

                elif event.key == pygame.K_d:
                    power_change = 1

        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tank_move = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    change_tur = 0
      

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0

            

    # EVENT HANDLING AND THEN A GROUP OF LOGIC STATEMENTS, THEN GRAPHICS RENDERING AND THEN UPDATE THE DISPLAY
    #  THIS ALL HAPPENS EVERY FRAME PER SCOND, SO OPTIMISATION MAKES SENSE


    # LOGIC



        # draw everything and then render to save resources
        

        main_tank_x += tank_move

        current_tur_pos += change_tur

        if current_tur_pos > 8:
            current_tur_pos = 8
        elif current_tur_pos < 0:
            current_tur_pos = 0

        
        
        

        # COLLISION DETECTION


        if main_tank_x - (tank_width/2) < (x_location + barrier_width):
            main_tank_x += 5


        gameDisplay.fill(black)
        gun = tank(main_tank_x, main_tank_y, current_tur_pos)

        health_bars(player_health, enemy_health)

        enemy_gun = enemytank(enemy_tank_x, enemy_tank_y, 8)

        # FIRE POWER

        fire_power += power_change

        if fire_power > 100:
            fire_power = 100
        elif fire_power<1:
            fire_power = 1
        


        power(fire_power)
        

        barrier(x_location, random_height, barrier_width)

        gameDisplay.fill(green, rect=[0, display_height-ground_height, display_width, ground_height])

        # draw everything and then render to save resources
        pygame.display.update()

        if player_health <= 1:
            print("game over!!!!1111")
            game_over_1()

        elif enemy_health < 1:
            you_win()


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


