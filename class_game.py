
from class_payer import Player
from monster import Monster
from comet_event import CometFallEvent
import pygame


#2- create a second class called game
class Game:
    def __init__(self):
        # define when the game starts
        self.is_playing = False
        #add a player in the game
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generate the event
        self.comet_event = CometFallEvent()

        # create a group of monster
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # game restart over
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # add the image of the player to the game
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre  de vie du joueur
        self.player.update_health_bar(screen)

        # update event bar of the game
        self.comet_event.update_bar(screen)

        # projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
            # add all monster
            for monster in self.all_monsters:
                monster.forward()
                monster.update_health_bar(screen)
        # add the image of all projectiles
        self.player.all_projectiles.draw(screen)
        # apply all the monsters
        self.all_monsters.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
            print(self.player.rect.x)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
