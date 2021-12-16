import pygame
import sys
from pygame import mixer
def check_events():
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
	if event.key == pygame.K_q:
		sys.exit()
def check_keyup_events(event):
	return
def check_mouse_events(event):
	return
def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1440,900))
	pygame.display.set_caption('Doraemon')
	mixer.init()
	mixer.music.load('sounds/Doraemon Theme Song.mp3')
	img_file = 'images/doraemon cartoon drawing animated film.png'
	doraemon = pygame.image.load(img_file)
	# mixer.music.play(loops = -1, start = 16)
	clock = pygame.time.Clock()
	while True:
		check_events()
		doraemon_rect = doraemon.get_rect()
		doraemon_rect.center = (720,440)
		screen.blit(doraemon, doraemon_rect)
		mixer.music.play(loops = -1, start = 16)
		pygame.display.flip()
		clock.tick(1/45)
run_game()