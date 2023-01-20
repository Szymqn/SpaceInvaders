import pygame
import sys
from game import Game
from start import Start
from crt import CRT


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    screen_setting = [screen, screen_height, screen_height]
    start = Start(*screen_setting)
    game = Game(*screen_setting)
    crt = CRT(*screen_setting)

    ALIENLASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENLASER, 800)

    def test_placeholder():
        pass

    def to_menu():
        start.status = True
        game.status = True
        game.game_restart = True
        game.restart()

    def quit_game():
        pygame.quit()
        sys.exit()

    while True:
        screen.fill((30, 30, 30))
        crt.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == ALIENLASER and start.status is False:
                game.alien_shoot()

        if game.quit:
            quit_game()

        if start.status:  # active start surface
            start.draw()
            if start.quit:
                quit_game()
        elif not game.status:  # deactivate game surface
            to_menu()
        else:  # active game surface
            game.run()

        pygame.display.flip()
        clock.tick(60)
