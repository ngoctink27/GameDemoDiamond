import pygame

class stone(): # Bac da
	def __init__(self):
		self.img = pygame.image.load("./img/stone/island/5.png")
		self.stone_1 = pygame.transform.scale(self.img, (128,72))
		self.stone_2 = pygame.transform.scale(self.img, (430,80))
		self.stone_3 = pygame.transform.scale(self.img, (192,108))
		

		self.img_2 = pygame.image.load("./img/stone/island/1.png")
		self.stone_4 = pygame.transform.scale(self.img_2, (100,20))
		self.img_6 = pygame.image.load("./img/stone/island/2.png")
		self.stone_5 = pygame.transform.scale(self.img_6, (100,20))

		self.img_3 = pygame.image.load("./img/stone/island/6.png")
		self.stone_6 = pygame.transform.scale(self.img_3, (430,80))

		self.img_4 = pygame.image.load("./img/stone/island/7.png") # Thang day
		self.rope_1 = pygame.transform.scale(self.img_4, (65,300))

		self.img_5 = pygame.image.load("./img/stone/island/3.png") # Bac Thang
		self.rope_2 = pygame.transform.scale(self.img_5, (168,168))

class key(): # Chia khoa
	def __init__(self):
		self.img_1 = pygame.image.load("./img/key/2.png")
		self.key_1 = pygame.transform.scale(self.img_1, (80,80))

class draw():
	def __init__(self):
		self.display = pygame.display.set_mode((1280,720))
		self.icon = pygame.image.load("./icon/1.png")

	