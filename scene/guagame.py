import pygame


# class Guagame():
#     pygame.init()
#     pygame.display.set_caption("打砖块")
#
#     def __init__(self):
#         self.screen = pygame.display.set_mode((400,300))
#
#     def clear(self):
#         self.screen.fill((255, 255, 255))
#
#     def draw_image(self, image):
#         self.screen.blit(image.texture, (image.x, image.y))
#
#     def drawScore(self, score):
#         score = 'score: ' + str(score)
#         self.drawTips(score, 300, 260)
#
#     def drawTips(self, text, x, y):
#         # 创建字体对象
#         font = pygame.font.Font(None, 20)
#         # 文本与颜色
#         text = font.render(text, 50, (0, 0, 0))
#         self.screen.blit(text, (x ,y))