#This file will maintain the prey class
class Prey(object):
	def __init__(self, id, image, pos):
		## Parameters
		self.id = id
		self.speed = [0, 0]
		## Imagery
		self.image = image
		self.rect = image.get_rect()
		self.rect = self.rect.move(pos)
	
	def update_speed(self, x, y):
		self.speed = [x, y]

	def move(self):
		self.rect = self.rect.move(self.speed)
	
	def draw(self, screen):
		screen.blit(self.image, self.rect)
