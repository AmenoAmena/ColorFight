import pygame
import random
from sys import exit

class Fighter:
    def __init__(self, color):
        self.color = color

# Define 24 Fighter classes with unique colors
class RedFighter(Fighter): 
    def __init__(self): super().__init__((255, 0, 0))  
class BlueFighter(Fighter): 
    def __init__(self): super().__init__((0, 0, 255))  
class GreenFighter(Fighter): 
    def __init__(self): super().__init__((0, 255, 0))  
class YellowFighter(Fighter): 
    def __init__(self): super().__init__((255, 255, 0))  
class PurpleFighter(Fighter): 
    def __init__(self): super().__init__((128, 0, 128))  
class CyanFighter(Fighter): 
    def __init__(self): super().__init__((0, 255, 255))  
class OrangeFighter(Fighter): 
    def __init__(self): super().__init__((255, 165, 0))  
class PinkFighter(Fighter): 
    def __init__(self): super().__init__((255, 192, 203))  
class BrownFighter(Fighter): 
    def __init__(self): super().__init__((165, 42, 42))  
class LimeFighter(Fighter): 
    def __init__(self): super().__init__((50, 205, 50))  
class TealFighter(Fighter): 
    def __init__(self): super().__init__((0, 128, 128))  
class IndigoFighter(Fighter): 
    def __init__(self): super().__init__((75, 0, 130))  
class VioletFighter(Fighter): 
    def __init__(self): super().__init__((238, 130, 238))  
class GoldFighter(Fighter): 
    def __init__(self): super().__init__((255, 215, 0))  
class SilverFighter(Fighter): 
    def __init__(self): super().__init__((192, 192, 192))  
class MaroonFighter(Fighter): 
    def __init__(self): super().__init__((128, 0, 0))  
class OliveFighter(Fighter): 
    def __init__(self): super().__init__((128, 128, 0))  
class CoralFighter(Fighter): 
    def __init__(self): super().__init__((255, 127, 80))  
class SalmonFighter(Fighter): 
    def __init__(self): super().__init__((250, 128, 114))  
class KhakiFighter(Fighter): 
    def __init__(self): super().__init__((240, 230, 140))  
class PlumFighter(Fighter): 
    def __init__(self): super().__init__((221, 160, 221))  
class DarkGreenFighter(Fighter): 
    def __init__(self): super().__init__((0, 100, 0))  
class DarkBlueFighter(Fighter): 
    def __init__(self): super().__init__((0, 0, 139))  
class DarkRedFighter(Fighter): 
    def __init__(self): super().__init__((139, 0, 0))  
class DarkGrayFighter(Fighter): 
    def __init__(self): super().__init__((169, 169, 169))  
class LightGrayFighter(Fighter): 
    def __init__(self): super().__init__((211, 211, 211))  

class Tile:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, self.color, (x, y, self.size, self.size))

class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.fps = 60
        self.rows, self.cols = 50, 50  
        self.tile_size = self.width // self.cols  

        self.fighters = [
            RedFighter(), BlueFighter(), GreenFighter(), YellowFighter(), PurpleFighter(), CyanFighter(),
            OrangeFighter(), PinkFighter(), BrownFighter(), LimeFighter(), TealFighter(), IndigoFighter(),
            VioletFighter(), GoldFighter(), SilverFighter(), MaroonFighter(), OliveFighter(), CoralFighter(),
            SalmonFighter(), KhakiFighter(), PlumFighter(), DarkGreenFighter(), DarkBlueFighter(),
            DarkRedFighter(), DarkGrayFighter(), LightGrayFighter()
        ]

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('ColorFight')

        self.clock = pygame.time.Clock()

        self.create_game_field()
        self.game_finished = False

    def create_game_field(self):
        total_elements = self.rows * self.cols
        num_fighters = len(self.fighters)
        elements_per_color = total_elements // num_fighters

        elements = [i + 1 for i in range(num_fighters) for _ in range(elements_per_color)]
        elements += [random.randint(1, num_fighters) for _ in range(total_elements - len(elements))]  

        random.shuffle(elements)

        self.game_field = []
        for i in range(self.rows):
            row = elements[i * self.cols:(i + 1) * self.cols]
            self.game_field.append(row)

    def draw(self):
        self.window.fill((0, 0, 0))  
        for i in range(self.rows):
            for j in range(self.cols):
                color = self.fighters[self.game_field[i][j] - 1].color
                tile = Tile(color, self.tile_size)
                tile.draw(self.window, j * self.tile_size, i * self.tile_size)
        pygame.display.flip()

    def fight(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if i > 0 and self.game_field[i][j] != self.game_field[i-1][j]:
                    winner = random.choice([self.game_field[i][j], self.game_field[i-1][j]])
                    self.game_field[i][j] = winner
                    self.game_field[i-1][j] = winner
                if j > 0 and self.game_field[i][j] != self.game_field[i][j-1]:
                    winner = random.choice([self.game_field[i][j], self.game_field[i][j-1]])
                    self.game_field[i][j] = winner
                    self.game_field[i][j-1] = winner

    def keyboard_handler(self, event):
        if event.key == pygame.K_r:  
            self.finish_game(1)
        elif event.key == pygame.K_b:  
            self.finish_game(2)
        elif event.key == pygame.K_g:  
            self.finish_game(3)
        elif event.key == pygame.K_y:  
            self.finish_game(4)
        elif event.key == pygame.K_p:  
            self.finish_game(5)
        elif event.key == pygame.K_c:  
            self.finish_game(6)
        elif event.key == pygame.K_o:  
            self.finish_game(7)
        elif event.key == pygame.K_n:  
            self.finish_game(8)
        elif event.key == pygame.K_m:  
            self.finish_game(9)
        elif event.key == pygame.K_l:  
            self.finish_game(10)
        elif event.key == pygame.K_t:  
            self.finish_game(11)
        elif event.key == pygame.K_i:  
            self.finish_game(12)
        elif event.key == pygame.K_v:  
            self.finish_game(13)
        elif event.key == pygame.K_s:  
            self.finish_game(14)
        elif event.key == pygame.K_k:  
            self.finish_game(15)
        elif event.key == pygame.K_q:  
            self.finish_game(16)
        elif event.key == pygame.K_h:  
            self.finish_game(17)
        elif event.key == pygame.K_j:  
            self.finish_game(18)
        elif event.key == pygame.K_w:  
            self.finish_game(19)
        elif event.key == pygame.K_z:  
            self.finish_game(20)
        elif event.key == pygame.K_x:  
            self.finish_game(21)
        elif event.key == pygame.K_u:  
            self.finish_game(22)
        elif event.key == pygame.K_a:  
            self.finish_game(23)
        elif event.key == pygame.K_SPACE:
            self.restart()
        elif event.key == pygame.K_ESCAPE:
            exit()

    def finish_game(self, color_index):
        self.game_finished = True
        for i in range(self.rows):
            for j in range(self.cols):
                self.game_field[i][j] = color_index

    def restart(self):
        self.create_game_field()
        self.game_finished = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.keyboard_handler(event)

            if not self.game_finished:
                self.fight() 
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

