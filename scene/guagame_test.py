import pygame
from pygame.locals import *
from scene_package.slider import timer


class Guagame():
    pygame.init()
    pygame.display.set_caption("打砖块")

    def __init__(self):
        self.screen = pygame.display.set_mode((400,600))
        self.scene = None
        self.x_scroll = 55

    def clear(self):
        self.screen.fill((255, 255, 255))

    def draw_image(self, image):
        self.screen.blit(image.texture, (image.x, image.y))

    def draw(self):
        self.scene.draw()

    def update(self):
        self.scene.update()

    def replace_scene(self, scene):
        self.scene = scene

    def action(self):
        # 调用注册的函数
        for k in self.scene.keydowns:
            if self.scene.keydowns[k]:
                if k in self.scene.actions:
                    self.scene.actions[k]()

    def timer(self):
        self.x_scroll = timer(self.screen, self.x_scroll)
        pygame.display.update()

    def begin(self):
        while True:
            self.scene.get_event()
            self.action()
            self.draw()
            # self.timer()
            self.update()

