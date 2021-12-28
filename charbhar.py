import pygame
import sys
from time import sleep
from random import randint
class Settings():
	"""A class to store all settings of चर-भर"""
	def __init__(self):
		"""Initialize the game's static settings"""
		self.screen_width = 1440
		self.screen_height = 800
		self.red_color = (100,0,0)
		self.blue_color = (0,0,100)
		self.goti_radius = 40
		self.number_of_players = 2
def check_keydown_events(event):
	"""Respond to keypresses"""
	if event.key == pygame.K_q:
		sys.exit()
def check_keyup_events(event):
	"""Respond to key releases"""
	return
def check_mouse_events(settings, event, screen, centre, red, blue, move, bhar,
	count, icon, icon_rect, icon_clicked):
	"""Respond to mouse events"""
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# print(icon_rect)
	tmp = icon_rect.collidepoint(mouse_x, mouse_y)
	tmp2 = False
	if tmp and not icon_clicked[0]:
		icon_clicked[0] = True
	elif tmp and icon_clicked[0]:
		icon_clicked[0] = False
	if icon_clicked[0]:
		tmp2 = True
		cen = screen.get_rect().center
		for i in range(3):
			if (mouse_x <= cen[0]+200 and mouse_x >= cen[0]-200 and
				mouse_y <= cen[1]+100*i+50 and mouse_y >= cen[1]+100*i-50):
				settings.number_of_players = i
				for i in range(25):
					red[i] = False
					blue[i] = False
				count[0] = 0; move[0] = 0; bhar[0] = 0;
				icon_clicked[0] = False
	r = settings.goti_radius; n = settings.number_of_players;
	for i in range (1,25):
		if (not icon_clicked[0] and not tmp2 and
			mouse_x <= centre[i][0]+r and mouse_x >= centre[i][0]-r and
			mouse_y <= centre[i][1]+r and mouse_y >= centre[i][1]-r):
			if bhar[0]:
				if bhar[0] == 1 and blue[i] and not is_bhar(i, red, blue, 2):
					blue[i] = False; bhar[0] = 0;
				elif bhar[0] == 2 and red[i] and not is_bhar(i, red, blue, 1):
					red[i] = False; bhar[0] = 0;
			elif count[0] < 18 and red[i] == False and blue[i] == False:
				if n == 2 and count[0]%2 == 0:
					red[i] = True
					if is_bhar(i, red, blue, 1):
						bhar[0] = 1
				elif n > 0 and count[0]%2 == 1:
					blue[i] = True
					if is_bhar(i, red, blue, 2):
						bhar[0] = 2
				if n == 2 or n == 1 and count[0]%2 == 1:
					count[0] += 1
					print_board(count, red, blue)
			elif count[0] >= 18:
				if n == 2 and count[0]%2 == 0 and red[i] == True:
					move[0] = i
				if n > 0 and count[0]%2 == 1 and blue[i] == True:
					move[0] = i
				if move[0] and red[i] == False and blue[i] == False:
					if movable(move, i):
						if n == 2 and count[0]%2 == 0:
							red[i] = True; red[move[0]] = False;
							if is_bhar(i, red, blue, 1):
								bhar[0] = 1
						elif n > 0 and count[0]%2 == 1:
							blue[i] = True; blue[move[0]] = False;
							if is_bhar(i, red, blue, 2):
								bhar[0] = 2
						if n == 2 or n == 1 and count[0]%2 == 1:
							move[0] = 0; count[0] += 1;
							print_board(count, red, blue)
def check_events(settings, screen, centre, red, blue, move, bhar, count, icon,
		icon_rect, icon_clicked):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event)
		if event.type == pygame.KEYUP:
			check_keyup_events(event)
		if event.type == pygame.MOUSEBUTTONDOWN:
			check_mouse_events(settings, event, screen, centre, red, blue, move,
			bhar, count, icon, icon_rect, icon_clicked)
