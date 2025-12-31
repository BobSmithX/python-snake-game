import pygame
from config import *
from snake import Snake
from food import Food

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

snake = Snake()
food = Food()
score = 0
game_over = False

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_dir((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_dir((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_dir((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_dir((1, 0))
            elif event.key == pygame.K_r and game_over:
                snake = Snake()
                food = Food()
                score = 0
                game_over = False

    if not game_over:
        snake.move()
        # 撞墙
        hx, hy = snake.body[0]
        if hx < 0 or hy < 0 or hx * CELL >= WIDTH or hy * CELL >= HEIGHT:
            game_over = True
        # 吃食物
        if snake.body[0] == food.pos:
            snake.eat()
            food.respawn()
            score += 1
        # 撞自己
        if snake.hit_self():
            game_over = True

    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    draw_text(f"Score: {score}", 10, 10)
    if game_over:
        draw_text("Game Over - Press R to Restart", 160, 190)
    pygame.display.flip()

pygame.quit()
