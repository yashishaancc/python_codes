import pygame
from pygame import mixer
import sys
from random import randint as rand
def check_events(move, move_up, move_down):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event, move, move_up, move_down)
		if event.type == pygame.KEYUP:
			check_keyup_events(event, move_up, move_down)
		if event.type == pygame.MOUSEBUTTONDOWN:
			check_mouse_events(event)
def check_keydown_events(event, move, move_up, move_down):
	if event.key == pygame.K_q:
		sys.exit()
	if event.key == pygame.K_SPACE:
		move[0] = True
	if event.key == pygame.K_UP:
		move_up[0] = True
	if event.key == pygame.K_DOWN:
		move_down[0] = True
def check_keyup_events(event, move_up, move_down):
	if event.key == pygame.K_UP:
		move_up[0] = False
	if event.key == pygame.K_DOWN:
		move_down[0] = False
def check_mouse_events(event):
	return
def update_arrow(move, move_up, move_down, arrow_x, arrow_y, skip, game_speed):
	if move[0]:
		if arrow_x[0] == 200:
			mixer.init()
			mixer.music.load('sounds/arrow.mp3')
			mixer.music.play()
		arrow_x[0] += 5*game_speed[0]
	elif move_up[0]:
		arrow_y[0] -= 1*game_speed[0]
		if arrow_y[0] <= 0:
			arrow_y[0] = 800
	elif move_down[0]:
		arrow_y[0] += 1*game_speed[0]
		if arrow_y[0] >= 800:
			arrow_y[0] = 0
	if arrow_x[0] > 1500:
		arrow_x[0] = 200
		move[0] = False
		skip[0] += 1
def balloon_pop(screen, score, highscore, game_speed, balloon_burst, balloon_x,
	balloon_y, arrow_x, move):
	score[0] += 1
	if highscore[0] < score[0]:
		highscore[0] = score[0]
	game_speed[0] += 0.5
	balloon_burst_rect = balloon_burst.get_rect()
	balloon_burst_rect.center = (balloon_x[0], balloon_y[0])
	screen.blit(balloon_burst, balloon_burst_rect)
	pygame.display.flip()
	mixer.init()
	mixer.music.load('sounds/pop.mp3')
	mixer.music.play()
	pygame.time.delay(500)
	balloon_y[0] = rand(700,1400)
	arrow_x[0] = 200
	move[0] = False
def game_over(screen, score, game_speed, skip, balloon_x, balloon_y, arrow_x,
	arrow_y):
	font = pygame.font.Font('freesansbold.ttf', 100)
	text = font.render("Game Over", True, (0,0,0))
	text_rect = text.get_rect()
	text_rect.center = (720,400)
	screen.blit(text, text_rect)
	score_text = font.render("Score: "+str(score[0]), True, (0,0,0))
	score_rect = score_text.get_rect()
	score_rect.center = (720,500)
	screen.blit(score_text, score_rect)
	font = pygame.font.Font('freesansbold.ttf', 20)
	pygame.display.flip()
	pygame.time.delay(3000)
	score[0] = 0
	game_speed[0] = 10
	skip[0] = 0
	balloon_x[0] = 1300
	balloon_y[0] = 800
	arrow_x[0] = 200
	arrow_y[0] = 400
def draw_board(screen, balloon, balloon_burst, arrow, balloons, balloon_x,
	balloon_y, arrow_x, arrow_y, game_speed, move, move_up, move_down, font,
	score, highscore,skip, count):
	screen.fill((255,200,2))
	count[0] += 1
	balloon_rect = balloon.get_rect()
	balloon_rect.center = (balloon_x[0], balloon_y[0])
	balloon_y[0] -= 2*game_speed[0]
	if balloon_y[0] < -100:
		balloon_y[0] = rand(700,1400)
	arrow_rect = arrow.get_rect()
	arrow_rect.center = (arrow_x[0], arrow_y[0])
	update_arrow(move, move_up, move_down, arrow_x, arrow_y, skip, game_speed)
	if skip[0] >= 10:
		game_over(screen, score, game_speed, skip, balloon_x, balloon_y,
			arrow_x, arrow_y)
	screen.blit(balloon, balloon_rect)
	screen.blit(arrow, arrow_rect)
	if (balloon_rect.top <= arrow_rect.top and 
		balloon_rect.top+200 >= arrow_rect.bottom and
		balloon_rect.left <= arrow_rect.right and
		balloon_rect.right >= arrow_rect.right):
		balloon_pop(screen, score, highscore, game_speed, balloon_burst,
			balloon_x, balloon_y, arrow_x, move)
	text = font.render("Score: "+str(score[0]), True, (0,0,0))
	text_rect = text.get_rect()
	text_rect.center = (1350,40)
	screen.blit(text, text_rect)
	text = font.render("High Score: "+str(highscore[0]), True, (0,0,0))
	text_rect = text.get_rect()
	text_rect.center = (720,40)
	screen.blit(text, text_rect)
	text = font.render("Arrows left: "+str(10-skip[0]), True, (0,0,0))
	text_rect = text.get_rect()
	text_rect.center = (100,40)
	screen.blit(text, text_rect)
def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1440,800))
	pygame.display.set_caption("Archery")
	count = [0]
	game_speed = [10]
	move = [False]
	move_up = [False]
	move_down = [False]
	score = [0]
	highscore = [0]
	skip = [0]
	balloon_x = [1300]
	balloon_y = [800]
	balloons = []
	arrow_x = [200]
	arrow_y = [400]
	clock = pygame.time.Clock()
	balloon = pygame.image.load('images/balloon copy.png')
	balloon_burst = pygame.image.load('images/balloon_burst copy.png')
	arrow = pygame.image.load('images/arrow copy.png')
	font = pygame.font.Font('freesansbold.ttf', 20)
	while True:
		check_events(move, move_up, move_down)
		draw_board(screen, balloon, balloon_burst, arrow, balloons, balloon_x,
			balloon_y, arrow_x, arrow_y, game_speed, move, move_up, move_down,
			font, score, highscore, skip, count)
		clock.tick(60)
		pygame.display.flip()
run_game()