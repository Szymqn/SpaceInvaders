import pygame
import sys
from game import Game
from intro import Intro
from settings import Settings
from crt import CRT


class GameState:
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        intro = Intro(screen, screen.get_height(), screen.get_width())
        intro.draw()

    def main_game(self):
        game = Game(screen, screen.get_height(), screen.get_width())
        game.draw()

    def settings(self):
        settings = Settings(screen, screen.get_height(), screen.get_width())
        settings.draw()

    def state_manager(self):
        match self.state:
            case 'intro':
                self.intro()
            case 'main_game':
                self.main_game()
            case 'settings':
                self.settings()


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