def movable(move, i):
	"""if move is valid return true"""
	if (move[0] == 1 and (i == 2 or i == 10) or
		move[0] == 2 and (i == 1 or i == 3 or i == 5) or
		move[0] == 3 and (i == 2 or i == 15) or
		move[0] == 4 and (i == 5 or i == 11) or
		move[0] == 5 and (i == 2 or i == 4 or i == 6 or i == 8) or
		move[0] == 6 and (i == 5 or i == 14) or
		move[0] == 7 and (i == 8 or i == 12) or
		move[0] == 8 and (i == 5 or i == 7 or i == 9) or
		move[0] == 9 and (i == 8 or i == 13) or
		move[0] == 10 and (i == 1 or i == 11 or i == 22) or
		move[0] == 11 and (i == 4 or i == 10 or i == 12 or i == 19) or
		move[0] == 12 and (i == 7 or i == 11 or i == 16) or
		move[0] == 13 and (i == 9 or i == 14 or i == 18) or
		move[0] == 14 and (i == 6 or i == 13 or i == 15 or i == 21) or
		move[0] == 15 and (i == 3 or i == 14 or i == 24) or
		move[0] == 16 and (i == 12 or i == 17) or
		move[0] == 17 and (i == 16 or i == 18 or i == 20) or
		move[0] == 18 and (i == 13 or i == 17) or
		move[0] == 19 and (i == 11 or i == 20) or
		move[0] == 20 and (i == 17 or i == 19 or i == 21 or i == 23) or
		move[0] == 21 and (i == 14 or i == 20) or
		move[0] == 22 and (i == 10 or i == 23) or
		move[0] == 23 and (i == 20 or i == 22 or i == 24) or
		move[0] == 24 and (i == 15 or i == 23)
		):
		return True
	return False
def is_red_bhar(i, red):
	if (i == 1 and red[2] and red[3] or	i == 1 and red[10] and red[22] or
		i == 2 and red[1] and red[3] or i == 2 and red[5] and red[8] or
		i == 3 and red[1] and red[2] or i == 3 and red[15] and red[24] or
		i == 4 and red[5] and red[6] or i == 4 and red[11] and red[19] or
		i == 5 and red[4] and red[6] or i == 5 and red[2] and red[8] or
		i == 6 and red[4] and red[5] or i == 6 and red[14] and red[21] or
		i == 7 and red[8] and red[9] or i == 7 and red[12] and red[16] or
		i == 8 and red[2] and red[5] or i == 8 and red[7] and red[9] or
		i == 9 and red[7] and red[8] or i == 9 and red[13] and red[18] or
		i == 10 and red[1] and red[22] or i == 10 and red[11] and red[12] or
		i == 11 and red[4] and red[19] or i == 11 and red[10] and red[12] or
		i == 12 and red[7] and red[16] or i == 12 and red[10] and red[11] or
		i == 13 and red[9] and red[18] or i == 13 and red[14] and red[15] or
		i == 14 and red[6] and red[21] or i == 14 and red[13] and red[15] or
		i == 15 and red[3] and red[24] or i == 15 and red[13] and red[14] or
		i == 16 and red[7] and red[12] or i == 16 and red[17] and red[18] or
		i == 17 and red[16] and red[18] or i == 17 and red[20] and red[23] or
		i == 18 and red[9] and red[13] or i == 18 and red[16] and red[17] or
		i == 19 and red[4] and red[11] or i == 19 and red[20] and red[21] or
		i == 20 and red[17] and red[23] or i == 20 and red[19] and red[21] or
		i == 21 and red[6] and red[14] or i == 21 and red[19] and red[20] or
		i == 22 and red[1] and red[10] or i == 22 and red[23] and red[24] or
		i == 23 and red[17] and red[20] or i == 23 and red[22] and red[24] or
		i == 24 and red[3] and red[15] or i == 24 and red[22] and red[23]
		):
		return True
	return False
