import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill(blue)
Pix = pygame.PixelArray(gameDisplay)


# Draw a single pixel
Pix[500, 500] = red


# Draw a line
pygame.draw.line(gameDisplay, green, (10, 10), (500, 500), 20)

# Draw a circle
pygame.draw.circle(gameDisplay, red, (200, 300), 40, 5) # x, y, radius, thickness

# Draw a rectangle
pygame.draw.rect(gameDisplay, green, (150, 140, 100, 100))


# Draw a polygon
pygame.draw.polygon(gameDisplay, red, ((140, 5), (300, 400), (45, 20), (567, 434), (435, 786)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()
