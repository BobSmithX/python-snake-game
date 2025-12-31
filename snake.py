from config import CELL, GREEN

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.dir = (1, 0)  # 右
        self.grow = False

    def change_dir(self, d):
        # 防止反向
        if (d[0] == -self.dir[0] and d[1] == -self.dir[1]):
            return
        self.dir = d

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.dir
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        self.grow = False

    def eat(self):
        self.grow = True

    def hit_self(self):
        return self.body[0] in self.body[1:]

    def draw(self, screen):
        import pygame
        for x, y in self.body:
            pygame.draw.rect(
                screen, GREEN, (x * CELL, y * CELL, CELL, CELL)
            )
