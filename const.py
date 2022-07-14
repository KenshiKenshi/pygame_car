from pygame import time, image, transform, display

# цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# разрешение
display_width = 800
display_height = 600

# настройки машины
crashed = False
car_width = 73
car_speed = 0

# модуль для времени, чтобы мониторить кадры в секунду
clock = time.Clock()

carImg = image.load('image/mashinka.jpg')  # картинка для игрока
carImg = transform.scale(carImg, (70, 80))  # задаем размер картинки
enemyImg = image.load('image/bobik.jpg') # враги по встречке
enemyImg = transform.scale(enemyImg, (70, 80))

gameDisplay = display.set_mode((display_width, display_height))
display.set_caption("Dai Darogy")  # название игры