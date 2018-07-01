from scene.gua_image import GuaImage
import random
import pygame
from pygame.locals import *


class Cloud(GuaImage):
    def __init__(self, name='cloud'):
        super().__init__(name)
        self.speed = 1

    def update(self):
        self.y += self.speed
        if self.y > 600:
            self.x = random.randint(0, 350)
            self.y = -random.randint(0, 200)
        super().update()
