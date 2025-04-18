import pygame
pygame.init()

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ping-pong")
clock = pygame.time.Clock()

sinine = (51, 204, 255)

Alus = pygame.image.load("img/pad.png")
Alus = pygame.transform.scale(Alus, [120, 20])
Pall = pygame.image.load("img/ball.png")
Pall = pygame.transform.scale(Pall, [20, 20])

posX, posY = 0, 100
speedX, speedY = 4, 7

PosX, PosY = 0, 320
SpeedX, SpeedY = 4, 4

score = 0

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(sinine)

    posX += speedX
    posY += speedY
    PosX += SpeedX

    if posX > 640 - Pall.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > 480 - Pall.get_rect().height or posY < 0:
        speedY = -speedY

    if PosX > 640 - Alus.get_rect().width or PosX < 0:
        SpeedX = -SpeedX

    pall_rect = pygame.Rect(posX, posY, Pall.get_width(), Pall.get_height())
    alus_rect = pygame.Rect(PosX, PosY, Alus.get_width(), Alus.get_height())

    if pall_rect.colliderect(alus_rect):
        if posY + Pall.get_height() <= PosY + 5:
            score += 1
        elif posY >= PosY + Alus.get_height() - 5:
            score -= 1
        speedY = -speedY

    screen.blit(Alus, (PosX, PosY))
    screen.blit(Pall, (posX, posY))


     # Kuvame skoori
    font = pygame.font.SysFont(None, 25)
    score_text = font.render(f"Skoor: {score}", True, (0, 0, 0))
    screen.blit(score_text, (0, 0))

    pygame.display.flip()

pygame.quit()