import pygame as py
import random as rand
import time

py.init()

display_width = 800
display_height = 600

sky = (184, 228, 234)

gameDisplay = py.display.set_mode((display_width, display_height))

py.display.set_caption('A test boat')

clock = py.time.Clock()

#image for seagull
seagullImg = py.image.load('seagull.png')


class Seagull:
    width = 61
    height = 47
    image = seagullImg
    speed = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Displaying seagull
    def show(self):
        gameDisplay.blit(self.image, (self.x, self.y))

    # Should make seagull move 5 pixel each loop?!
    def move(self):
        self.y += self.speed


def game_loop():
    gameexit = False

    while not gameexit:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

        gameDisplay.fill(sky)
        #Set seagull1 at coordinates 400 and 0
        seagull1 = Seagull(400, 0)
        #Displays seagull1
        seagull1.show()
        #This doesn't work properly!!!
        seagull1.move()

        print(seagull1.y)
        py.display.update()
        clock.tick(60)


game_loop()
py.quit()
quit()
