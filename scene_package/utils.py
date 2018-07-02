import pygame


def log(*args, **kw):
    print(*args, **kw)

def rectIntersects(a, b):
    if b.y > a.y and b.y < a.y + a.imageHeight:
        if b.x > a.x and b.x < a.x + a.imageWidth:
            return True
    return False


# 使图片只载入一次
def images():
    d = {
         'bullet': 'image/bullet1.png',
         'background': 'image/background2.png',
         'player': 'image/player.png',
         'cloud': 'image/cloud.jpg',
         'enemy2': 'image/enemy2.png',
         'enemy1': 'image/enemy1.png',
    }
    return d

def loadimages():
    image_dict = images()
    d = {}
    for k, v in image_dict.items():
        path = image_dict[k]
        img = pygame.image.load(path).convert_alpha()
        d[k] = img
    return d

def texture_by_name(imageName):
    # 这个可以考虑放进guagame.py
    images = loadimages()
    img = images[imageName]
    return img