def is_blue_bhar(i, blue):
	if (i == 1 and blue[2] and blue[3] or i == 1 and blue[10] and blue[22] or
		i == 2 and blue[1] and blue[3] or i == 2 and blue[5] and blue[8] or
		i == 3 and blue[1] and blue[2] or i == 3 and blue[15] and blue[24] or
		i == 4 and blue[5] and blue[6] or i == 4 and blue[11] and blue[19] or
		i == 5 and blue[4] and blue[6] or i == 5 and blue[2] and blue[8] or
		i == 6 and blue[4] and blue[5] or i == 6 and blue[14] and blue[21] or
		i == 7 and blue[8] and blue[9] or i == 7 and blue[12] and blue[16] or
		i == 8 and blue[2] and blue[5] or i == 8 and blue[7] and blue[9] or
		i == 9 and blue[7] and blue[8] or i == 9 and blue[13] and blue[18] or
		i == 10 and blue[1] and blue[22] or i == 10 and blue[11] and blue[12] or
		i == 11 and blue[4] and blue[19] or i == 11 and blue[10] and blue[12] or
		i == 12 and blue[7] and blue[16] or i == 12 and blue[10] and blue[11] or
		i == 13 and blue[9] and blue[18] or i == 13 and blue[14] and blue[15] or
		i == 14 and blue[6] and blue[21] or i == 14 and blue[13] and blue[15] or
		i == 15 and blue[3] and blue[24] or i == 15 and blue[13] and blue[14] or
		i == 16 and blue[7] and blue[12] or i == 16 and blue[17] and blue[18] or
		i == 17 and blue[16] and blue[18] or
		i == 17 and blue[20] and blue[23] or
		i == 18 and blue[9] and blue[13] or i == 18 and blue[16] and blue[17] or
		i == 19 and blue[4] and blue[11] or i == 19 and blue[20] and blue[21] or
		i == 20 and blue[17] and blue[23] or
		i == 20 and blue[19] and blue[21] or
		i == 21 and blue[6] and blue[14] or i == 21 and blue[19] and blue[20] or
		i == 22 and blue[1] and blue[10] or i == 22 and blue[23] and blue[24] or
		i == 23 and blue[17] and blue[20] or
		i == 23 and blue[22] and blue[24] or
		i == 24 and blue[3] and blue[15] or i == 24 and blue[22] and blue[23]
		):
		return True
	return False
def is_bhar(i, red, blue, turn):
	"""if bhar is made return true"""
	if (turn == 1 and is_red_bhar(i, red)):
		return True
	if (turn == 2 and is_blue_bhar(i, blue)):
		return True
	return False
def print_board(count, red, blue):
	print(f"\x1b[33mcount[0] = {count[0]}\x1b[0m")
	for i in range(1,25):
		if red[i]:
			print(f"\x1b[31m{i}\x1b[0m", end = "")
		elif blue[i]:
			print(f"\x1b[34m{i}\x1b[0m", end = "")
		else:
			print(f"{i}", end = "")
		if i == 1 or i == 2:
			print("--------", end = "")
		elif i == 22 or i == 23:
			print("-------", end = "")
		elif i == 3:
			print("\n|  ", end = "")
		elif i == 18:
			print(" |  |\n|  ", end = "")
		elif i == 4 or i == 5:
			print("-----", end = "")
		elif i == 19 or i == 20:
			print("----", end = "")
		elif i == 12:
			print("    ", end = "")
		elif i == 6:
			print("  |\n|  |  ", end = "")
		elif i == 15:
			print("\n|  |  ", end = "")
		elif i == 7 or i == 8:
			print("--", end = "")
		elif i == 10 or i == 11 or i == 13 or i == 14 or i == 16 or i == 17:
			print("-", end = "")
		elif i == 9:
			print("  |  |\n", end = "")
		elif i == 21:
			print(" |\n", end = "")
		elif i == 24:
			print("\n", end = "")
