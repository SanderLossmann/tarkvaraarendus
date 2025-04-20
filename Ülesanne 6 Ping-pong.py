import pygame
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ping-pong")
clock = pygame.time.Clock()

pygame.mixer.music.load('music/song18.mp3')
pygame.mixer.music.play(-1)

sinine = (51, 204, 255)

Alus = pygame.image.load("img/pad.png")
Alus = pygame.transform.scale(Alus, [120, 20])
Pall = pygame.image.load("img/ball.png")
Pall = pygame.transform.scale(Pall, [20, 20])

posX, posY = 0, 100
speedX, speedY = 4, 7

PosX, PosY = 0, 320
SpeedX, SpeedY = 0, 0

score = 0

gameover = False

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                SpeedX = 4
            if event.key == pygame.K_LEFT:
                SpeedX = -4

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                SpeedX = 0

    screen.fill(sinine)

    posX += speedX
    posY += speedY
    PosX += SpeedX

    if posX > 640 - Pall.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > 480 - Pall.get_rect().height or posY < 0:
        speedY = -speedY

    if PosX > 640 - Alus.get_rect().width or PosX < 0:
        SpeedX = 0

    if posY > 480 - Pall.get_rect().height:
        gameover = True
        pygame.quit()

    pall_rect = pygame.Rect(posX, posY, Pall.get_width(), Pall.get_height())
    alus_rect = pygame.Rect(PosX, PosY, Alus.get_width(), Alus.get_height())

    if pall_rect.colliderect(alus_rect):
        if posY + Pall.get_height() <= PosY + 5:
            score += 1

        speedY = -speedY

    screen.blit(Alus, (PosX, PosY))
    screen.blit(Pall, (posX, posY))


    font = pygame.font.SysFont(None, 25)
    score_text = font.render(f"Skoor: {score}", True, (0, 0, 0))
    screen.blit(score_text, (0, 0))

    pygame.display.flip()