import pygame
import sys
import os
from random import randint as rand
count = [0]
class Settings():
	"""A class to store all settings of Dino Game"""
	def __init__(self):
		"""Initialize the game's static settings"""
		self.screen_width = 1440
		self.screen_height = 500
		self.red_color = (100,0,0)
		self.blue_color = (0,0,100)
class Dinosaur():
	x_pos = 80
	y_pos = 310
	y_pos_duck = 340
	Jump_vel = 8.5
	def __init__(self, ducking, running, jumping):
		self.duck_img = ducking
		self.run_img = running
		self.jump_img = jumping
		self.dino_duck = False
		self.dino_run = True
		self.dino_jump = False
		self.step_index = 0
		self.jump_vel = self.Jump_vel 
		self.image = self.run_img[0]
		self.dino_rect = self.image.get_rect()
		self.dino_rect.x = self.x_pos
		self.dino_rect.y = self.y_pos
	def update(self, user_input):
		if self.dino_duck:
			self.duck()
		if self.dino_run:
			self.run()
		if self.dino_jump:
			self.jump()
		if self.step_index >= 10:
			self.step_index = 0
		if ((user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and 
			not self.dino_jump):
			self.dino_duck = False
			self.dino_run = False
			self.dino_jump = True
		elif user_input[pygame.K_DOWN] and not self.dino_jump:
			self.dino_duck = True
			self.dino_run = False
			self.dino_jump = False
		elif not (self.dino_jump or user_input[pygame.K_DOWN]):
			self.dino_duck = False
			self.dino_run = True
			self.dino_jump = False
	def duck(self):
		self.image = self.duck_img[self.step_index//5]
		self.dino_rect = self.image.get_rect()
		self.dino_rect.x = self.x_pos
		self.dino_rect.y = self.y_pos_duck
		self.step_index += 1
	def run(self):
		self.image = self.run_img[self.step_index//5]
		self.dino_rect = self.image.get_rect()
		self.dino_rect.x = self.x_pos
		self.dino_rect.y = self.y_pos
		self.step_index += 1
	def jump(self):
		self.image = self.jump_img
		if self.dino_jump:
			self.dino_rect.y -= self.jump_vel*4
			self.jump_vel -= 0.8
		if self.jump_vel < -self.Jump_vel:
			self.dino_jump = False
			self.jump_vel = self.Jump_vel
	def draw(self, screen):
		screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
class Cloud():
	def __init__(self, settings, cloud):
		self.x = settings.screen_width+rand(800,1000)
		self.y = rand(50,100)
		self.image = cloud
		self.width = self.image.get_width()
	def update(self, settings, screen, game_speed):
		self.x -= game_speed[0]
		if self.x < - self.width:
			self.x = settings.screen_width+rand(2500,3000)
			self.y = rand(50,100)
	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))
class Obstacle():
	def __init__(self, settings, image, type):
		self.image = image
		self.type = type
		self.rect = self.image[self.type].get_rect()
		self.rect.x = settings.screen_width
	def update(self, game_speed, obstacles):
		self.rect.x -= game_speed[0]
		if self.rect.x < -self.rect.width:
			obstacles.pop()
	def draw(self, screen):
		screen.blit(self.image[self.type], self.rect)
class SmallCactus(Obstacle):
	def __init__(self, settings, image):
		 self.type = rand(0,2)
		 super().__init__(settings, image, self.type)
		 self.rect.y = 325
class LargeCactus(Obstacle):
	def __init__(self, settings, image):
		 self.type = rand(0,2)
		 super().__init__(settings, image, self.type)
		 self.rect.y = 300
class Bird(Obstacle):
	def __init__(self, settings, image):
		self.type = 0
		super().__init__(settings, image, self.type)
		self.rect.y = 250
		self.index = 0
	def draw(self, screen):
		if self.index >= 9:
			self.index = 0
		screen.blit(self.image[self.index//5], self.rect) 
def check_keydown_events(event, run):
	"""Respond to keypresses"""
	if event.key == pygame.K_q:
		run[0] = False
def check_keyup_events(event):
	"""Respond to key releases"""
	return
def check_mouse_events(settings, event, screen):
	"""Respond to mouse events"""
	return
def check_events(settings, screen, run):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run[0] = False
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event, run)
		if event.type == pygame.KEYUP:
			check_keyup_events(event)
		if event.type == pygame.MOUSEBUTTONDOWN:
			check_mouse_events(settings, event, screen)
def background(screen, bg, x_pos_bg, y_pos_bg, game_speed):
	image_width = bg.get_width()
	screen.blit(bg, (x_pos_bg[0], y_pos_bg[0]))
	screen.blit(bg, (image_width+x_pos_bg[0], y_pos_bg[0]))
	if x_pos_bg[0] <= -image_width:
		screen.blit(bg, (image_width+x_pos_bg[0], y_pos_bg[0]))
		x_pos_bg[0] = 0
	x_pos_bg[0] -= game_speed[0]
def score(screen, font, points, game_speed):
	points[0] += 1
	if points[0]%100 == 0:
		game_speed[0] += 1
	text = font.render("Points: "+str(points[0]), True, (0,0,0))
	text_rect = text.get_rect()
	text_rect.center = (1350,40)
	screen.blit(text, text_rect)
def draw_board(settings, screen, player, clouds, font, bg, x_pos_bg, y_pos_bg,
		 points, obstacles, small_cactus, large_cactus, bird, running, run, 
		 death_count, game_speed):
	"""Draw full board on screen"""
	screen.fill((255,255,255))
	screen_rect = screen.get_rect()
	cen = screen_rect.center
	right = screen_rect.right
	bottom = screen_rect.bottom
	user_input = pygame.key.get_pressed()
	player.draw(screen)
	player.update(user_input)
	if len(obstacles) == 0:
		r = rand(0,2)
		if r == 0:
			obstacles.append(SmallCactus(settings, small_cactus))
		elif r == 1:
			obstacles.append(LargeCactus(settings, large_cactus))
		elif r == 2:
			obstacles.append(Bird(settings, bird))
	for obstacle in obstacles:
		obstacle.draw(screen)
		obstacle.update(game_speed, obstacles)
		if player.dino_rect.colliderect(obstacle.rect):
			pygame.time.delay(1000)
			death_count[0] += 1
			menu(screen, death_count, points, settings, running, run)
	background(screen, bg, x_pos_bg, y_pos_bg, game_speed)
	clouds.draw(screen)
	clouds.update(settings, screen, game_speed)
	score(screen, font, points, game_speed)
def menu(screen, death_count, points, settings, running, run):
	while run:
		screen.fill((255,255,255))
		font = pygame.font.Font('freesansbold.ttf', 30)
		if death_count[0] == 0:
			text = font.render("Press any key to start", True, (0,0,0))
		if death_count[0] > 0:
			text = font.render("Press any key to restart", True, (0,0,0))
			score = font.render("Your score: "+str(points[0]), True, (0,0,0))
			score_rect = score.get_rect()
			score_rect.center = (settings.screen_width//2,
								settings.screen_height//2+50)
			screen.blit(score, score_rect)
		text_rect = text.get_rect()
		text_rect.center = (settings.screen_width//2, settings.screen_height//2)
		screen.blit(text, text_rect)
		screen.blit(running[0], (settings.screen_width//2-20, 
								settings.screen_height//2-140))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run[0] = False
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				run_game()
def run_game():
	pygame.init()
	settings = Settings()
	run = [True]
	game_speed = [14]
	x_pos_bg = [0]
	y_pos_bg = [380]
	points = [0]
	death_count = [0]
	obstacles = []
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(
		(settings.screen_width,settings.screen_height))
	pygame.display.set_caption("Dino Game")
	# Loading images
	running = [pygame.image.load(os.path.join("images", "DinoRun1.png")),
				pygame.image.load(os.path.join("images", "DinoRun2.png"))]
	jumping = pygame.image.load(os.path.join("images", "DinoJump.png"))
	ducking = [pygame.image.load(os.path.join("images", "DinoDuck1.png")),
				pygame.image.load(os.path.join("images", "DinoDuck2.png"))]
	small_cactus = [pygame.image.load(os.path.join("images",
													"SmallCactus1.png")),
				pygame.image.load(os.path.join("images", "SmallCactus2.png")),
				pygame.image.load(os.path.join("images", "SmallCactus3.png"))]
	large_cactus = [pygame.image.load(os.path.join("images",
													"LargeCactus1.png")),
				pygame.image.load(os.path.join("images", "LargeCactus2.png")),
				pygame.image.load(os.path.join("images", "LargeCactus3.png"))]
	bird = [pygame.image.load(os.path.join("images", "Bird1.png")),
			pygame.image.load(os.path.join("images", "Bird2.png"))]
	cloud = pygame.image.load(os.path.join("images", "Cloud.png"))
	bg = pygame.image.load(os.path.join("images", "Track.png"))
	player = Dinosaur(ducking, running, jumping)
	clouds = Cloud(settings, cloud)
	font = pygame.font.Font('freesansbold.ttf', 20)
	if(count[0] == 0):
		count[0] += 1
		menu(screen, death_count, points, settings, running, run)
	while run[0]:
		check_events(settings, screen, run)
		draw_board(settings, screen, player, clouds, font, bg, x_pos_bg,
				y_pos_bg, points, obstacles, small_cactus, large_cactus,
				bird, running, run, death_count, game_speed)
		clock.tick(30)
		pygame.display.flip()

if __name__=="__main__":
	run_game()