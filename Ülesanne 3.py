import pygame
pygame.init()

WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ruutudega täidetud ekraan")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)


def draw_squares(square_size, rows, cols, line_color):
    for x in range(0, cols * square_size, square_size):
        for y in range(0, rows * square_size, square_size):
            pygame.draw.rect(SCREEN, line_color, (x, y, square_size, square_size), 1)


running = True
while running:
    SCREEN.fill(WHITE)
    draw_squares(20, HEIGHT // 20, WIDTH // 20, RED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
