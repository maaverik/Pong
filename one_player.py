from pong_functions import *

pygame.init()

fpsClock = pygame.time.Clock()

paddle1_vel = [0,0]
paddle2_vel = [0,0]

DIFF = 2 				# positive integer representing difficulty level

def one_player_loop():	
	global paddle2_vel, paddle1_vel
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
			
		# primitive AI replica : 
		# If ball is moving away from paddle, center bat
			

		if get_velx() > 0:
			if get_pad_posy() < int(HEIGHT/2):
				paddle1_vel[1] = DIFF
			elif get_pad_posy() > int(HEIGHT/2):
				paddle1_vel[1] = -DIFF
			
		# if ball moving towards paddle, track its movement.
		
		elif get_velx() < 0:
			if get_pad_posy() < get_posy():
				paddle1_vel[1] = DIFF
			else :
				paddle1_vel[1] = -DIFF

		pygame.display.update()
		fpsClock.tick(60)						#run at 60 fps
