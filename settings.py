import pygame
import os
import sys

def set_level(default):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        return 1
    elif keys[pygame.K_2]:
        return 2
    elif keys[pygame.K_3]:
        return 3
    elif keys[pygame.K_4]:
        return 4
    elif keys[pygame.K_5]:
        return 5

    return default


class Settings:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        # self.font = pygame.font.Font('font/Pixeled.ttf', 20)
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        font_path = os.path.join(base_path, 'font', 'Pixeled.ttf')
        self.font = pygame.font.Font(font_path, 20)

    def draw(self):
        center_x = self.screen_width / 2

        level_surf = self.font.render('SET DIFFICULTY LEVEL', False, 'white')
        level_rect = level_surf.get_rect(center=(center_x, self.screen_height / 2 - 260))
        self.screen.blit(level_surf, level_rect)

        v_easy_surf = self.font.render('VERY EASY - 1', False, 'white')
        v_easy_rect = v_easy_surf.get_rect(center=(center_x, self.screen_height / 2 - 200))
        self.screen.blit(v_easy_surf, v_easy_rect)

        easy_surf = self.font.render('EASY - 2', False, 'white')
        easy_rect = easy_surf.get_rect(center=(center_x, self.screen_height / 2 - 140))
        self.screen.blit(easy_surf, easy_rect)

        medium_surf = self.font.render('MEDIUM - 3', False, 'white')
        medium_rect = medium_surf.get_rect(center=(center_x, self.screen_height / 2 - 80))
        self.screen.blit(medium_surf, medium_rect)

        hard_surf = self.font.render('HARD - 4', False, 'white')
        hard_rect = hard_surf.get_rect(center=(center_x, self.screen_height / 2 - 20))
        self.screen.blit(hard_surf, hard_rect)

        v_hard_surf = self.font.render('VERY HARD - 5', False, 'white')
        v_hard_rect = hard_surf.get_rect(center=(center_x - 45, self.screen_height / 2 + 40))
        self.screen.blit(v_hard_surf, v_hard_rect)

        manu_surf = self.font.render('PRESS M TO MENU', False, 'white')
        menu_rect = manu_surf.get_rect(center=(center_x, self.screen_height / 2 + 100))
        self.screen.blit(manu_surf, menu_rect)
