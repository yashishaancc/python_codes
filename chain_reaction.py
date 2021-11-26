import pygame
from random import randint
class Settings():
	def __init__(self):
		self.screen_width = 400
		self.screen_height = 600
		self.red_color = (100,0,0)
		self.blue_color = (0,0,100)
		self.goti_radius = 10
		self.number_of_rows = 10
		self.number_of_columns = 6
		self.box_size = 50
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
	for i in range(1,r+1):
		for j in range(1,c+1):
			if (ball[0] == 0 and mouse_x >= b*j and mouse_x <= b*(j+1) and
				mouse_y >= b*i and mouse_y <= b*(i+1)):
				if n == 2 and count[0]%2 == 0 and ball[(i-1)*c+j] < 100:
					ball[(i-1)*c+j] += 1
					count[0] += 1
				elif(count[0]%2 == 1 and 
					(ball[(i-1)*c+j] == 0 or ball[(i-1)*c+j] > 100)):
					if ball[(i-1)*c+j] == 0:
						ball[(i-1)*c+j] = 101
					else:
						ball[(i-1)*c+j] += 1
					count[0] += 1
def adj(bc, i, t):
	if t == 1:
		if bc[i] < 100:
			bc[i] += 1
		else:
			bc[i] -= 100
			bc[i] += 1
	if t == 2:
		if bc[i] < 100:
			bc[i] += 100
			bc[i] += 1
		else:
			bc[i] += 1
