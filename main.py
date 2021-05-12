import pygame
import math
import random
import time
import os

from src.colors import colors
from src.tele_main import tele_main
from src.background import draw
from src.background import stone
from src.ground_1 import ground_1

pygame.init()

pygame.display.set_caption("Yolo_pp!")

screen = draw()
stone = stone()
color = colors()

pygame.display.set_icon(screen.icon)

def Add_actor(): # list actor
	global img, actor
	img = []
	path = "./img/mainer"
	FJoin = os.path.join
	files = [FJoin(path, f) for f in os.listdir(os.path.expanduser(path))]
	for i in range(len(files)):
		img.append(pygame.image.load(files[i]))
	actor = []
	for i in range(len(img)):
		actor.append(pygame.transform.scale(img[i],(60,100)))
Add_actor()

actor_id = random.randint(0,len(actor)-1)
mainer = actor[actor_id]

run = tele_main(False, 52, 200, 1, False, mainer, False)
def check_run():
	if run.go:
		run.run()
	run.update_run()
	run.draw_main()

# ground_1 = ground_1(52, 200, 1, False, False, False, False)

global fpsclock
fpsclock = pygame.time.Clock()

running = True

while running:
	screen.display.fill(color.blue)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		

		if run.drop == False:
			if event.type == pygame.KEYDOWN:
				if run.pause == False:
					if event.key == pygame.K_RIGHT:
						run.go = True
						run.derection = 1

					if event.key == pygame.K_LEFT:
						run.go =  True
						run.derection = -1

				if event.key == pygame.K_UP:
					if run.drump == False:
						run.update_drump(True)
						run.update_Up(run.y)
				if event.key == pygame.K_DOWN:
					run.down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				run.go = False
			if event.key == pygame.K_LEFT:
				run.go = False
			if event.key == pygame.K_DOWN:
				run.down = False

	check_run()
	if pygame.mixer.music.get_busy() == False:
		pygame.mixer.music.load("wii.mp3")
		pygame.mixer.music.play()

	# screen.display.blit(mainer, (run.x, run.y))

	pygame.display.update()
	fpsclock.tick(60)

pygame.quit()