from scene.scene import Scene
from scene.guagame_test import Guagame



def run():
    gua_game = Guagame()
    scene = Scene()
    gua_game.replace_scene(scene)
    gua_game.begin()


if __name__ == '__main__':
    run()