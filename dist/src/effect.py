import random
import pygame
from src.background import draw

class bullet():
	def __init__(self, x1,x2,y1,y2,color):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.color = color
		self.bullet = []
		self.screen = draw()

	def update(self):
		for i in range(random.randint(0,2)):
			x = random.randint(self.x1,self.x2)
			y = random.randint(self.y1,self.y2)
			self.bullet.append((x,y))

	def draw(self):
		self.update()
		i = len(self.bullet)-1
		while i>=0:	
			pygame.draw.circle(self.screen.display, self.color, (self.bullet[i][0],self.bullet[i][1]), 2)
			self.bullet.pop(i)
			i-=1
