import pygame
#
#
# def slider_button(screen, active_colour, x_scroll, y):
#     cur = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     pygame.draw.line(screen, active_colour, (10, y), (110, y))
#     if 110 > cur[0] > 10 and y+16 > cur[1] > y-10:
#         if click[0] == 1:
#             x_scroll = cur[0]
#     return x_scroll
#
# def timer(screen, button_scroll, y):
#     x_scroll1 = slider_button(screen, (190, 190, 190), button_scroll, y)
#     button_scroll = x_scroll1
#     pygame.draw.rect(screen, ((190, 190, 190)), [x_scroll1 - 5, y-10, 10, 24])
#     return button_scroll

class Slider():
    def __init__(self, y):
        self.height = y

    def slider_button(self, screen, active_colour, x_scroll, y):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.line(screen, active_colour, (10, y), (110, y))
        if 110 > cur[0] > 10 and y + 16 > cur[1] > y - 10:
            if click[0] == 1:
                x_scroll = cur[0]
        return x_scroll

    def timer(self, screen, button_scroll, y):
        x_scroll1 = self.slider_button(screen, (190, 190, 190), button_scroll, y)
        button_scroll = x_scroll1
        pygame.draw.rect(screen, ((190, 190, 190)), [x_scroll1 - 5, y - 10, 10, 24])
        return button_scroll
