import pygame
import math
pygame.init()
from class_game import Game

# create a window
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))
# add the background
background = pygame.image.load('assets/bg.jpg')

# import the welcoming page
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

# upload the botton
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/2)




# create a game variable
game = Game()


running = True
# window will be executed as long as the variable is true
while running:
    # add the window game
    screen.blit(background, (0, -200))

    # verify if the player is playing or not
    if game.is_playing:
        # star`ts instructions of the game
        game.update(screen)
    # verify if game is not playing
    else:
        # add the welcoming screen
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # update the screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("end the game")
            # know if the player press on the key board
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # find out if the space key has being pressed to launch the  projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # making sure that the mouse is in collision withe play button
            if play_button_rect.collidepoint(event.pos):
                # game is activate
                game.start()
