def adjust(settings, ball):
	r = settings.number_of_rows; c = settings.number_of_columns;
	bc = [ball[i] for i in range(r*c+1)]
	for i in range(1,r+1):
		for j in range(1,c+1):
			if i == 1 and j == 1:
				if bc[1] > 1 and bc[1] < 100:
					bc[1] -= 2
					adj(bc, 2, 1)
					adj(bc, c+1, 1)
				if bc[1] > 101:
					bc[1] -= 2
					if bc[1] == 100:
						bc[1] = 0
					adj(bc, 2, 2)
					adj(bc, c+1, 2)
			elif i == 1 and j == c:
				if bc[c] > 1 and bc[c] < 100:
					bc[c] -= 2
					adj(bc, c-1, 1)
					adj(bc, 2*c, 1)
				if bc[c] > 101:
					bc[c] -= 2
					if bc[c] == 100:
						bc[c] = 0
					adj(bc, c-1, 2)
					adj(bc, 2*c, 2)
			elif i == r and j == 1:
				if bc[(i-1)*c+j] > 1 and bc[(i-1)*c+j] < 100:
					bc[(i-1)*c+j] -= 2
					adj(bc, (i-2)*c+j, 1)
					adj(bc, (i-1)*c+j+1, 1)
				if bc[(i-1)*c+j] > 101:
					bc[(i-1)*c+j] -= 2
					if bc[(i-1)*c+j] == 100:
						bc[(i-1)*c+j] = 0
					adj(bc, (i-2)*c+j, 2)
					adj(bc, (i-1)*c+j+1, 2)
			elif i == r and j == c:
				if bc[(i-1)*c+j] > 1 and bc[(i-1)*c+j] < 100:
					bc[(i-1)*c+j] -= 2
					adj(bc, (i-2)*c+j, 1)
					adj(bc, (i-1)*c+j-1, 1)
				if bc[(i-1)*c+j] > 101:
					bc[(i-1)*c+j] -= 2
					if bc[(i-1)*c+j] == 100:
						bc[(i-1)*c+j] = 0
					adj(bc, (i-2)*c+j, 2)
					adj(bc, (i-1)*c+j-1, 2)
			elif i == 1:
				if bc[(i-1)*c+j] > 2 and bc[(i-1)*c+j] < 100:
					bc[(i-1)*c+j] -= 3
					adj(bc, (i-1)*c+j-1, 1)
					adj(bc, (i-1)*c+j+1, 1)
					adj(bc, (i)*c+j, 1)
				if bc[(i-1)*c+j] > 102:
					bc[(i-1)*c+j] -= 3
					if bc[(i-1)*c+j] == 100:
						bc[(i-1)*c+j] = 0
					adj(bc, (i-1)*c+j-1, 2)
					adj(bc, (i-1)*c+j+1, 2)
					adj(bc, (i)*c+j, 2)
			elif j == 1:
				if bc[(i-1)*c+j] > 2 and bc[(i-1)*c+j] < 100:
					bc[(i-1)*c+j] -= 3
					adj(bc, (i-2)*c+j, 1)
					adj(bc, (i-1)*c+j+1, 1)
					adj(bc, (i)*c+j, 1)
				if bc[(i-1)*c+j] > 102:
					bc[(i-1)*c+j] -= 3
					if bc[(i-1)*c+j] == 100:
						bc[(i-1)*c+j] = 0
					adj(bc, (i-2)*c+j, 2)
					adj(bc, (i-1)*c+j+1, 2)
					adj(bc, (i)*c+j, 2)
			elif j == c:
				if bc[(i-1)*c+j] > 2 and bc[(i-1)*c+j] < 100:
					bc[(i-1)*c+j] -= 3
					adj(bc, (i-2)*c+j, 1)
					adj(bc, (i-1)*c+j-1, 1)
					adj(bc, (i)*c+j, 1)
				if bc[(i-1)*c+j] > 102:
					bc[(i-1)*c+j] -= 3
					if bc[(i-1)*c+j] == 100:
						bc[(i-1)*c+j] = 0
					adj(bc, (i-2)*c+j, 2)
					adj(bc, (i-1)*c+j-1, 2)
					adj(bc, (i)*c+j, 2)
			elif i == r:
				if bc[(i-1)*c+j] > 2 and bc[(i-1)*c+j] < 100:
					bc[(i-1)*c+j] -= 3
					adj(bc, (i-1)*c+j-1, 1)
					adj(bc, (i-1)*c+j+1, 1)
					adj(bc, (i-2)*c+j, 1)
				if bc[(i-1)*c+j] > 102:
					bc[(i-1)*c+j] -= 3
					if bc[(i-1)*c+j] == 100:
						bc[(i-1)*c+j] = 0
					adj(bc, (i-1)*c+j-1, 2)
					adj(bc, (i-1)*c+j+1, 2)
					adj(bc, (i-2)*c+j, 2)
			else:
				if bc[(i-1)*c+j] > 3 and bc[(i-1)*c+j] < 100:
					bc[(i-1)*c+j] -= 4
					adj(bc, (i-1)*c+j-1, 1)
					adj(bc, (i-1)*c+j+1, 1)
					adj(bc, (i-2)*c+j, 1)
					adj(bc, (i)*c+j, 1)
				if bc[(i-1)*c+j] > 103:
					bc[(i-1)*c+j] -= 4
					if bc[(i-1)*c+j] == 100:
						bc[(i-1)*c+j] = 0
					adj(bc, (i-1)*c+j-1, 2)
					adj(bc, (i-1)*c+j+1, 2)
					adj(bc, (i-2)*c+j, 2)
					adj(bc, (i)*c+j, 2)
	for i in range(1,r+1):
		for j in range(1,c+1):
			ball[(i-1)*c+j] = bc[(i-1)*c+j]
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
	b = settings.box_size; n = settings.number_of_players
	for i in range(1,r+1):
		for j in range(1,c+1):
			pygame.draw.rect(screen, (0,255,0), [b*j,b*i,b,b], 1)
			if ball[(i-1)*c+j] == 1:
				pygame.draw.circle(screen, (255,0,0), [b*j+b/2,b*i+b/2],
					rad, 0)
			if ball[(i-1)*c+j] == 2:
				pygame.draw.circle(screen, (255,0,0), [b*j+b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+3*b/4,b*i+b/4],
					rad, 0)
			if ball[(i-1)*c+j] == 3:
				pygame.draw.circle(screen, (255,0,0), [b*j+b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+3*b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+b/4,b*i+3*b/4],
					rad, 0)
			if ball[(i-1)*c+j] == 4:
				pygame.draw.circle(screen, (255,0,0), [b*j+b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+3*b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+b/4,b*i+3*b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+3*b/4,b*i+3*b/4],
					rad, 0)
			if ball[(i-1)*c+j] == 5:
				pygame.draw.circle(screen, (255,0,0), [b*j+b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+3*b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+b/4,b*i+3*b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+3*b/4,b*i+3*b/4],
					rad, 0)
				pygame.draw.circle(screen, (255,0,0), [b*j+b/2,b*i+b/2],
					rad, 0)
			if ball[(i-1)*c+j] == 101:
				pygame.draw.circle(screen, (0,0,255), [b*j+b/2,b*i+b/2],
					rad, 0)
			if ball[(i-1)*c+j] == 102:
				pygame.draw.circle(screen, (0,0,255), [b*j+b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+3*b/4,b*i+b/4],
					rad, 0)
			if ball[(i-1)*c+j] == 103:
				pygame.draw.circle(screen, (0,0,255), [b*j+b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+3*b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+b/4,b*i+3*b/4],
					rad, 0)
			if ball[(i-1)*c+j] == 104:
				pygame.draw.circle(screen, (0,0,255), [b*j+b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+3*b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+b/4,b*i+3*b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+3*b/4,b*i+3*b/4],
					rad, 0)
			if ball[(i-1)*c+j] == 105:
				pygame.draw.circle(screen, (0,0,255), [b*j+b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+3*b/4,b*i+b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+b/4,b*i+3*b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+3*b/4,b*i+3*b/4],
					rad, 0)
				pygame.draw.circle(screen, (0,0,255), [b*j+b/2,b*i+b/2],
					rad, 0)
	adjust(settings, ball)
	flag = 0; rcnt = 0; bcnt = 0;
	if(count[0] > 1):
		for i in range(1,r+1):
			for j in range(1,c+1):
				if ball[(i-1)*c+j] > 0 and ball[(i-1)*c+j] < 100:
					rcnt += ball[(i-1)*c+j]
				if ball[(i-1)*c+j] > 100:
					bcnt += ball[(i-1)*c+j]-100
		if rcnt == 0:
			flag = 2
		if bcnt == 0:
			flag = 1
	if (n == 0 or n == 1 and count[0]%2 == 0) and ball[0] == 0:
		while flag == 0:
			rand = randint(1,r*c)
			if count[0]%2 == 0 and ball[rand] < 100:
				ball[rand] += 1
				count[0] += 1
				break
			elif count[0]%2 == 1 and (ball[rand] == 0 or ball[rand] > 100):
				if ball[rand] == 0:
					ball[rand] = 101
				else:
					ball[rand] += 1
				count[0] += 1
				break
	if(flag == 1 or flag == 2):
		ball[0] = 1
		font = pygame.font.SysFont(None, 100)
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
	pygame.display.set_caption("Chain Reaction")
	r = settings.number_of_rows; c = settings.number_of_columns;
	ball = [0 for i in range(r*c+1)]
	count = [0]
	while True:
		check_events(settings, ball, count)
		draw_board(settings, screen, ball, count)
		pygame.display.flip()
run_game()