def computer_moves(count, bhar, move, red, blue, n):
	if count[0] < 18 and (n == 0 or n == 1 and count[0]%2 == 0):
		while True:
			rand = randint(1,24)
			if bhar[0] == 2 and count[0]%2 == 0 and n == 1:
				break
			elif bhar[0]:
				if (bhar[0] == 1 and blue[rand] and
					not is_bhar(rand, red, blue, 2)):
					blue[rand] = False
					bhar[0] = 0
					break
				elif(bhar[0] == 2 and red[rand] and
					not is_bhar(rand, red, blue, 1)):
					red[rand] = False
					bhar[0] = 0
					break
			elif count[0]%2 == 0 and red[rand] == 0 and blue[rand] == 0:
				red[rand] = True
				count[0] += 1
				print_board(count, red, blue)
				if is_bhar(rand, red, blue, 1):
					bhar[0] = 1
					continue
				break
			elif count[0]%2 == 1 and blue[rand] == False and red[rand] == False:
				blue[rand] = True
				count[0] += 1
				print_board(count, red, blue)
				if is_bhar(rand, red, blue, 2):
					bhar[0] = 2
				break
	elif count[0] >= 18 and (n == 0 or n == 1 and count[0]%2 == 0):
		while True:
			rand = randint(1,24)
			if bhar[0] == 2 and count[0]%2 == 0 and n == 1:
				break
			elif bhar[0]:
				if (bhar[0] == 1 and blue[rand] and
					not is_bhar(rand, red, blue, 2)):
					blue[rand] = False
					bhar[0] = 0
					break
				elif(bhar[0] == 2 and red[rand] and
					not is_bhar(rand, red, blue, 1)):
					red[rand] = False
					bhar[0] = 0
					break
			elif move[0] and count[0]%2 == 1 and n == 1:
				break
			elif move[0] and red[rand] == False and blue[rand] == False:
				if movable(move, rand):
					if count[0]%2 == 0:
						print("Move red from "+str(move[0])+" to "+str(rand))
						red[rand] = True
						red[move[0]] = False
						if is_bhar(rand, red, blue, 1):
							bhar[0] = 1
							move[0] = 0
							count[0] += 1
							print_board(count, red, blue)
							continue
					elif count[0]%2 == 1:
						print("Move blue from "+str(move[0])+" to "+str(rand))
						blue[rand] = True
						blue[move[0]] = False
						if is_bhar(rand, red, blue, 2):
							bhar[0] = 2
					move[0] = 0
					count[0] += 1
					print_board(count, red, blue)
					break
			elif count[0]%2 == 0 and red[rand]:
				move[0] = rand
				break
			elif count[0]%2 == 1 and blue[rand]:
				move[0] = rand
				break
def game_over(screen, count, move, bhar, red, blue, r, b, cen):
	font = pygame.font.Font(None, 200)
	if r < 3:
		text = font.render('Blue wins', True, (0,0,255))
	if b < 3:
		text = font.render('Red wins', True, (255,0,0))
	text_rect = text.get_rect()
	text_rect.center = cen
	screen.blit(text, text_rect)
	pygame.display.flip()
	sleep(3)
	text = font.render('Replay in 3 sec', True, (0,255,0))
	text_rect = text.get_rect()
	text_rect.center = cen
	screen.blit(text, text_rect)
	pygame.display.flip()
	sleep(3)
	for i in range(25):
		red[i] = False
		blue[i] = False
	count[0] = 0; move[0] = 0; bhar[0] = 0;
