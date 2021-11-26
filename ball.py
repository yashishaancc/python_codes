import pygame
import sys
global multiplier
def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event)
		if event.type == pygame.KEYUP:
			check_keyup_events(event)
		if event.type == pygame.MOUSEBUTTONDOWN:
			check_mouse_events(event)
def check_keydown_events(event):
	global multiplier
	if event.key == pygame.K_q:
		sys.exit()
	if event.key == pygame.K_DOWN:
		multiplier *= 2
	if event.key == pygame.K_UP:
		multiplier /= 2
def check_keyup_events(event):
	return
def check_mouse_events(event):
	return
def draw_ball(screen, count):
	if (720+count[0]%2720 <= 1400):
		x = 720+count[0]%2720
	elif (720+count[0]%2720 <= 1400+1360):
		x = 1400-count[0]%2720+680
	else:
		x = count[0]%2720-680-1360
	if (400+count[0]%1440 <= 760):
		y = 400+count[0]%1440
	elif (400+count[0]%1440 <= 760+720):
		y = 760-count[0]%1440+360 
	else:
		y = count[0]%1440-360-720
	screen.fill((0,0,0))
	pygame.draw.circle(screen, (0,255,0), [x,y], 40, 0)
	global multiplier
	count[0] += 10*multiplier
def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1440,800))
	pygame.display.set_caption("Ball")
	count = [0]
	global multiplier
	multiplier = 1
	while True:
		check_events()
		draw_ball(screen, count)
		pygame.display.flip()
run_game()