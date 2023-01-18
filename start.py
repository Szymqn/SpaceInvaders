import pygame
from leaderboard import Leaderboard
from settings import Settings


class Start:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.font = pygame.font.Font('font/Pixeled.ttf', 20)
        self.status = True  # start surface status
        self.quit = False  # quit game

        screen_settings = [self.screen, self.screen_height, self.screen_width]

        self.leaderboard = Leaderboard(*screen_settings)
        self.settings = Settings(*screen_settings)

    def draw(self):
        keys = pygame.key.get_pressed()

        key_pressed = pygame.K_e if keys[pygame.K_e] else pygame.K_q if keys[pygame.K_q] else pygame.K_l if keys[
            pygame.K_l] else pygame.K_s if keys[pygame.K_s] else None

        if key_pressed:
            match key_pressed:
                case pygame.K_e:
                    self.status = False
                case pygame.K_q:
                    self.status = False
                    self.quit = True
                case pygame.K_l:
                    self.leaderboard.status = True
                case pygame.K_s:
                    self.settings.status = True

        if self.leaderboard.status:
            self.leaderboard.draw()
        elif self.settings.status:
            self.settings.draw()
        else:
            menu_surf = self.font.render('WELCOME TO SPACE INVADERS', False, 'white')
            menu_rect = menu_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) - 190))
            self.screen.blit(menu_surf, menu_rect)

            start_surf = self.font.render('PRESS E TO START', False, 'white')
            start_rect = menu_surf.get_rect(center=((self.screen_width / 2) + 90, (self.screen_height / 2) - 80))
            self.screen.blit(start_surf, start_rect)

            lead_surf = self.font.render('PRESS L TO LEADERBOARD', False, '#AA6C39')
            lead_rect = lead_surf.get_rect(center=((self.screen_width / 2) + 10, (self.screen_height / 2) + 10))
            self.screen.blit(lead_surf, lead_rect)

            settings_surf = self.font.render('PRESS S TO SETTINGS', False, 'white')
            settings_rect = lead_surf.get_rect(center=((self.screen_width / 2) + 40, (self.screen_height / 2) + 100))
            self.screen.blit(settings_surf, settings_rect)

            quit_surf = self.font.render('PRESS Q TO QUIT', False, 'white')
            quit_rect = quit_surf.get_rect(center=((self.screen_width / 2) + 0, (self.screen_height / 2) + 190))
            self.screen.blit(quit_surf, quit_rect)