def draw_board(settings, screen, centre, red, blue, move, bhar, count, icon,
		icon_rect, icon_clicked):
	"""Draw full board on screen"""
	if count[0]%2 == 0:
		screen.fill(settings.red_color)
	else:
		screen.fill(settings.blue_color)
	screen_rect = screen.get_rect()
	cen = screen_rect.center
	right = screen_rect.right
	bottom = screen_rect.bottom
	pygame.draw.rect(screen, (0,255,0), [100,100,right-200,bottom-200], 1)
	pygame.draw.rect(screen, (0,255,0), [200,200,right-400,bottom-400], 1)
	pygame.draw.rect(screen, (0,255,0), [300,300,right-600,bottom-600], 1)
	pygame.draw.rect(screen, (0,255,0), pygame.Rect(cen[0],100,1,200), 1)
	pygame.draw.rect(screen, (0,255,0), [cen[0],bottom-300,1,200], 1)
	pygame.draw.rect(screen, (0,255,0), pygame.Rect(100,cen[1],200,1), 1)
	pygame.draw.rect(screen, (0,255,0), pygame.Rect(right-300,cen[1],200,1), 1)
	r = 0; b = 0; rad = settings.goti_radius; n = settings.number_of_players;
	for i in range(1,25):
		if red[i]:
			pygame.draw.circle(screen, (255,0,0), centre[i], rad, 0)
			r += 1
		if blue[i]:
			pygame.draw.circle(screen, (0,0,255), centre[i], rad, 0)
			b += 1
	if icon_clicked[0]:
		screen.fill((0,100,0))
		font = pygame.font.Font(None, 100)
		text = font.render('Select number of players', True, (0,255,0))
		text_rect = text.get_rect()
		text_rect.center = cen[0], cen[1]-200
		screen.blit(text, text_rect)
		text = font.render('0', True, (0,255,0))
		text_rect = text.get_rect()
		text_rect.center = cen[0], cen[1]+000
		screen.blit(text, text_rect)
		text = font.render('1', True, (0,255,0))
		text_rect = text.get_rect()
		text_rect.center = cen[0], cen[1]+100
		screen.blit(text, text_rect)
		text = font.render('2', True, (0,255,0))
		text_rect = text.get_rect()
		text_rect.center = cen[0], cen[1]+200
		screen.blit(text, text_rect)
	screen.blit(icon, icon_rect)
	computer_moves(count, bhar, move, red, blue, n)
	if count[0] >= 18 and (r < 3 or b < 3):
		game_over(screen, count, move, bhar, red, blue, r, b, cen)
def set_centre(settings, screen):
	"""set centre dimensions of all 24 places"""
	screen_rect = screen.get_rect()
	cen = screen.get_rect().center
	right = screen_rect.right
	bottom = screen_rect.bottom
	centre = [[0,0] for i in range(25)]
	centre[1] = [100,100];              centre[2] = [cen[0],100];
	centre[3] = [right-100,100];        centre[4] = [200,200];
	centre[5] = [cen[0],200];           centre[6] = [right-200,200];
	centre[7] = [300,300];              centre[8] = [cen[0],300];
	centre[9] = [right-300,300];        centre[10] = [100,cen[1]];
	centre[11] = [200,cen[1]];          centre[12] = [300,cen[1]];
	centre[13] = [right-300,cen[1]];    centre[14] = [right-200,cen[1]];
	centre[15] = [right-100,400];       centre[16] = [300,bottom-300];
	centre[17] = [cen[0],bottom-300];   centre[18] = [right-300,bottom-300];
	centre[19] = [200,bottom-200];      centre[20] = [cen[0],bottom-200];
	centre[21] = [right-200,bottom-200];centre[22] = [100,bottom-100];
	centre[23] = [cen[0],bottom-100];   centre[24] = [right-100,bottom-100];
	return centre
def run_game():
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(
		(settings.screen_width,settings.screen_height))
	pygame.display.set_caption("चर-भर")
	centre = set_centre(settings, screen)
	red = [False for i in range(25)]
	blue = [False for i in range(25)]
	count = [0]; move = [0]; bhar = [0];
	icon = pygame.image.load('images/settings.png')
	icon_clicked = [False]
	icon_rect = icon.get_rect()
	icon_rect.center = (settings.screen_width-12, 12)
	while True:
		check_events(settings, screen, centre, red, blue, move, bhar, count,
			icon, icon_rect, icon_clicked)
		draw_board(settings, screen, centre, red, blue, move, bhar, count, icon,
			icon_rect, icon_clicked)
		pygame.display.flip()
run_game()
# मेरा नाम आशिष है।
# मेरा नाम आशिष है।