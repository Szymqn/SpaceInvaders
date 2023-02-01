import pygame
import sys
from game import Game
from start import Start
from crt import CRT


class GameState:
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        game = Game(*screen_setting)
        game.run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER and start.status is False:
                game.alien_shoot()

        pygame.display.flip()

    def state_manager(self):
        match self.state:
            case 'intro':
                self.intro()


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    screen_setting = [screen, screen_height, screen_height]
    crt = CRT(*screen_setting)
    game_state = GameState()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    while True:
        screen.fill((30, 30, 30))
        crt.draw()
        game_state.intro()

        clock.tick(60)
