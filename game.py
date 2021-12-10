import pygame
def run_game():
	pygame.init()
	pygame.display.set_mode((1440,900))
	pygame.display.set_caption("Empty window")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
run_game()