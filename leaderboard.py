import pygame


class Leaderboard:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.font = pygame.font.Font('font/Pixeled.ttf', 20)
        self.status = True

    @staticmethod
    def get_records():
        file = open('records/leaderboard', 'r')
        temp = file.read().strip().split(' ')
        records = list(map(int, temp))
        records.sort(reverse=True)
        file.close()
        return records

    def draw(self):
        records = self.get_records()

        pos = 1
        offset = 40
        gold_color = '#AA6C39'

        head_surf = self.font.render('TOP 10 SCORES', False, gold_color)
        head_rect = head_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) - 240))
        self.screen.blit(head_surf, head_rect)

        for i in range(10):
            try:
                value = records[i]
            except IndexError:
                records.append(None)
                value = None

            score_surf = self.font.render(f'{pos}: {value}', False, gold_color)

            score_rect = score_surf.get_rect(center=(self.screen_width / 2, ((self.screen_height / 2) - 220) + offset))
            offset += 40
            print(offset)
            self.screen.blit(score_surf, score_rect)
            pos += 1

        quit_surf = self.font.render('PRESS Q TO QUIT', False, gold_color)
        quit_rect = quit_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) + 240))
        self.screen.blit(quit_surf, quit_rect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.status = False
