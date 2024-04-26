import pygame

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Размеры
SQUARE_SIZE = 50
BOARD_SIZE = 8 * SQUARE_SIZE

# Шрифты
FONT = pygame.font.SysFont(None, 30)


# Загрузка изображений фигур
piece_images = {
    'p': pygame.image.load('img\\p.png'),
    'r': pygame.image.load('img\\r.png'),
    'n': pygame.image.load('img\\n.png'),
    'b': pygame.image.load('img\\b.png'),
    'q': pygame.image.load('img\\q.png'),
    'k': pygame.image.load('img\\k.png'),
    'P': pygame.image.load('img\\Pb.png'),
    'R': pygame.image.load('img\\Rb.png'),
    'N': pygame.image.load('img\\Nb.png'),
    'B': pygame.image.load('img\\Bb.png'),
    'Q': pygame.image.load('img\\Qb.png'),
    'K': pygame.image.load('img\\Kb.png'),
}

screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
# Функция для отрисовки клетки
def draw_square(screen, x, y, color):
    rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(screen, color, rect)

# Функция для отрисовки фигуры
def draw_piece(screen, piece, x, y):
    image = piece_images[piece]
    rect = image.get_rect(topleft=(x * SQUARE_SIZE, y * SQUARE_SIZE))
    screen.blit(image, rect)

# Функция для отрисовки доски
def draw_board(screen, positions):
    for y in range(8):
        for x in range(8):
            color = WHITE if (x + y) % 2 == 0 else GREEN
            draw_square(screen, x, y, color)
            piece = positions[y][x]
            if piece:
                draw_piece(screen, piece, x, y)

# Функция для обработки событий
def handle_events():
    print("Здесь реализовываем обработку событий")



# Основной цикл игры
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            MOUSE_CLICKED_POSITION = pygame.mouse.get_pos()
           # Обработка нажатий мыши




    pygame.display.set_caption('Шахматы')
    #pygame.time.Clock().tick(30)
    # Стартовая позиция
    positions = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ]

    # Отрисовка доски и фигур
    draw_board(screen, positions)


    # Обновление экрана
    pygame.display.flip()



# Завершение Pygame
pygame.quit()