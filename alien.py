import pygame
import os
import sys


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        # file_path = os.path.join('graphics', f'{color}.png')
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_path, 'graphics', f'{color}.png')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Image file not found: {file_path}")
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        match color:
            case 'red':
                self.value = 100
            case 'green':
                self.value = 200
            case 'yellow':
                self.value = 300
            case 'blue':
                self.value = 400
            case 'purple':
                self.value = 500

    def update(self, direction):
        self.rect.x += direction


class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        # self.image = pygame.image.load('graphics/extra.png').convert_alpha()
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_path, 'graphics', 'extra.png')
        self.image = pygame.image.load(image_path).convert_alpha()

        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(center=(x, 80))

    def update(self):
        self.rect.x += self.speed
