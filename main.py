import os

import pygame
import sys
from game import Game
from intro import Intro
from leaderboard import Leaderboard
from settings import Settings, set_level
from crt import CRT


def get_player_name(screen, font):
    input_box = pygame.Rect(100, 300, 400, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))

        name_surf = font.render('Enter your name:', False, color_inactive)
        name_rect = name_surf.get_rect(center=(screen.get_width() / 2, (screen.get_height() / 2) - 240))
        screen.blit(name_surf, name_rect)

        txt_surface = font.render(text, True, color)
        width = max(400, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

    return text


class GameState:
    def __init__(self):
        self.state = 'intro'
        self.screen_settings = [screen, screen_height, screen_width]
        self.level = 1

    def intro(self):
        self.state = 'intro'
        intro = Intro(*self.screen_settings)
        intro.draw()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    def leaderboard(self):
        leaderboard = Leaderboard(*self.screen_settings)
        leaderboard.draw()

    def settings(self):
        settings = Settings(*self.screen_settings)
        settings.draw()

        self.level = set_level(self.level)
        game.change_level(self.level)

    def key_interpreter(self):
        keys = pygame.key.get_pressed()

        if self.state == 'intro':
            if keys[pygame.K_e]:
                self.state = 'main_game'
            elif keys[pygame.K_s]:
                self.state = 'settings'
            elif keys[pygame.K_l]:
                self.state = 'leaderboard'
        else:
            if keys[pygame.K_m]:
                self.state = 'intro'

    def state_manager(self):
        match self.state:
            case 'intro':
                self.intro()
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

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    font_path = os.path.join(base_path, 'font', 'Pixeled.ttf')
    font = pygame.font.Font(font_path, 20)
    player_name = get_player_name(screen, font)
    print(f"Player name: {player_name}")

    game = Game(screen, screen.get_height(), screen.get_width(), player_name)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)
    game_state = GameState()

    while True:
        screen.fill((30, 30, 30))
        crt.draw()
        game_state.state_manager()
        game_state.key_interpreter()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER and game_state.state == "main_game":
                game.alien_shoot()

        if game_state.state == "main_game":
            game.draw()

        clock.tick(60)
        pygame.display.flip()
