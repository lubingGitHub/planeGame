import pygame
from sys import exit
from scene.scene_basic import SceneBasic
from scene.gua_image import GuaImage
from scene.player import Player
from scene.enemy import Enemy
from scene.cloud import Cloud
from scene.bullet import Bullet


class Scene(SceneBasic):
    def __init__(self):
        super().__init__()
        self.bg = GuaImage('background')
        self.player = Player()
        self.cloud = Cloud()
        self.bullet = Bullet()
        self.player.x = 100
        self.player.y = 150
        self.number_of_enemies = 10
        self.actions = {
            pygame.K_d: self.player.move_right,
            pygame.K_a: self.player.move_left,
            pygame.K_w: self.player.move_up,
            pygame.K_s: self.player.move_down,
            pygame.K_j: self.player.fire,
            pygame.K_ESCAPE: exit,
        }

        self.elements = []
        self.add_elements(self.bg)
        self.add_elements(self.player)
        self.add_elements(self.cloud)
        self.add_enemies()


    # def draw(self):
    #     self.game.draw_image(self.bg)
    #     self.game.draw_image(self.player)

    def update(self):
        # self.cloud.y += 1
        super().update()
        # self.player.fire()

    def add_enemies(self):
        es = []
        for i in range(self.number_of_enemies):
            e = Enemy()
            es.append(e)
            self.add_elements(e)
        self.enemies = es

