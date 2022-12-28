import pygame


class Start:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.font = pygame.font.Font('font/Pixeled.ttf', 20)
        self.status = True

    def draw(self):
        menu_surf = self.font.render('WELCOME TO SPACE INVADERS', False, 'white')
        menu_rect = menu_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) - 80))
        self.screen.blit(menu_surf, menu_rect)

        start_surf = self.font.render('PRESS E TO START', False, 'white')
        start_rect = menu_surf.get_rect(center=((self.screen_width / 2) + 80, (self.screen_height / 2) + 10))
        self.screen.blit(start_surf, start_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.status = False
