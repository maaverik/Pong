from pong_functions import *

pygame.init()

fpsClock = pygame.time.Clock()

paddle1_vel = [0,0]
paddle2_vel = [0,0]


def one_player_loop():	
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

			elif event.type == KEYUP:
				if event.key == K_UP:
					paddle2_vel[1]=0
				elif event.key == K_DOWN:
					paddle2_vel[1]=0
			
			# AI part
			# If ball is moving away from paddle, center bat
		
			if ball_vel[0] < 0:
				if paddle1_pos[1] < int(HEIGHT/2):
					paddle1_vel[1] = 3
				elif paddle1_pos[1] > int(HEIGHT/2):
					paddle1_vel[1] = -3
				
			# if ball moving towards paddle, track its movement.
			
			elif ball_vel[0] > 0:
				if paddle1_pos[1] < ball_pos[1]:
					paddle1_vel[1] = 3
				else :
					paddle1_vel[1] = -3

		pygame.display.update()
		fpsClock.tick(60)						#run at 60 fps
