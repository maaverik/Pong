import pygame, sys, random
from pygame.locals import *


BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
RED 		= (205, 92, 92)
WIDTH       = 600
HEIGHT      = 400
BALL_RADIUS = 10
PAD_WIDTH   = 8
PAD_HEIGHT  = 80
LEFT        = False
RIGHT       = True
paddle2_pos = [int(PAD_WIDTH/2),int(HEIGHT/2)]
paddle1_pos = [int(WIDTH-PAD_WIDTH/2),int(HEIGHT/2)]

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong")

# initialize ball_pos and ball_vel for new ball in middle of table

ball_pos = [int(WIDTH/2),int(HEIGHT/2)]
ball_vel = [0,0]
score1   = 0
score2   = 0

# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [int(WIDTH/2),int(HEIGHT/2)]
    ball_vel = [0,0]
    if direction == "Right":
        ball_vel = [random.randint(2,4),-random.randint(1,3)]
    elif direction == "Left":
        ball_vel = [-random.randint(2,4),-random.randint(1,3)]

# define event handlers

def new_game():
    global paddle1_vel, paddle2_vel  
    global score1, score2 
    score1=score2=0
    paddle1_pos = [int(WIDTH-PAD_WIDTH/2),int(HEIGHT/2)]
    paddle2_pos = [int(PAD_WIDTH/2),int(HEIGHT/2)]
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    spawn_ball("Left")

def draw(paddle1_vel, paddle2_vel):
	global paddle1_pos, paddle2_pos  
	global score1, score2  

	pygame.draw.line(window, WHITE, (int(WIDTH/2), 0), (int(WIDTH/2), HEIGHT), 2)
	pygame.draw.line(window, WHITE, (PAD_WIDTH, 0), (PAD_WIDTH, HEIGHT), 2)
	pygame.draw.line(window, WHITE, (WIDTH - PAD_WIDTH, 0), (WIDTH - PAD_WIDTH, HEIGHT), 2)

	if ball_pos[1]<=BALL_RADIUS or ball_pos[1]>=HEIGHT-BALL_RADIUS:
   	    ball_vel[1]=-ball_vel[1]
	ball_pos[0] +=ball_vel[0]
	ball_pos[1] +=ball_vel[1]

	pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS)

	if paddle1_pos[1]+paddle1_vel[1]>int(PAD_HEIGHT/2) and paddle1_pos[1]+paddle1_vel[1]<int(HEIGHT-PAD_HEIGHT/2):
		paddle1_pos[1]=paddle1_pos[1]+paddle1_vel[1]

	if paddle2_pos[1]+paddle2_vel[1]>int(PAD_HEIGHT/2) and paddle2_pos[1]+paddle2_vel[1]<int(HEIGHT-PAD_HEIGHT/2):
		paddle2_pos[1]=paddle2_pos[1]+paddle2_vel[1]
	
	pygame.draw.line(window, WHITE, (PAD_WIDTH,paddle1_pos[1]-50), (PAD_WIDTH,paddle1_pos[1]+50), PAD_WIDTH)
	pygame.draw.line(window, WHITE, (WIDTH - PAD_WIDTH,paddle2_pos[1]-50), (WIDTH - PAD_WIDTH,paddle2_pos[1]+50), PAD_WIDTH)

	if ball_pos[0]<=PAD_WIDTH*2+BALL_RADIUS or ball_pos[0]>=WIDTH-PAD_WIDTH*2-BALL_RADIUS:

		if (ball_pos[1] in range(paddle1_pos[1]-50,paddle1_pos[1]+51) and ball_pos[0]<int(WIDTH/2) )or (ball_pos[1] in range(paddle2_pos[1]-50,paddle2_pos[1]+51) and ball_pos[0]>int(WIDTH/2)):
			if ball_vel[0]<0:
				ball_vel[0] =-(ball_vel[0]-1)
			else:
				ball_vel[0] =-(ball_vel[0]+1)
		else:
			if ball_pos[0]>int(WIDTH/2):
				score2 +=1
				spawn_ball("Left")
			else:
				score1 +=1
				spawn_ball("Right")

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
