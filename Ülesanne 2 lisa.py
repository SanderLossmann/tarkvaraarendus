import pygame
pygame.init()
import math

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 2")
screen.fill([204, 255, 204])

font1 = pygame.font.SysFont(None, 48)
text1 = "TULEVIK 2050"

center_x = 500
center_y = 200
radius = 90

angle_between = math.radians(20)
start_angle = -angle_between * len(text1) / 4

bg = pygame.image.load("img/bg_shop.jpg")
screen.blit(bg,[0,0])
muua = pygame.image.load("img/seller.png")
muua = pygame.transform.scale(muua, [250, 300])
screen.blit(muua,[100,170])
chat = pygame.image.load("img/chat.png")
screen.blit(chat, [250,40])
VIKK = pygame.image.load("img/VIKK logo.png")
screen.blit(VIKK, [10,10])
Mook = pygame.image.load("img/Mõõk.png")
Mook = pygame.transform.scale(Mook, [250, 250])
screen.blit(Mook, [-130,50])
tort = pygame.image.load("img/tort.png")
tort = pygame.transform.scale(tort, [140, 140])
screen.blit(tort, [260, 170])


font = pygame.font.Font(None, 27)
text = font.render("Tere, minu nimi on Sander", True, [255, 255, 255])
screen.blit(text, [280,140])

gameover = False
while not gameover:

    for i, char in enumerate(text1):
        angle = start_angle + i * angle_between
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        char_surf = font.render(char, True, (255, 255, 255))
        rect = char_surf.get_rect(center=(x, y))
        screen.blit(char_surf, rect)
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.flip()
pygame.quit()
