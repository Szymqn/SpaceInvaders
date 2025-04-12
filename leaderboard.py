import pygame
import os
import sys


class Leaderboard:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        font_path = os.path.join(base_path, 'font', 'Pixeled.ttf')
        self.font = pygame.font.Font(font_path, 20)

    @staticmethod
    def get_records():
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        leaderboard_path = os.path.join(base_path, 'records', 'leaderboard')
        with open(leaderboard_path, 'r') as f:
            temp = f.read().strip().split('\n')

        records = []
        for line in temp:
            try:
                name, score = line.split(': ')
                records.append((name, int(score)))
            except ValueError:
                continue

        records.sort(key=lambda x: x[1], reverse=True)
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
                name, score = records[i]
            except IndexError:
                name, score = None, None

            score_text = f'{pos}: {name} - {score}' if name and score else f'{pos}: ---'
            score_surf = self.font.render(score_text, False, gold_color)

            score_rect = score_surf.get_rect(center=(self.screen_width / 2, ((self.screen_height / 2) - 220) + offset))
            offset += 40
            self.screen.blit(score_surf, score_rect)
            pos += 1

        quit_surf = self.font.render('PRESS M TO BACK', False, gold_color)
        quit_rect = quit_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) + 240))
        self.screen.blit(quit_surf, quit_rect)
