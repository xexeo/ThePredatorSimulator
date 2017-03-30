#This file will maintain the prey class
class Prey(object):
	def __init__(self, image, pos):
		## Parameters
		self.speed = [0, 0]
		## Imagery
		self.image = image
		self.rect = image.get_rect()
		self.rect = self.rect.move(pos)
		self.origRect = self.rect.copy()
	
	def get_pos(self):
		return self.rect
		
	def update_speed(self, x, y):
		self.speed = [x, y]

	def move(self):
		self.rect = self.rect.move(self.speed)
	
	def reset(self):
		self.rect = self.origRect.copy()
		
	def draw(self, screen):
		screen.blit(self.image, self.rect)
