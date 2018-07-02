import pygame
from pygame.locals import *
from sys import exit
from scene.guagame_test import Guagame
from scene.gua_image import GuaImage
from scene.bullet import Bullet
from scene_package.utils import texture_by_name
from config import config
from scene_package.slider import timer


class Player(GuaImage):
    def __init__(self, name='player'):
        super().__init__(name)
        # self.speed = 10
        self.cool_down = 0
        self.x_scroll = 55

    def move_left(self):
        self.move_x(self.x - self.speed)

    def move_right(self):
        self.move_x(self.x + self.speed)

    def move_up(self):
        self.move_y(self.y - self.speed)

    def move_down(self):
        self.move_y(self.y + self.speed)

    def move_x(self, x):
        if x < 0:
            x = 0
        if x > 400 - self.w:
            x = 400 - self.w
        self.x = x

    def move_y(self, y):
        if y < 0:
            y = 0
        if y > 600 - self.h:
            y = 600 - self.h
        self.y = y

    def update(self):
        self.speed = config['player_speed']
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


