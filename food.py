import random
from config import CELL, RED, WIDTH, HEIGHT

class Food:
    def __init__(self):
        self.respawn()

    def respawn(self):
        max_x = WIDTH // CELL - 1
        max_y = HEIGHT // CELL - 1
        self.pos = (random.randint(0, max_x), random.randint(0, max_y))

    def draw(self, screen):
        import pygame
        x, y = self.pos
        pygame.draw.rect(
            screen, RED, (x * CELL, y * CELL, CELL, CELL)
        )
