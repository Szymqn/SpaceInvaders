import pygame
from Levels import Levels


class Settings:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.status = False
        self.font = pygame.font.Font('font/Pixeled.ttf', 20)
        self.level = Levels

    def go_back(self):
        self.status = False

    def draw(self):
        level_surf = self.font.render('SET DIFFICULTY LEVEL', False, 'white')
        level_rect = level_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2 - 140))
        self.screen.blit(level_surf, level_rect)

        easy_surf = self.font.render('EASY - 1', False, 'white')
        easy_rect = easy_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2 - 80))
        self.screen.blit(easy_surf, easy_rect)

        medium_surf = self.font.render('MEDIUM - 2', False, 'white')
        medium_rect = medium_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2 - 20))
        self.screen.blit(medium_surf, medium_rect)

        hard_surf = self.font.render('HARD - 3', False, 'white')
        hard_rect = hard_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2 + 40))
        self.screen.blit(hard_surf, hard_rect)

        manu_surf = self.font.render('PRESS M TO MENU', False, 'white')
        menu_rect = manu_surf.get_rect(center=(self.screen_width / 2, self.screen_height / 2 + 100))
        self.screen.blit(manu_surf, menu_rect)

        keys = pygame.key.get_pressed()

        # submit
        if keys[pygame.K_m]:
            self.go_back()
        # change level
        elif keys[pygame.K_1]:
            self.level(1)
        elif keys[pygame.K_2]:
            self.level(2)
        elif keys[pygame.K_3]:
            self.level(3)
