import pygame
pygame.init()

screen=pygame.display.set_mode([200, 600])
pygame.display.set_caption("Foor - Sander Lossmann")

#värvid
Punane = (255, 0, 0)
Kollane = (255, 255, 0)
Roheline = (0, 255, 0)
Must = (0, 0, 0)
Hall = (128, 128, 128)
Sinine = (0, 0, 255)
Valge = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Must)

    #joonistame
    pygame.draw.rect(screen, Hall, [50, 50, 100, 247], 2)
    pygame.draw.circle(screen, Punane, [100, 100], 35, 35)
    pygame.draw.circle(screen, Kollane, [100, 175], 35, 35)
    pygame.draw.circle(screen, Roheline, [100, 250], 35, 35)
    pygame.draw.rect(screen, Hall, [90, 295, 25, 250], 2)
    pygame.draw.line(screen, Hall, [80,545], [125,545], 2)
    pygame.draw.line(screen, Hall, [125,545], [140, 580], 2)
    pygame.draw.line(screen, Hall, [140, 580], [65, 580], 2)
    pygame.draw.line(screen, Hall, [65, 580], [80, 545], 2)
    pygame.draw.rect(screen, Sinine, [85, 548, 37,10], 5)
    pygame.draw.rect(screen, Hall, [85, 558, 37,10], 1)
    pygame.draw.rect(screen, Valge, [85, 568, 37, 10], 5)


    pygame.display.flip()
