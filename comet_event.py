import pygame
# create a class


class CometFallEvent:
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5

    def add_percent(self):
        self.percent += self.percent_speed/100

    def update_bar(self, surface):
        # update percentage
        self.add_percent()

        # black bar (in the background)
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # l'axe des x
            surface.get_height() - 20, # l'axe des y
            (surface.get_widht()/100) * self.percent,  # longueur de la fenetre
            10,  # epaisseur de la barre
        ])

        # red bar
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() -20,  # l'axe des y
            (surface.get_widht() / 100) * self.percent,  # longueur de la fenetre
            10,  # epaisseur de la barre

        ])
