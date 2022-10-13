#!/usr/bin/python3

import pygame
import sys
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,480))

FPS = 60
bx=0
by=0
bsx=2.5
bsy=-3.5
ctable = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255)]
font = pygame.font.SysFont(None,80)
text = font.render('DVD',True,(255,0,0))
w = text.get_width()
h = text.get_height()


def drawBox():
	screen.blit(text,(bx,by))

def moveCalc():
	global bx
	global by
	global bsx
	global bsy
	global text
	global ctable

	if by + bsy < 0 or by + bsy + h > 480:
		bsy*=-1
		text = font.render('DVD',True,ctable[random.randrange(len(ctable))])
	if bx + bsx < 0 or bx + bsx + w > 640:
		bsx*=-1
		text = font.render('DVD',True,ctable[random.randrange(len(ctable))])

	bx+=bsx
	by+=bsy

def main():
	clock = pygame.time.Clock()
	
	while True:
		screen.fill((0,0,0))
		drawBox()
		moveCalc()
		pygame.display.flip()
		clock.tick(FPS)
		for i in pygame.event.get():
			if i.type == QUIT:
				pygame.quit()
				sys.exit()

if __name__ == '__main__':
	main()
