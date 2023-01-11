import pygame
import sys
from game import Game
from start import Start
from crt import CRT


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    screen_setting = [screen, screen_height, screen_height]
    start = Start(*screen_setting)
    game = Game(*screen_setting)
    crt = CRT(*screen_setting)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    def to_menu():
        start.status = True
        game.status = False
        game.game_restart = True
        game.restart()

    while True:
        screen.fill((30, 30, 30))
        crt.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER and start.status is False:
                game.alien_shoot()

        if start.status:
            start.draw()
        elif game.status:
            to_menu()
        else:
            game.run()

        pygame.display.flip()
        clock.tick(60)
