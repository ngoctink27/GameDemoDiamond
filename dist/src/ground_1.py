import pygame
import math
import time
from src.background import draw
from src.background import stone, key
from src.colors import colors
from src.effect import bullet

class ground_1():
	# global drop,x1,y1
	def __init__(self, x, y, derection, go, xbool, ybool, down):
		self.x = x # Vi tri main
		self.y = y
		self.colors = colors()

		self.derection = derection # Huong di
		self.go = go
		self.drop = False
		self.pause = False  # Di xuong bac thang
		self.down = down	# Di xuong
		self.drump = False
		# self.angle = 0

		self.key = key()
		self.screen = draw()
		self.stone = stone()
		self.img_1 = pygame.image.load("./img/background/2.jpg")
		self.background = pygame.transform.scale(self.img_1, (1280,720))


		self.x1 = 285  		# Vi tri hon da roi
		self.y1 = 0
		self.over_1 = False

		self.x_stone4 = 450 		# Vi tri thanh ngang
		self.y_stone4 = 300
		self.derection_stone4 = 1 # Huong di thanh ngang
		self.x_stone5 = 20
		self.y_stone5 = 600

		self.countdown = 30
		self.xbool = xbool # Trang thai quay cua main
		self.ybool = ybool

		self.effect_1 = bullet(500,580,455,520, self.colors.white)
		self.unkey = False

		self.angle_rope2 = 0 # Goc quay cua cua thang
		self.down_1 = False
		self.down_2 = False
		self.down_3 = False
		self.down_4 = False
		self.ok_4 = False   # Kiem tra leo du 4 bac chua
		self.die_rope2 = 0
		self.countdown_rope2 = 40

		self.mainer = 0

		self.win = False

	def update(self):
		self.drop = False
		self.x = 52 
		self.y = 200
		self.y1 = 0 
		self.countdown = 30
		self.angle = 0
		self.xbool = False
		self.ybool = False
		self.unkey = False
		self.over_1 = False

		self.angle_rope2 = 0 # Goc quay cua cua thang
		self.down_1 = False
		self.down_2 = False
		self.down_3 = False
		self.down_4 = False
		self.ok_4 = False   # Kiem tra leo du 4 bac chua
		self.die_rope2 = 0
		self.countdown_rope2 = 40
		self.win = False


	def drop_1(self):
		if self.drop:
			self.go = False
			if self.y<800:
				self.y+=7
				self.xbool = True
				self.ybool = True
				# self.angle -=2
				# self.pause = True
			else: 
				self.update()
				# self.pause = False

	def check_out2(self):
		if (self.x >= 270 and self.x <= 400) and self.y1>=self.y:
			self.drop = True


	def drop_2(self): # Hon da roi
		if self.countdown>0:
			self.countdown -= 1

		if self.countdown==0:
			self.screen.display.blit(self.stone.stone_1, (self.x1, self.y1))
			if self.y1 < 230:
				self.y1 += 12
				self.check_out2()
	def drop_3(self):
		if (self.x>400 and self.x<=560) and self.y>=380:
			if self.y<540:
				self.y+=7
			else:
				self.y = 542
				self.down_4 = False
			
	def display_ground1(self):
		self.screen.display.blit(self.background, (0,0))
		self.screen.display.blit(self.stone.stone_1, (50, 300))
		self.screen.display.blit(self.stone.stone_3, (250, 300))

		# Thanh ngang di chuyen
		if self.derection_stone4 == 1:
			if self.x_stone4 < 700:
				self.x_stone4 +=2
			else:
				self.derection_stone4 =-1
		else:
			if self.x_stone4 > 450:
				self.x_stone4 -=2
			else:
				self.derection_stone4 = 1

		self.screen.display.blit(self.stone.stone_4, (self.x_stone4, self.y_stone4))
		self.screen.display.blit(self.stone.stone_2, (820, 300))
		self.screen.display.blit(self.stone.rope_1, (1150,330))

		# Cham vao chia khoa
		if self.unkey == False:
			self.screen.display.blit(self.key.key_1, (500,470))
			self.effect_1.draw()
		# Rotate Rope_2
		if self.die_rope2 == 0:
			yolo = pygame.transform.rotate(self.stone.rope_2, self.angle_rope2)
			self.screen.display.blit(yolo, (595, 480))
			
		else: 
			if self.die_rope2 == 1:
				self.angle_rope2 = 0
				yolo = pygame.transform.rotate(self.stone.rope_2, 90)
				self.screen.display.blit(yolo, (430, 480))
				if self.x>=430 and self.y>=520:
					self.drop = True

			else:
				if self.die_rope2 == 2:
					self.angle_rope2 = 0
					yolo = pygame.transform.rotate(self.stone.rope_2, 225)
					self.screen.display.blit(yolo, (230, 500))
					if self.x>=220 and self.y>=520:
						self.drop = True
		
		if self.unkey:
			self.screen.display.blit(self.stone.stone_5, (self.x_stone5, self.y_stone5))


	def reach_key(self):
		if self.down_4:
			self.drop_3()
		if self.x>=500 and self.x<=570:
			if self.y>=490 and self.y<=530:
				self.unkey = True



	# Leo cau thang
	def up_rope2(self): 
		# self.screen.display.blit(self.mainer, (710, 500))
		if self.y<=543 and self.y>505:
			if self.x<760 and self.x>=730:
				self.x = 760
		else:
			# Bac 1
			if self.x<730 and self.x>=695:
				if self.y>500:
					self.y = 500
					self.drump = False
					self.down_1 = True
			if self.y<=501 and self.y>=480:
				if self.x<700 and self.x>570:
					self.x = 700
			if self.down_1:
				if self.y == 500 and (self.x>751 and self.x<=830):
					self.y += 42
					self.down_1 = False

			# Bac 2
			if self.x<690 and self.x>=645:
				if self.y>460:
					self.y = 460
					self.drump = False
					self.down_2 = True
			if self.y<=461 and self.y>=430:
				if self.x<655 and self.x>570:
					self.x = 655
			if self.down_2:
				if self.y == 460 and (self.x>=693 and self.x<=830):
					self.y += 40
					self.down_2 = False

			# Bac 3
			if self.x<650 and self.x>=610:
				if self.y>420:
					self.y = 420
					self.drump = False
					self.down_3 = True
			if self.y<=421 and self.y>=400:
				if self.x<615 and self.x>570:
					self.x = 615
			if self.down_3:
				if self.y == 420 and (self.x>=650 and self.x<=830):
					self.y += 40
					self.down_3 = False

			# Bac 4
			if self.ok_4 == False:
				if self.x<610 and self.x>=570:
					if self.y>380:
						self.y = 380
						self.drump = False
						self.down_4 = True
				# print(self.x, self.y)
				if self.y<=381 and self.y>=360:
					if self.x<585 and self.x>450:
						self.x = 585
						self.ok_4 = True
			if self.down_4:
				if self.y == 380 and (self.x>=612 and self.x<=830):
					self.y += 40
					self.down_4 = False
					self.ok_4 = False
			# print(self.down_4)
		if self.ok_4:
			if self.y>=379 and self.y<=543:
				if self.x>560:
					self.x = 560
	def rotate_rope2(self):
		if self.die_rope2<2:
			if self.countdown_rope2 == 0:
				self.die_rope2 =self.die_rope2+1
				self.countdown_rope2 = 40
			else:
				self.countdown_rope2 -=1
	def up_stone5(self):

 		if self.y_stone5>=200:
 			self.y_stone5 -=3
 			self.y -=3
	def run_ground1(self):
		self.display_ground1()
		# Drop
		if self.y == 200 and self.x <=20 :
			self.drop = True

		if self.y == 200 and (self.x >= 150 and self.x <= 225):
			self.drop = True
		
		if self.y == 200 and (self.x >= 270 and self.x <= 400):
			self.drop_2()

		if self.y == 200 and (self.x >= 410 and self.x<=800):
			if self.x<=self.x_stone4-30 or self.x>=self.x_stone4+80:
				self.drop = True
			else:
				self.x += 2*self.derection_stone4

		if self.x >= 1130 and self.x<=1190:
			if self.down:
				if self.y<540:
					self.y +=3
					self.pause = True
				else:
					self.pause = False
					self.over_1 = True
		if self.over_1 and self.drop==False:
			self.up_rope2()
			self.reach_key()
			# if self.angle_rope2 <224:
			# self.angle_rope2 +=1
			if self.unkey:
				self.rotate_rope2()
				# self.up_stone5()

		# font_out = pygame.font.SysFont('comicsansms', 80)
		# text_6 = font_out.render('Perfect!', True, (255,0,0) )
		# self.screen.display.blit(text_6, (500,200))
		if self.y >=540 and self.x <=100:
			self.win = True

		if self.win:
			font_out = pygame.font.SysFont('comicsansms', 80)
			text_6 = font_out.render('Perfect!', True, (255,0,0) )
			self.screen.display.blit(text_6, (500,200))
			pygame.mixer.music.stop()
			pygame.mixer.music.load("pdvs.mp3")
			pygame.mixer.music.play()
			self.win = False

		self.drop_1()