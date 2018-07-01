import pygame
from scene.guagame_test import Guagame
from scene_package.utils import texture_by_name


class GuaImage:
    def __init__(self, name):
        self.game = Guagame()
        self.texture = texture_by_name(name)
        self.x = 0
        self.y = 0
        self.w = self.texture.get_width()
        self.h = self.texture.get_height()

    def draw(self):
        self.game.clear()

    def draw_tips(self):
        pass

    def update(self):
        pygame.display.update()