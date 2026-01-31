import pygame
from constants import *
from logger import log_state

def main():
    print(("Starting Asteroids with pygame version: " 
            f"{pygame.version.ver}"))

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill("black")

        pygame.display.flip()


if __name__ == "__main__":
    main()
