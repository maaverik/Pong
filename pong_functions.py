import pygame, sys, random
from pygame.locals import *

# define constants

BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
RED 		= (205, 92, 92)
WIDTH       = 700
HEIGHT      = 500
BALL_RADIUS = 10
PAD_WIDTH   = 8
PAD_HEIGHT  = 80

paddle2_pos = [int(PAD_WIDTH/2),int(HEIGHT/2)]				# centre of paddles; in [x,y] format
paddle1_pos = [int(WIDTH-PAD_WIDTH/2),int(HEIGHT/2)]
ball_pos    = [int(WIDTH/2),int(HEIGHT/2)]					# centre of ball
ball_vel    = [0,0]
score1      = 0
score2      = 0

# create window

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong")

# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):						# sets ball velocity upwards right or left
    global ball_pos, ball_vel 
    ball_pos = [int(WIDTH/2),int(HEIGHT/2)]
    ball_vel = [0,0]
    if direction == "Right":
    	ball_vel = [random.randint(2,4),-random.randint(1,3)]
    elif direction == "Left":
        ball_vel = [-random.randint(2,4),-random.randint(1,3)]


def new_game():
    global score1, score2 
    score1=score2=0
    paddle1_pos = [int(WIDTH-PAD_WIDTH/2),int(HEIGHT/2)]		
    paddle2_pos = [int(PAD_WIDTH/2),int(HEIGHT/2)]
    spawn_ball("Left")


def get_velx():									# to access it in different file
	return ball_vel[0]


def get_posy():									# to access it in different file
	return ball_pos[1]


def get_pad_posy():								# to access it in different file
	return paddle1_pos[1]


def update_and_draw(paddle1_vel, paddle2_vel):			# handles logic and drawing
	# Use the global variables
	global paddle1_pos, paddle2_pos, score1, score2, ball_vel, ball_pos  

	#Draw central line and borders
	
	pygame.draw.line(window, WHITE, (int(WIDTH/2), 0), (int(WIDTH/2), HEIGHT), 2)
	pygame.draw.line(window, WHITE, (PAD_WIDTH, 0), (PAD_WIDTH, HEIGHT), 2)
	pygame.draw.line(window, WHITE, (WIDTH - PAD_WIDTH, 0), (WIDTH - PAD_WIDTH, HEIGHT), 2)

	#Update ball position depending on its current position and velocity

	if ball_pos[1]<=BALL_RADIUS or ball_pos[1]>=HEIGHT-BALL_RADIUS:			# If the ball hits walls
   	    ball_vel[1]=-ball_vel[1]
	ball_pos[0] +=ball_vel[0]
	ball_pos[1] +=ball_vel[1]

	#Draw the ball after updating position
	
	pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS)

	# Update paddle positions as long as they are not at the boundary

	if paddle1_pos[1]+paddle1_vel[1]>int(PAD_HEIGHT/2) and paddle1_pos[1]+paddle1_vel[1]<int(HEIGHT-PAD_HEIGHT/2):
		paddle1_pos[1]=paddle1_pos[1]+paddle1_vel[1]

	if paddle2_pos[1]+paddle2_vel[1]>int(PAD_HEIGHT/2) and paddle2_pos[1]+paddle2_vel[1]<int(HEIGHT-PAD_HEIGHT/2):
		paddle2_pos[1]=paddle2_pos[1]+paddle2_vel[1]

	# Draw paddles after updating positions
	
	pygame.draw.line(window, WHITE, (PAD_WIDTH,paddle1_pos[1]-50), (PAD_WIDTH,paddle1_pos[1]+50), PAD_WIDTH)
	pygame.draw.line(window, WHITE, (WIDTH - PAD_WIDTH,paddle2_pos[1]-50), (WIDTH - PAD_WIDTH,paddle2_pos[1]+50), PAD_WIDTH)

	# check if the ball hit a paddle; if it did, reverse its velocity; if not, score accordingly

	if ball_pos[0]<=PAD_WIDTH*2+BALL_RADIUS or ball_pos[0]>=WIDTH-PAD_WIDTH*2-BALL_RADIUS:

		if (ball_pos[1] in range(paddle1_pos[1]-50,paddle1_pos[1]+51) and ball_pos[0]<int(WIDTH/2) ) or (ball_pos[1] in range(paddle2_pos[1]-50,paddle2_pos[1]+51) and ball_pos[0]>int(WIDTH/2)):
			if ball_vel[0]<0:
				ball_vel[0] =-(ball_vel[0]-1)
			else:
				ball_vel[0] =-(ball_vel[0]+1)
		else:
			if ball_pos[0]>int(WIDTH/2):		#check which player geys a point depending on which side the ball is in
				score1 +=1
				spawn_ball("Left")
			else:
				score2 +=1
				spawn_ball("Right")

	# draw scores

	font          = pygame.font.SysFont(None, 32)
	msg1          = font.render(str(score1), True, WHITE)
	msg2          = font.render(str(score2), True, WHITE)
	
	msg1Rect      = msg1.get_rect()
	msg2Rect      = msg2.get_rect()
	msg1Rect.left = int(WIDTH/4)
	msg2Rect.left = int(WIDTH/4 * 3)
	msg1Rect.top  = int(HEIGHT/4)
	msg2Rect.top  = int(HEIGHT/4)

	window.blit(msg1, msg1Rect)
	window.blit(msg2, msg2Rect)
