import pygame
from pygame.locals import *
from sys import exit
from scene.guagame_test import Guagame
from scene.gua_image import GuaImage
from scene.bullet import Bullet
from scene_package.utils import texture_by_name


class Player(GuaImage):
    def __init__(self, name='player'):
        super().__init__(name)
        self.speed = 1
        self.cool_down = 0

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def update(self):
        if self.cool_down > 0:
            self.cool_down -= 1
        super().update()

    def fire(self):
        if self.cool_down == 0:
            self.cool_down = 50
            x = self.x + self.w / 2
            y = self.y
            print(x, y)
            # 初始化时按另外键会没有反应
            b = Bullet()
            b.x = x
            b.y = y
            self.scene.add_elements(b)
