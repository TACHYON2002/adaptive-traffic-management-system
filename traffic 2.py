import pyfirmata
import time
import pygame
from threading import Thread

COLOURS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "reset": "\u001b[0m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}


def colortext(text):
    for colour in COLOURS:
        text = text.replace("[[" + colour + "]]", COLOURS[colour])
    return text


def ledgreenhorizontal(b):
    if b == 1:
        print(colortext('[[green]]horizontalgreenon[[reset]]'))
    else:
        print('horizontalgreenoff')


def ledyellowhorizontal(b):
    if b == 1:
        print(colortext('[[yellow]]horizontalyellowon[[reset]]'))
    else:
        print('horizontalyellowoff')


def ledredhorizontal(b):
    if b == 1:
        print(colortext('[[red]]horizontalredon[[reset]]'))
    else:
        print('horizontalredoff')


def ledgreenvertical(b):
    if b == 1:
        print(colortext('[[green]]verticalgreenon[[reset]]'))
    else:
        print('verticalgreenoff')


def ledyellowvertical(b):
    if b == 1:
        print(colortext('[[yellow]]verticalyellownon[[reset]]'))
    else:
        print('verticalyellowoff')


def ledredvertical(b):
    if b == 1:
        pygame.init()
        white = (255, 255, 255)
        displayout = pygame.display.set_mode((1000, 700))
        img = pygame.image.load(r'D:\HACKATHON\traffic light\red.png')
        displayout.fill(white)
        displayout.blit(img, (60, 100))
        pygame.display.update()
    else:
        print('verticalredoff')


def ldrhorizontal1():
    a = int(input('ldrhorizontal1'))
    return a


def ldrhorizontal2():
    a = int(input('ldrhorizontal2'))
    return a


def ldrhorizontal3():
    a = int(input('ldrhorizontal3'))
    return a


def ldrhorizontal4():
    a = 1
    return a


def ldrvertical1():
    a = int(input('ldrvertical1'))
    return a


def ldrvertical2():
    a = int(input('ldrvertical2'))
    return a


def ldrvertical3():
    a = int(input('ldrvertical3'))
    return a


def ldrvertical4():
    a = 1
    return a


def main():
    b = 1
    while b == 1:

        a = input('TO START ENTER 1    TO END ENTER 0\n')

        if a == '1':

            while True:
                traffic()

        elif a == '0':

            print('PROGRAM ENDED')
            b = 2

        else:

            print('TRY AGAIN')


def traffic():
    ledredvertical(1)
    ledredhorizontal(1)

    ldrhorizontal1in = ldrhorizontal1()
    ldrhorizontal2in = ldrhorizontal2()
    ldrhorizontal3in = ldrhorizontal3()
    ldrvertical1in = ldrvertical1()
    ldrvertical2in = ldrvertical2()
    ldrvertical3in = ldrvertical3()

    if ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in == ldrvertical1in + ldrvertical2in + ldrvertical3in:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(7)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(7)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)


    elif ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in == 0 and ldrvertical1in + ldrvertical2in + ldrvertical3in != 0:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(7)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredhorizontal(0)

    elif ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in != 0 and ldrvertical1in + ldrvertical2in + ldrvertical3in == 0:

        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(7)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)

    elif ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in == 1 and ldrvertical1in + ldrvertical2in + ldrvertical3in == 2:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(7)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(4)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)

    elif ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in == 1 and ldrvertical1in + ldrvertical2in + ldrvertical3in == 3:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(10)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(4)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)

    elif ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in == 2 and ldrvertical1in + ldrvertical2in + ldrvertical3in == 3:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(10)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(6)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)

    elif ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in == 2 and ldrvertical1in + ldrvertical2in + ldrvertical3in == 1:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(4)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(7)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)

    elif ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in == 3 and ldrvertical1in + ldrvertical2in + ldrvertical3in == 1:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(4)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(10)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)

    elif ldrhorizontal1in + ldrhorizontal2in + ldrhorizontal3in == 3 and ldrvertical1in + ldrvertical2in + ldrvertical3in == 2:

        ledredvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledgreenvertical(1)
        time.sleep(6)
        ledgreenvertical(0)
        ledyellowvertical(1)
        time.sleep(2)
        ledyellowvertical(0)
        ledredvertical(1)
        ledredhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledgreenhorizontal(1)
        time.sleep(10)
        ledgreenhorizontal(0)
        ledyellowhorizontal(1)
        time.sleep(2)
        ledyellowhorizontal(0)
        ledredvertical(0)




main()