import pygame, time
import sys
from pygame.sprite import Sprite
pygame.init()
window = pygame.display.set_mode((800,500))

myfont = pygame.font.SysFont("TIMES NEW ROMAN",40)
label = myfont.render("PRESS ENTER TO CONTINUE TO GAME", 1, (180,150,100))
window.fill((255,255,255))
window.blit(label, (60,100))
pygame.display.update()
pygame.display.set_caption("Programmer World")
#time.sleep(5)

image = pygame.image.load('images/alien.bmp')
print(image)
rect = image.get_rect()
print(rect)
rect.x = rect.width
rect.y = rect.height
print(rect.x)
print(rect.y)
print(float(rect.y))
print(rect.right)
print(rect.left)
window.blit(image, rect)
window_rect = window.get_rect()
print(window_rect)
print(window_rect.width)
print(window_rect.height)
print(window_rect.right)
print(window_rect.left)
time.sleep(5)
"""
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                label2 = myfont.render("Hello world!", 1, (255, 0, 0))
                window.blit(label2, (200, 200))
            elif event.key==pygame.K_KP_ENTER:
                label2 = myfont.render(" ", 1, (255, 0, 0))
                window.blit(label2, (200, 200))
    pygame.display.flip()
"""
pygame.quit()
