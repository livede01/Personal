import pygame

pygame.init() # Muss als erstes aufgerufen werden
clock = pygame.time.Clock()
width, height = 320, 240 
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

speed = [1, 1]

screen = pygame.display.set_mode((width, height)) 

pygame.display.set_caption('Hallo Bochum!')

running = True
while running: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    screen.fill((255,255,255))
    screen.blit(ball, ballrect)
    clock.tick_busy_loop(50)
    pygame.display.flip()
