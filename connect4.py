import pygame
from random import randint
class Settings():
	def __init__(self):
		self.screen_width = 900
		self.screen_height = 800
		self.red_color = (100,0,0)
		self.blue_color = (0,0,100)
		self.goti_radius = 40
		self.number_of_rows = 6
		self.number_of_columns = 7
		self.box_size = 100
		self.number_of_players = 2
def check_events(settings, ball, count):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event)
		if event.type == pygame.KEYUP:
			check_keyup_events(event)
		if event.type == pygame.MOUSEBUTTONDOWN:
			check_mouse_events(settings, event, ball, count)
def check_keydown_events(event):
	if event.key == pygame.KEY_q:
		sys.exit()
def check_keyup_events(event):
	return
def check_mouse_events(settings, event, ball, count):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	r = settings.number_of_rows; c = settings.number_of_columns;
	b = settings.box_size; n = settings.number_of_players;
	for i in range(1,c+1):
		if(ball[0] == 0 and mouse_x >= b*i and mouse_x <= b*(i+1)):
			cnt = 0
			for j in range(1,r+1):
				if not ball[(j-1)*c+i]:
					cnt += 1
				else:
					break
			if not(cnt == 0):
				if count[0]%2 == 0 and n == 2:
					ball[(cnt-1)*c+i] = 1
				elif n > 0:
					ball[(cnt-1)*c+i] = 2
				if n > 0:
					count[0] += 1
def draw_board(settings, screen, ball, count):
	if count[0]%2 == 0:
		screen.fill(settings.red_color)
	else:
		screen.fill(settings.blue_color)
	screen_rect = screen.get_rect()
	cen = screen_rect.center
	right = screen_rect.right
	bottom = screen_rect.bottom
	rad = settings.goti_radius
	r = settings.number_of_rows; c = settings.number_of_columns;
	b = settings.box_size; n = settings.number_of_players;
	if n == 1 and count[0]%2 == 0 and ball[0] == 0:
		cn = 0
		for i in range(1,c+1):
			cnt = 0
			for j in range(1,r+1):
				if not ball[(j-1)*c+i]:
					cnt += 1
				else:
					break
			if cnt:
				break
			else:
				cn += 1
		while cn < c:
			rand = randint(1,c)
			cnt = 0
			for j in range(1,r+1):
				if not ball[(j-1)*c+rand]:
					cnt += 1
				else:
					break
			if cnt:
				ball[(cnt-1)*c+rand] = 1
				break
		if cn < c:
			count[0] += 1
	if n == 0 and ball[0] == 0:
		cn = 0
		for i in range(1,c+1):
			cnt = 0
			for j in range(1,r+1):
				if not ball[(j-1)*c+i]:
					cnt += 1
				else:
					break
			if cnt:
				break
			else:
				cn += 1
		while cn < c:
			rand = randint(1,c)
			cnt = 0
			for j in range(1,r+1):
				if not ball[(j-1)*c+rand]:
					cnt += 1
				else:
					break
			if cnt:
				if count[0]%2 == 0:
					ball[(cnt-1)*c+rand] = 1
				else:
					ball[(cnt-1)*c+rand] = 2
				break
		if cn < c:
			count[0] += 1
	for i in range(1,r+1):
		for j in range(1,c+1):
			pygame.draw.rect(screen, (0,255,0), [b*j,b*i,b,b], 1)
			if ball[(i-1)*c+j] == 1:
				pygame.draw.circle(screen, (255,0,0), [b*j+b/2,b*i+b/2],
					rad, 0)
			if ball[(i-1)*c+j] == 2:
				pygame.draw.circle(screen, (0,0,255), [b*j+b/2,b*i+b/2],
					rad, 0)
	flag = 0
	for i in range(1,r+1-3):
		for j in range(1,c+1):
			if ball[(i-1)*c+j] and (ball[(i-1)*c+j] == ball[i*c+j]
				== ball[(i+1)*c+j] == ball[(i+2)*c+j]):
				flag = ball[(i-1)*c+j]
		for j in range(1,c+1-3):
			if ball[(i-1)*c+j] and (ball[(i-1)*c+j] == ball[i*c+j+1]
				== ball[(i+1)*c+j+2] == ball[(i+2)*c+j+3]):
				flag = ball[(i-1)*c+j]
		for j in range(1+3,c+1):
			if ball[(i-1)*c+j] and (ball[(i-1)*c+j] == ball[i*c+j-1]
				== ball[(i+1)*c+j-2] == ball[(i+2)*c+j-3]):
				flag = ball[(i-1)*c+j]
	for i in range(1,r+1):
		for j in range(1,c+1-3):
			if ball[(i-1)*c+j] and (ball[(i-1)*c+j] == ball[(i-1)*c+j+1]
				== ball[(i-1)*c+j+2] == ball[(i-1)*c+j+3]):
				flag = ball[(i-1)*c+j]
	cnt = 0
	if flag == 0:
		for i in range(1,r+1):
			for j in range(1,c+1):
				if ball[(i-1)*c+j]:
					cnt += 1
	if cnt == r*c:
		flag = 3
	if(flag == 1 or flag == 2):
		ball[0] = 1
		font = pygame.font.SysFont(None, 200)
		if flag == 3:
			text = font.render('Game draw', True, (0,0,255), (255,0,0))
		if flag == 2:
			text = font.render('Blue wins', True, (0,0,255), (255,0,0))
		if flag == 1:
			text = font.render('Red wins', True, (255,0,0), (0,0,255))
		text_rect = text.get_rect()
		text_rect.center = cen
		screen.blit(text, text_rect)
def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(
		(settings.screen_width,settings.screen_height))
	pygame.display.set_caption("Connect4")
	r = settings.number_of_rows; c = settings.number_of_columns;
	ball = [0 for i in range(r*c+1)]
	count = [0]
	while True:
		check_events(settings, ball, count)
		draw_board(settings, screen, ball, count)
		pygame.display.flip()
run_game()