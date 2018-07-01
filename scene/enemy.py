from scene.gua_image import GuaImage
import random


class Enemy(GuaImage):
    def __init__(self):
        self.type = random.randint(1, 2)
        self.name = 'enemy' + str(self.type)
        super().__init__(self.name)
        self.speed = random.randint(2, 5)

    def update(self):
        self.y += self.speed
        if self.y > 600:
            self.x = random.randint(0, 350)
            self.y = -random.randint(0, 200)
        super().update()
