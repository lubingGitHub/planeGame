import pygame
from pygame.locals import *
from sys import exit
from scene.guagame_test import Guagame
from scene.gua_image import GuaImage


class Bullet(GuaImage):
    def __init__(self, name='bullet'):
        super().__init__(name)
        self.speed = 1

    def update(self):
        self.y -= self.speed

