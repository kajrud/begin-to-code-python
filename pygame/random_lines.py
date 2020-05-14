import random
import pygame

class DrawDemo:
    @staticmethod
    def do_draw_demo():
        init_result = pygame.init()
        if init_result [1] != 0:
            print ("Błąd instalacji biblioteki pygame")
            return

        width = 800
        height = 600
        size = (width, height)

        def get_random_coordinate():
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            return (x, y)

        def get_random_color():
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            return (red, green, blue)

        surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Przykładowy rysunek")

        gray = (128, 128, 128)

        surface.fill(gray)

        for count in range (100):
            start = get_random_coordinate()
            end = get_random_coordinate()
            color = get_random_color()
            pygame.draw.line(surface, color, start, end)

        for count in range(100):
            pos = get_random_coordinate()
            color = get_random_color()
            radius = random.randint(5, 50)
            pygame.draw.circle(surface, color, pos, radius)

        pygame.display.flip()

DrawDemo.do_draw_demo()