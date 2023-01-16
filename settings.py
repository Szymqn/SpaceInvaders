import pygame


class Settings:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.status = False

    def set_difficulty(self):
        pass

    def submit(self):
        self.status = True

    def draw(self):
        pass
