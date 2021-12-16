import pygame
import sys
from random import randint as rand
class Balloon():
	def __init__(self, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = 1300
		self.rect.y = 800
	def update(self, game_speed, balloons):
		self.rect.y -= game_speed[0]
		if self.rect.y <= -self.rect.height:
			balloons.pop()
	def draw(self, screen):
		screen.blit(self.image, self.rect)
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
def draw_board(screen, balloon, balloon_burst, arrow, balloons, balloon_x,
	balloon_y, arrow_x, arrow_y, game_speed, move, move_up, move_down, font,
	score, skip, count):
	screen.fill((255,200,2))
	count[0] += 1
	balloon_rect = balloon.get_rect()
	balloon_rect.center = (balloon_x[0], balloon_y[0])
	balloon_y[0] -= 2*game_speed[0]
	if balloon_y[0] < -100:
		balloon_y[0] = rand(700,1400)
	arrow_rect = arrow.get_rect()
	arrow_rect.center = (arrow_x[0], arrow_y[0])
	if move[0]:
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
		# arrow_y[0] = 400
		move[0] = False
		skip[0] += 1
	if skip[0] >= 10:
		font = pygame.font.Font('freesansbold.ttf', 100)
		text = font.render("Game Over\nReplay in 3 sec", True, (0,0,0))
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
		skip[0] = 0
		balloon_x[0] = 1300
		balloon_y[0] = 800
		arrow_x[0] = 200
		arrow_y[0] = 400
	# if len(balloons) <= 0:
	# 	balloons.append(Balloon(balloon))
	# for balloon in balloons:
	# 	balloon.draw(screen)
	# 	balloon.update(game_speed, balloons)
	# 	if (balloon.rect.top <= arrow_rect.top and 
	# 		balloon.rect.top+200 >= arrow_rect.bottom and
	# 		balloon.rect.left <= arrow_rect.right and
	# 		balloon.rect.right >= arrow_rect.right):
	# 		score[0] += 1
	# 		balloon_burst_rect = balloon_burst.get_rect()
	# 		balloon_burst_rect.center = (balloon.rect.x, balloon.rect.y)
	# 		screen.blit(balloon_burst, balloon_burst_rect)
	# 		pygame.display.flip()
	# 		pygame.time.delay(1000)
	# 		balloon_y[0] = 700
	# 		arrow_x[0] = 200
	# 		move[0] = False
	screen.blit(balloon, balloon_rect)
	screen.blit(arrow, arrow_rect)
	if (balloon_rect.top <= arrow_rect.top and 
		balloon_rect.top+200 >= arrow_rect.bottom and
		balloon_rect.left <= arrow_rect.right and
		balloon_rect.right >= arrow_rect.right):
		score[0] += 1
		balloon_burst_rect = balloon_burst.get_rect()
		balloon_burst_rect.center = (balloon_x[0], balloon_y[0])
		screen.blit(balloon_burst, balloon_burst_rect)
		pygame.display.flip()
		pygame.time.delay(500)
		balloon_y[0] = rand(700,1400)
		arrow_x[0] = 200
		move[0] = False
	# score[0] += 1
	# if score[0]%10 == 0:
		# game_speed[0] += 1
	text = font.render("Score: "+str(score[0]), True, (0,0,0))
	text_rect = text.get_rect()
	text_rect.center = (1350,40)
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
			font, score, skip, count)
		clock.tick(60)
		pygame.display.flip()
run_game()