import pygame
pygame.init()

IGreen = [153, 255, 153]

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ralliauto mäng")
screen.fill(IGreen)
clock = pygame.time.Clock()

Rally = pygame.image.load("img/bg_rally.jpg")
Rally = pygame.transform.scale(Rally, [640, 480])

punane_auto = pygame.image.load("img/f1_red.png")
sinine_auto = pygame.image.load("img/f1_blue.png")


sinine_auto = pygame.transform.rotate(sinine_auto, 180)

PosX, PosY = 420, 100
posX, posY = 180, 200
posx, posy = 270, 0
POSX, POSY = 330, 0

speed = 4
Speed = 6
SPEED = 5
speeD = 3
speedX = 0
punase_auto_posX = 300

gameover = False
score = 0

def check_collision(punane_rect, sinine_rects):
    for sinine_rect in sinine_rects:
        if punane_rect.colliderect(sinine_rect):
            return True
    return False

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speedX = 3
            elif event.key == pygame.K_LEFT:
                speedX = -3
            elif event.key == pygame.K_RETURN and gameover:
                # Kui mäng on läbi, alusta uuesti
                punase_auto_posX = 300
                PosY = 200
                posY = 0
                posy = 0
                POSY = 0
                speedX = 0
                gameover = False
                score = 0
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                speedX = 0

    if not gameover:
        punase_auto_posX += speedX

        if punase_auto_posX < 140:
            punase_auto_posX = 140
        if punase_auto_posX > 500 - punane_auto.get_width():
            punase_auto_posX = 500 - punane_auto.get_width()

        posY += Speed
        PosY += speed
        posy += SPEED
        POSY += speeD


        if PosY > 480:
            PosY = -sinine_auto.get_height()
            score += 1

        if posY > 480:
            posY = -sinine_auto.get_height()
            score += 1

        if posy > 480:
            posy = -sinine_auto.get_height()
            score += 1

        if POSY > 480:
            POSY = -sinine_auto.get_height()
            score += 1

        punase_auto_rect = pygame.Rect(punase_auto_posX, 390, punane_auto.get_width(), punane_auto.get_height())
        sinised_autod_rects = [
            pygame.Rect(PosX, PosY, sinine_auto.get_width(), sinine_auto.get_height()),
            pygame.Rect(posX, posY, sinine_auto.get_width(), sinine_auto.get_height()),
            pygame.Rect(posx, posy, sinine_auto.get_width(), sinine_auto.get_height()),
            pygame.Rect(POSX, POSY, sinine_auto.get_width(), sinine_auto.get_height())
        ]

        if check_collision(punase_auto_rect, sinised_autod_rects):
            gameover = True

    screen.blit(Rally, [0, 0])
    screen.blit(punane_auto, (punase_auto_posX, 390))
    screen.blit(sinine_auto, (PosX, PosY))
    screen.blit(sinine_auto, (posX, posY))
    screen.blit(sinine_auto, (posx, posy))
    screen.blit(sinine_auto, [POSX, POSY])

    # Kuvame skoori
    font = pygame.font.SysFont(None, 25)
    score_text = font.render(f"Skoor: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if gameover:
        # Kui mäng on läbi, kuvame skoori
        game_over_text = font.render(f"Mäng Läbi! Skoor: {score}. Uuesti alustamiseks ENTER. Väljumiseks ESC.", True, (0, 0, 0))
        screen.blit(game_over_text, (50, 200))

    pygame.display.flip()