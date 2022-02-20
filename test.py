import pygame
import time

def asf(b,delay):
    if b == 1:

        white = (255, 255, 255)
        displayout = pygame.display.set_mode((1000, 700))
        img = pygame.image.load(r'D:\HACKATHON\traffic light\red.png')
        displayout.fill(white)
        displayout.blit(img, (60, 100))
        pygame.display.update()
        time.sleep(delay)
        pygame.quit()

    else:
        print('d')
asf(1,1)