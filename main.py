import pygame
import sys
from game import Game
from intro import IntroState
from crt import CRT


class GameState:
    def __init__(self):
        self.state = 'intro'
        self.screen_settings = [screen, screen_height, screen_width]
        self.state_manager()

    def intro(self):
        IntroState(*self.screen_settings)

    def main_game(self):
        game = Game(*self.screen_settings)
        game.draw()

    def state_manager(self):
        match self.state:
            case 'intro':
                self.intro()
            case 'main_game':
                self.main_game()


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    crt = CRT(screen, screen.get_height(), screen.get_width())
    game_state = GameState()

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    while True:
        screen.fill((30, 30, 30))
        crt.draw()
        game_state.intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.flip()
