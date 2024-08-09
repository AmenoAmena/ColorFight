import pygame

class Fighter:
    def __init__(self, color):
        self.color = color

class RedFighter(Fighter):
    def __init__(self):
        super().__init__((255, 0, 0))  

class BlueFighter(Fighter):
    def __init__(self):
        super().__init__((0, 0, 255))  

class Tile:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.width = 4
        self.height = 3

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, self.color, (x, y, self.size, self.size))

class ColorFight:
    def __init__(self):
        self.pygame.init()
        self.width = 800
        self.height = 600
        self.fps = 60

        self.window = pygame.display.set_mode((self.width, self.height))
        self.pygame.display.set_caption('ColorFight')

        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)

        self.clock = pygame.time.Clock()


    def draw(self):
        pass

    def update(self):
        pass

    def run(self):
        pass

    