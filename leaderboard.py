import pygame


class Leaderboard:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.font = pygame.font.Font('font/Pixeled.ttf', 20)
        self.status = True
        self.quit = False

    def get_records(self):
        file = open('records/leaderboard', 'r')
        temp = file.read().strip().split(' ')
        records = list(map(int, temp))
        records.sort(reverse=True)
        print(records)
        file.close()

    def draw(self):
        self.get_records()
        pass
