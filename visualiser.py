import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))  # width, height
pygame.display.set_caption("Keyboard - Color")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # TODO update with each color of input
    pygame.display.flip()  # update display
    clock.tick(60)  # 60 fps
pygame.quit()
