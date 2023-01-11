import pygame
import obstacle
from random import choice, randint
from alien import Alien, Extra
from laser import Laser
from player import Player


class Game:
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.game_restart = True
        self.victory_status = True
        self.status = False
        self.quit = False
        self.score_record = True

        # Player setup
        player_sprite = Player((self.screen_width / 2, self.screen_height), self.screen_width, speed=5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # health and score setup
        self.lives = 3
        self.live_surf = pygame.image.load('graphics/player.png').convert_alpha()
        self.live_x_start_pos = screen_width - (self.live_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = pygame.font.Font('font/Pixeled.ttf', 20)

        # Obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start=screen_width / 15, y_start=480)

        # Alien setup
        self.rows = 6
        self.cols = 8
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup(self.rows, self.cols)
        self.alien_direction = 1

        # Extra setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(40, 80)

        # Audio
        music = pygame.mixer.Sound('audio/music.wav')
        music.set_volume(0.04)
        # infinity loop
        music.play(loops=-1)
        self.laser_sound = pygame.mixer.Sound('audio/laser.wav')
        self.laser_sound.set_volume(0.06)
        self.explosion_sound = pygame.mixer.Sound('audio/explosion.wav')
        self.explosion_sound.set_volume(0.06)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def obstacles_destroy(self):
        self.blocks.empty()

    def alien_setup(self, rows, cols, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien('yellow', x, y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien('green', x, y)
                else:  # >= 3:
                    alien_sprite = Alien('red', x, y)
                self.aliens.add(alien_sprite)

    def aliens_destroy(self):
        self.aliens.empty()

    def aline_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= self.screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_move_down(2)
                self.alien_direction = 1

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, self.screen_height)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(['right', 'left']), self.screen_width))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):
        # player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                # alien collisions
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()
                    self.explosion_sound.play()

                # extra collisions
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    self.score += 500
                    laser.kill()

        # alien lasers
        if self.alien_lasers:
            for laser in self.alien_lasers:
                # obstacle collisions
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()

                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        self.victory_status = False
                        self.restart_message()

        # aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    self.victory_status = False
                    self.restart_message()

    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
            self.screen.blit(self.live_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render('score:' + str(self.score), False, 'white')
        score_rect = score_surf.get_rect(topleft=(10, -10))
        self.screen.blit(score_surf, score_rect)

    def victory(self):
        if not self.aliens.sprites():
            self.restart_message()

    def restart_message(self):
        self.extra_spawn_time = 1
        self.game_restart = False
        self.obstacles_destroy()
        self.aliens_destroy()
        self.alien_lasers.empty()

        if self.victory_status:
            message_surf = self.font.render('You Won!', False, 'white')
        else:
            message_surf = self.font.render('You Lose!', False, 'white')

        message_rect = message_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) - 180))
        self.screen.blit(message_surf, message_rect)

        score_surf = self.font.render(f'YOUR SCORE: {self.score}', False, 'white')
        score_rect = score_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) - 120))
        self.screen.blit(score_surf, score_rect)

        self.score_message()

        restart_surf = self.font.render('PRESS R TO RESTART', False, 'white')
        restart_rect = restart_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2)))
        self.screen.blit(restart_surf, restart_rect)

        menu_surf = self.font.render('PRESS M TO MENU', False, 'white')
        menu_rect = menu_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) + 60))
        self.screen.blit(menu_surf, menu_rect)

        quit_surf = self.font.render('PRESS Q TO QUIT', False, 'white')
        quit_rect = menu_surf.get_rect(center=((self.screen_width / 2), (self.screen_height / 2) + 120))
        self.screen.blit(quit_surf, quit_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.game_restart = True
            self.restart()
        elif keys[pygame.K_m]:
            self.status = True
        elif keys[pygame.K_q]:
            self.quit = True

    def score_message(self):
        self.leaderboard()

        if self.score <= int(self.high_score()):
            h_score_surf = self.font.render(f'HIGH SCORE: {self.high_score()}', False, 'white')
            h_score_rect = h_score_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) - 60))
            self.screen.blit(h_score_surf, h_score_rect)
        else:
            new_h_score_surf = self.font.render('NEW HIGH SCORE!!!', False, 'white')
            new_h_score_rect = new_h_score_surf.get_rect(center=(self.screen_width / 2, (self.screen_height / 2) - 60))
            self.screen.blit(new_h_score_surf, new_h_score_rect)

    def leaderboard(self):
        if self.score_record:
            file = open('records/leaderboard', 'a')
            file.writelines(str(self.score))
            file.close()
            self.score_record = False

    def high_score(self):
        file = open('records/high_score', 'r')
        lines = file.readlines()
        high_score = lines[0]
        file.close()

        if self.score > int(high_score):
            with open('records/high_score', 'w') as f:
                f.write(str(self.score))
                f.close()

        return high_score

    def restart(self):
        self.alien_setup(self.rows, self.cols)

        self.extra_spawn_time = randint(40, 80)

        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start=self.screen_width / 15, y_start=480)

        self.score_record = True

        self.lives = 3
        self.score = 0

    def run(self):
        if self.game_restart:
            self.player.update()
            self.alien_lasers.update()
            self.extra.update()

            self.aliens.update(self.alien_direction)
            self.aline_position_checker()
            self.extra_alien_timer()
            self.collision_checks()

            self.player.sprite.lasers.draw(self.screen)
            self.player.draw(self.screen)
            self.blocks.draw(self.screen)
            self.aliens.draw(self.screen)
            self.alien_lasers.draw(self.screen)
            self.extra.draw(self.screen)

            self.display_lives()
            self.display_score()
            self.victory()
        else:
            self.restart_message()
