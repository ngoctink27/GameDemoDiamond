import pygame

from src.ground_1 import ground_1
from src.background import draw

pygame.init()


class tele_main(): # nhan vat di chuyen
	
	def __init__(self,drump, x,y,derection, go, mainer, down):
		self.x = x 		# Vi tri main
		self.y = y		# Vi tri main
		self.derection = derection # Huong di
		self.drump = drump 	 # Trang thai nhay	
		self.step = 4
		self.upmax = False   # da cham max chua
		self.go = go 		
		self.queueUp = 0 	 # Vi tri nhay
		self.drop = False    # trang thai Drop
		self.down = down
		# self.pause = False

		self.xbool = False
		self.ybool = False
		self.angle = 5
		self.mainer = mainer

		self.ground1 = ground_1(x,y,derection,go,self.xbool, self.ybool, self.down)
		self.screen = draw()


	def update_Up(self,y):
		self.queueUp = y

	def update_drump(self,drump):
		self.drump = drump
		
	def run(self):
		# if self.pause == False:
		
		if self.derection == 1: # Go RIGHT
			self.x += self.step
			self.xbool = False
			self.ybool = False
			if self.x >=1200:
				self.x = 1200

		if self.derection == -1: # Go LEFT
			self.xbool = True
			self.ybool = False
			self.x -= self.step
			if self.x <=0:
				self.x = 0

	def drumps(self): 		# Drump

		if self.drump:
			# print(self.queueUp)
			if self.upmax == False:
				if self.y>self.queueUp-60:
					self.y -= 3	
				else:
					self.upmax = True
			else:
				if self.y < self.queueUp:
					self.y += 3
				else:
					self.upmax = False
					self.drump = False
		else:
			 self.upmax = False

	def update_run(self):
		self.ground1.x = self.x
		self.ground1.y = self.y
		self.ground1.derection = self.derection
		self.ground1.go = self.go
		self.ground1.down = self.down
		self.ground1.mainer = self.mainer
		self.ground1.drump = self.drump
		self.ground1.xbool = self.xbool
		self.ground1.ybool = self.ybool

		self.ground1.run_ground1()

		self.x = self.ground1.x
		self.y = self.ground1.y
		self.go = self.ground1.go
		self.drop = self.ground1.drop
		self.xbool = self.ground1.xbool
		self.ybool = self.ground1.ybool
		# self.angle = self.ground1.angle
		self.pause = self.ground1.pause 
		self.drump = self.ground1.drump

		if self.drop == False:
			self.drumps()

	def draw_main(self):
		self.mainer1 =  pygame.transform.flip(self.mainer, self.xbool, self.ybool)
		self.screen.display.blit(self.mainer1, (self.x, self.y))

