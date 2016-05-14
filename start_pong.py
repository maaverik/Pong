#!/usr/bin/python3

import pygame, sys, random
from pygame.locals import *
from pong_functions import *

pygame.init()

fpsClock = pygame.time.Clock()

paddle1_vel = [0,0]
paddle2_vel = [0,0]

new_game()

while True:										#main game loop
	window.fill(WHITE)						#clear screen before drawing again
	draw(paddle1_vel, paddle2_vel)

	for event in pygame.event.get():		#event handler
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == KEYDOWN:
			if event.key == K_UP:
				paddle2_vel[1]=-3
			elif event.key == K_DOWN:
				paddle2_vel[1]=3
			elif event.key == K_w:
				paddle1_vel[1]=-3
			elif event.key == K_s:
				paddle1_vel[1]=3	

		elif event.type == KEYUP:
			if event.key == K_UP:
				paddle2_vel[1]=0
			elif event.key == K_DOWN:
				paddle2_vel[1]=0
			elif event.key == K_w:
				paddle1_vel[1]=0
			elif event.key == K_s:
				paddle1_vel[1]=0	

	pygame.display.update()
	fpsClock.tick(60)						#run at 50 fps
