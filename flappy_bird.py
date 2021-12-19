import pygame
import sys
from pygame.locals import *
import random
def check_events(game_images):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			check_keydown_events(event, game_images)
		if event.type == pygame.KEYUP:
			check_keyup_events(event)
		if event.type == pygame.MOUSEBUTTONDOWN:
			check_mouse_events(event)
def check_keydown_events(event, game_images):
	if event.key == pygame.K_q:
		sys.exit()
	if event.key == pygame.K_SPACE:
		flappygame(game_images)
	if event.key == pygame.K_UP:
		pass
	if event.key == pygame.K_DOWN:
		pass
def check_keyup_events(event):
	if event.key == pygame.K_UP:
		pass
	if event.key == pygame.K_DOWN:
		pass
def check_mouse_events(event):
	return
def createPipe(game_images):
	offset = 500//3
	pipeHeight = game_images['pipeimage'][0].get_height()
	y2 = offset+random.randrange(0, int(400 - 1.2 * offset))  
	pipeX = 600+10
	y1 = pipeHeight - y2 + offset
	pipe = [{'x': pipeX, 'y': -y1}, {'x': pipeX, 'y': y2}]
	return pipe
def isGameOver(game_images, horizontal, vertical, up_pipes, down_pipes):
    if vertical > elevation-25 or vertical<0:
        return True
    for pipe in up_pipes:
        pipeHeight = game_images['pipeimage'][0].get_height()
        if(vertical < pipeHeight + pipe['y'] and
        	abs(horizontal-pipe['x']) < game_images['pipeimage'][0].get_width()
        	):
            return True
    for pipe in down_pipes:
        if ((vertical+game_images['flappybird'].get_height() > pipe['y']) and
        	abs(horizontal-pipe['x']) < game_images['pipeimage'][0].get_width()
        	):
            return True
    return False
def flappygame(game_images):
    your_score = 0
    horizontal = int(600//5)
    vertical = int(500//2)
    ground = 0
    mytempheight = 100
    first_pipe = createPipe(game_images)
    second_pipe = createPipe(game_images)
    down_pipes = [
		{'x': 600+300-mytempheight, 'y': first_pipe[1]['y']},
		{'x': 600+300-mytempheight+(600//2), 'y': second_pipe[1]['y']},
    ]
    up_pipes = [
        {'x': 600+300-mytempheight, 'y': first_pipe[0]['y']},
        {'x': 600+200-mytempheight+(600//2), 'y': second_pipe[0]['y']},
    ]
    pipeVelX = -4
    bird_velocity_y = -9
    bird_Max_Vel_Y = 10
    bird_Min_Vel_Y = -8
    birdAccY = 1
    bird_flap_velocity = -8
    bird_flapped = False
    while True:
        for event in pygame.event.get():
            if (event.type == QUIT or
            	(event.type == KEYDOWN and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN and
            	(event.key == K_SPACE or event.key == K_UP)):
                if vertical > 0:
                    bird_velocity_y = bird_flap_velocity
                    bird_flapped = True
        game_over = isGameOver(game_images, horizontal, vertical, up_pipes,
        	down_pipes)
        if game_over:
            return
        playerMidPos = horizontal+game_images['flappybird'].get_width()//2
        for pipe in up_pipes:
            pipeMidPos = pipe['x']+game_images['pipeimage'][0].get_width()//2
            if pipeMidPos <= playerMidPos < pipeMidPos+4:
                your_score += 1
                print(f"Your your_score is {your_score}")
        if bird_velocity_y < bird_Max_Vel_Y and not bird_flapped:
            bird_velocity_y += birdAccY
        if bird_flapped:
            bird_flapped = False
        playerHeight = game_images['flappybird'].get_height()
        vertical = vertical+min(bird_velocity_y,
        	elevation-vertical-playerHeight)
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
        if 0 < up_pipes[0]['x'] < 5:
            newpipe = createPipe(game_images)
            up_pipes.append(newpipe[0])
            down_pipes.append(newpipe[1])
        if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
            up_pipes.pop(0)
            down_pipes.pop(0)
        screen.blit(game_images['background'], (0, 0))
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
            screen.blit(game_images['pipeimage'][0],
                        (upperPipe['x'], upperPipe['y']))
            screen.blit(game_images['pipeimage'][1],
                        (lowerPipe['x'], lowerPipe['y']))
        screen.blit(game_images['sea_level'], (ground, elevation))
        screen.blit(game_images['flappybird'], (horizontal, vertical))
        numbers = [int(x) for x in list(str(your_score))]
        width = 0
        for num in numbers:
            width += game_images['scoreimages'][num].get_width()
        Xoffset = (600 - width)/1.1
        for num in numbers:
            screen.blit(game_images['scoreimages'][num],
                        (Xoffset, 600*0.02))
            Xoffset += game_images['scoreimages'][num].get_width()
        pygame.display.update()
        clock.tick(60)
def run_game():
	pygame.init()
	global screen, clock
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((600,500))
	pygame.display.set_caption('Flappy Bird')
	game_images = {}
	game_images['scoreimages'] = (
		pygame.image.load('images/0.png').convert_alpha(),
		pygame.image.load('images/1.png').convert_alpha(),
		pygame.image.load('images/2.png').convert_alpha(),
		pygame.image.load('images/3.png').convert_alpha(),
		pygame.image.load('images/4.png').convert_alpha(),        
		pygame.image.load('images/5.png').convert_alpha(),
		pygame.image.load('images/6.png').convert_alpha(),
		pygame.image.load('images/7.png').convert_alpha(),
		pygame.image.load('images/8.png').convert_alpha(),
	pygame.image.load('images/9.png').convert_alpha()
	)
	game_images['flappybird'] = pygame.image.load('images/bird.png')
	game_images['sea_level'] = pygame.image.load('images/base.jfif')
	game_images['background'] = pygame.image.load('images/background.jpg')
	game_images['pipeimage'] = (
		pygame.transform.rotate(pygame.image.load('images/pipe.png'),180),
		pygame.image.load('images/pipe.png')
	)
	global elevation
	elevation = 400
	horizontal = 120
	vertical = int(500-game_images['flappybird'].get_height())//2
	print("WELCOME TO THE FLAPPY BIRD GAME")
	print("Press space or enter to start the game")
	while True:
		check_events(game_images)
		screen.blit(game_images['background'], (0,0))
		screen.blit(game_images['flappybird'], (horizontal, vertical))
		screen.blit(game_images['sea_level'], (0, elevation))
		pygame.display.flip()
		clock.tick(60)
run_game()