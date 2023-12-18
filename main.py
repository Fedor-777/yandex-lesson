from functoins import load_level, generate_level, move
from start import *

level_map = load_level(input("Введите имя файла: "))
# Инициализируем игру
pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()

# Создаем спрайты
tile_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')

# создаем  player
player = generate_level(level_map, tile_group, hero_group, tile_images, player_image)
# открываем стартовый экран который воспроизводит игровой цикл пока не нажмем кнопку
start_screen(screen, clock)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move(player, level_map, "left")
            elif event.key == pygame.K_RIGHT:
                move(player, level_map, "right")
            elif event.key == pygame.K_DOWN:
                move(player, level_map, "down")
            elif event.key == pygame.K_UP:
                move(player, level_map, "up")

    screen.fill(pygame.Color("black"))

    # Отрисовываем игрока
    tile_group.draw(screen)
    hero_group.draw(screen)

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
