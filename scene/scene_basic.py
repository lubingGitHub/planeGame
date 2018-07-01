import pygame
from pygame.locals import *
from sys import exit
from scene.guagame_test import Guagame


class SceneBasic:
    def __init__(self):
        self.is_transited = False
        self.game = Guagame()
        self.keydowns = {}
        self.actions = {
            pygame.K_ESCAPE: exit,
        }
        self.elements = []

    def get_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self.keydowns[event.key] = True
            elif event.type == KEYUP:
                self.keydowns[event.key] = False

    def action(self):
        # 调用的注册的函数
        for k in self.keydowns:
            if self.keydowns[k]:
                if k in self.actions:
                    self.actions[k]()

    def transited(self):
        self.is_transited = True

    def draw(self):
        self.game.clear()
        for i in self.elements:
            self.game.draw_image(i)

    def draw_tips(self):
        pass

    def update(self):
        pygame.display.update()
        for i in self.elements:
            i.update()

    def add_elements(self, img):
        img.scene = self
        self.elements.append(img)

    def begin(self):
        while self.is_transited is False:
            self.get_event()
            self.action()
            self.draw()
            self.draw_tips()
            self.update()
