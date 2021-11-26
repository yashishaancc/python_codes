import pygame
from random import randint
class Settings():
	def __init__(self):
		self.screen_width = 500
		self.screen_height = 500
		self.red_color = (100,0,0)
		self.blue_color = (0,0,100)
		self.goti_radius = 20
		self.number_of_rows = 8
		self.number_of_columns = 8
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
	for i in range(1,c+1):
		for j in range(1,r+1):
			if (ball[0] == 0 and mouse_x >= b*i and mouse_x <= b*(i+1) and
				mouse_y >= b*j and mouse_y <= b*(j+1)):
				if n == 2 or n == 1 and count[0]%2 == 1:
					is_valid(settings, ball, j, i, count)
def is_valid(settings, ball, row, column, count):
	r = settings.number_of_rows; c = settings.number_of_columns;
	if ball[(row-1)*c+column]:
		return False
	if count[0]%2 == 0:
		ball[(row-1)*c+column] = 1
	else:
		ball[(row-1)*c+column] = 2
	change = 0;
	i = row-1; j = column-1;
	while i >= 1 and column >= 1:# north-west
		if not i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			change = 1
			i += 1; j += 1;
			while i < row and j < column:
				ball[(i-1)*c+j] = ball[(row-1)*c+column]
				i += 1; j += 1;
			break
		if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			break
		if ball[(i-1)*c+j] == 0:
			break
		i -= 1; j -= 1;
	i = row+1; j = column+1;
	while i <= r and j <= c:# south-east
		if not i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			change = 1
			i -= 1; j -= 1;
			while i > row and j > column:
				ball[(i-1)*c+j] = ball[(row-1)*c+column]
				i -= 1; j -= 1;
			break
		if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			break
		if ball[(i-1)*c+j] == 0:
			break
		i += 1; j += 1;
	i = row-1; j = column+1;
	while i >= 1 and j <= c:# north-east
		if not i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			change = 1
			i += 1; j -= 1;
			while i < row and j > column:
				ball[(i-1)*c+j] = ball[(row-1)*c+column]
				i += 1; j -= 1;
			break
		if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			break
		if ball[(i-1)*c+j] == 0:
			break
		i -= 1; j += 1;
	i = row+1; j = column-1;
	while i <= r and j >= 0:# south-west
		if not i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			change = 1
			i -= 1; j += 1;
			while i > row and j < column:
				ball[(i-1)*c+j] = ball[(row-1)*c+column]
				i -= 1; j += 1;
			break
		if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			break
		if ball[(i-1)*c+j] == 0:
			break
		i += 1; j -= 1;
	i = row-1; j = column;
	while i >= 0:# north
		if not i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			change = 1
			i += 1;
			while i < row:
				ball[(i-1)*c+j] = ball[(row-1)*c+column]
				i += 1;
			break
		if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			break
		if ball[(i-1)*c+j] == 0:
			break
		i -= 1;
	i = row+1; j = column;
	while i <= r:# south
		if not i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			change = 1
			i -= 1;
			while i > row:
				ball[(i-1)*c+j] = ball[(row-1)*c+column]
				i -= 1;
			break
		if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			break
		if ball[(i-1)*c+j] == 0:
			break
		i += 1;
	i = row; j = column+1;
	while j <= c:# east
		if not j == column+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			change = 1
			j -= 1;
			while j > column:
				ball[(i-1)*c+j] = ball[(row-1)*c+column]
				j -= 1;
			break
		if j == column+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			break
		if ball[(i-1)*c+j] == 0:
			break
		j += 1;
	i = row; j = column-1;
	while j >= 0:# west
		if j != column-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			change = 1
			j += 1;
			while j < column:
				ball[(i-1)*c+j] = ball[(row-1)*c+column]
				j += 1;
			break
		if j == column-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
			break
		if ball[(i-1)*c+j] == 0:
			break
		j -= 1;
	if (change == 0):
		ball[(row-1)*c+column] = 0
		return False
	else:
		count[0] += 1
		return True
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
	if n == 0 and ball[0] == 0 or n == 1 and count[0]%2 == 0 and ball[0] == 0:
		flag = 0; v = 0; cnt = 0; rcnt = 0; bcnt = 0;
		for row in range(1,r+1):
			for column in range(1,c+1):
				if ball[(row-1)*c+column]:
					cnt += 1
					if ball[(row-1)*c+column] == 1:
						rcnt += 1
					if ball[(row-1)*c+column] == 2:
						bcnt += 1
					continue
				if count[0]%2 == 0:
					ball[(row-1)*c+column] = 1
				else:
					ball[(row-1)*c+column] = 2
				change = 0;
				i = row-1; j = column-1;
				while i >= 1 and column >= 1:# north-west
					if i != row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						change = 1
						break
					if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						break
					if ball[(i-1)*c+j] == 0:
						break
					i -= 1; j -= 1;
				i = row+1; j = column+1;
				while i <= r and j <= c:# south-east
					if i != row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						change = 1
						break
					if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						break
					if ball[(i-1)*c+j] == 0:
						break
					i += 1; j += 1;
				i = row-1; j = column+1;
				while i >= 1 and j <= c:# north-east
					if i != row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						change = 1
						break
					if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						break
					if ball[(i-1)*c+j] == 0:
						break
					i -= 1; j += 1;
				i = row+1; j = column-1;
				while i <= r and j >= 0:# south-west
					if i != row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						change = 1
						break
					if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						break
					if ball[(i-1)*c+j] == 0:
						break
					i += 1; j -= 1;
				i = row-1; j = column;
				while i >= 0:# north
					if i != row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						change = 1
						break
					if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						break
					if ball[(i-1)*c+j] == 0:
						break
					i -= 1;
				i = row+1; j = column;
				while i <= r:# south
					if i != row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						change = 1
						break
					if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						break
					if ball[(i-1)*c+j] == 0:
						break
					i += 1;
				i = row; j = column+1;
				while j <= c:# east
					if j != column+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						change = 1
						break
					if j == column+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						break
					if ball[(i-1)*c+j] == 0:
						break
					j += 1;
				i = row; j = column-1;
				while j >= 0:# west
					if j != column-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						change = 1
						break
					if j == column-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
						break
					if ball[(i-1)*c+j] == 0:
						break
					j -= 1;
				ball[(row-1)*c+column] = 0
				if change:
					v = 1
					break
			if v:
				break
		while v:
			row = randint(1,r)
			column = randint(1,c)
			if (is_valid(settings, ball, row, column, count)):
				break
	for i in range(1,r+1):
		for j in range(1,c+1):
			pygame.draw.rect(screen, (0,255,0), [b*j,b*i,b,b], 1)
			if ball[(i-1)*c+j] == 1:
				pygame.draw.circle(screen, (255,0,0), [b*j+b/2,b*i+b/2],
					rad, 0)
			if ball[(i-1)*c+j] == 2:
				pygame.draw.circle(screen, (0,0,255), [b*j+b/2,b*i+b/2],
					rad, 0)
	flag = 0; v = 0; cnt = 0; rcnt = 0; bcnt = 0;
	for row in range(1,r+1):
		for column in range(1,c+1):
			if ball[(row-1)*c+column]:
				cnt += 1
				if ball[(row-1)*c+column] == 1:
					rcnt += 1
				if ball[(row-1)*c+column] == 2:
					bcnt += 1
				continue
			if count[0]%2 == 0:
				ball[(row-1)*c+column] = 1
			else:
				ball[(row-1)*c+column] = 2
			change = 0;
			i = row-1; j = column-1;
			while i >= 1 and column >= 1:# north-west
				if i != row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					change = 1
					break
				if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					break
				if ball[(i-1)*c+j] == 0:
					break
				i -= 1; j -= 1;
			i = row+1; j = column+1;
			while i <= r and j <= c:# south-east
				if i != row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					change = 1
					break
				if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					break
				if ball[(i-1)*c+j] == 0:
					break
				i += 1; j += 1;
			i = row-1; j = column+1;
			while i >= 1 and j <= c:# north-east
				if i != row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					change = 1
					break
				if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					break
				if ball[(i-1)*c+j] == 0:
					break
				i -= 1; j += 1;
			i = row+1; j = column-1;
			while i <= r and j >= 0:# south-west
				if i != row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					change = 1
					break
				if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					break
				if ball[(i-1)*c+j] == 0:
					break
				i += 1; j -= 1;
			i = row-1; j = column;
			while i >= 0:# north
				if i != row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					change = 1
					break
				if i == row-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					break
				if ball[(i-1)*c+j] == 0:
					break
				i -= 1;
			i = row+1; j = column;
			while i <= r:# south
				if i != row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					change = 1
					break
				if i == row+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					break
				if ball[(i-1)*c+j] == 0:
					break
				i += 1;
			i = row; j = column+1;
			while j <= c:# east
				if j != column+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					change = 1
					break
				if j == column+1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					break
				if ball[(i-1)*c+j] == 0:
					break
				j += 1;
			i = row; j = column-1;
			while j >= 0:# west
				if j != column-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					change = 1
					break
				if j == column-1 and ball[(i-1)*c+j] == ball[(row-1)*c+column]:
					break
				if ball[(i-1)*c+j] == 0:
					break
				j -= 1;
			ball[(row-1)*c+column] = 0
			if change:
				v = 1
				break
		if v:
			break
	if v == 0:
		if cnt != r*c:
			if count[0]%2 == 0:
				flag = 2
			else:
				flag = 1
		elif rcnt > bcnt:
			flag = 1
		elif bcnt > rcnt:
			flag = 2
		else:
			flag = 3
	if(flag == 1 or flag == 2 or flag == 3):
		ball[0] = 1
		font = pygame.font.SysFont(None, 100)
		if flag == 3:
			text = font.render('Game draw', True, (0,255,0), (255,0,255))
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
	pygame.display.set_caption("Othello")
	r = settings.number_of_rows; c = settings.number_of_columns;
	ball = [0 for i in range(r*c+1)]
	ball[int((r/2-1)*c+c/2)] = 1; ball[int((r/2)*c+c/2+1)] = 1;
	ball[int((r/2-1)*c+c/2+1)] = 2; ball[int((r/2)*c+c/2)] = 2;
	count = [0]
	while True:
		check_events(settings, ball, count)
		draw_board(settings, screen, ball, count)
		pygame.display.flip()
run_game()