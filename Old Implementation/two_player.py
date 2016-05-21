from pong_functions import *

pygame.init()

fpsClock = pygame.time.Clock()

paddle1_vel = [0,0]
paddle2_vel = [0,0]


def two_player_loop():
	global paddle1_vel, paddle2_vel	
	while True:										#main game loop
		window.fill(BLACK)							#clear screen before drawing again
		update_and_draw(paddle1_vel, paddle2_vel)

		for event in pygame.event.get():			#event handler

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
		fpsClock.tick(60)						#run at 60 fps
