import pygame
import sys
from game import Game
from intro import Intro
from leaderboard import Leaderboard
from settings import Settings
from crt import CRT


class GameState:
    def __init__(self):
        self.state = 'intro'
        self.screen_settings = [screen, screen_height, screen_width]
        self.state_manager()

    def main_game(self):
        game = Game(*self.screen_settings)
        game.draw()

    def intro(self):
        self.state = 'intro'
        intro = Intro(*self.screen_settings)
        intro.draw()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_l]:
            self.state = 'leaderboard'
        elif keys[pygame.K_s]:
            self.state = 'settings'

    def leaderboard(self):
        leaderboard = Leaderboard(*self.screen_settings)
        leaderboard.draw()

    def settings(self):
        settings = Settings(*self.screen_settings)
        settings.draw()

    def state_manager(self):
        match self.state:
            case 'intro':
                self.intro()
            case 'main_game':
                self.main_game()
            case 'leaderboard':
                self.leaderboard()
            case 'settings':
                self.settings()


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    crt = CRT(screen, screen.get_height(), screen.get_width())

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)
    game_state = GameState()

    while True:
        screen.fill((30, 30, 30))
        crt.draw()
        game_state.state_manager()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.flip()
