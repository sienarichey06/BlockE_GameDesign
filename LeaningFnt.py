import pygame
pygame.init()
wind=pygame.display.set_mode((700,700))
pygame.display.set_caption("testing")
#create different type

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 25)
text=TITLE_FNT.render('Circle eats square', 1, (255, 0, 0))
wind.fill((255, 255, 255))
wind.blit(text, (50,50))
text=INST_FNT.render("2 player game. Circle uses keys up, down, side. Square uses w, a, s, d", 1, (0, 0, 255))
wind.blit(text, (300, 300))
pygame.display.update()

pygame.time.delay(10000)