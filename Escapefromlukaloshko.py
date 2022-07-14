import random
import pygame
from const import black, white, green, bright_green, display_height, display_width, car_width, clock, gameDisplay, carImg
from func import button, text_objects, things, car, things_dodged, crash
from datetime import datetime

pygame.init()



def get_time_now():
    cur_time = datetime.now().time()
    cur_date = datetime.now().date()
    return f'время: {cur_time} / дата: {cur_date}'


def crash():
    with open('database.txt', 'w+', encoding='utf8') as file:
        file.write(get_time_now())
    message_display('Ti Viebalsya?')


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('EcapeFromLulaloshko.ttf', 115)
        TextSurf, TextRect = text_objects("EscapeFromLukaloshko",largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    # старотовая позиция первой машины
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    # стартовая позиция второй машины
    x1 = (display_width * 0.65)
    y1 = (display_height * 0.8)


    x_change = 0
    x1_change = 0

    gameExit = False
    dodged = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1


    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            # управление
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_a:
                    x1_change = -5
                elif event.key == pygame.K_d:
                    x1_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # смена позиции
        x += x_change
        x1 += x1_change

        # фон
        gameDisplay.fill(white)
        # помехи на дороге
        things(thing_startx, thing_starty)
        thing_starty += thing_speed

        # создаем машину
        car(carImg, x, y)
        car(carImg, x1, y1)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        # логика счетчика
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)


        # логика помех
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        # 60 фпс
        clock.tick(60)


if __name__ == '__main__':
    game_intro()
    game_loop()
    pygame.quit()
    quit()