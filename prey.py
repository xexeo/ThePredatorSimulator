#This file will maintain the prey class
import sys

class Prey(object):
	def __init__(self, image, pos):
		## Parameters
		self.speed = [1,1]
		self.nearby_pred = (0,0,0,0)
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
		if (self.nearby_pred != (0,0,0,0)):
			dir1 = self.speed[0]
			dir2 = self.speed[1]
			orig_pos = self.rect
			if (orig_pos[0] < self.nearby_pred[0]):
				dir1 = self.speed[0] * -1
			elif(orig_pos[0] == self.nearby_pred[0]):
				dir1 = 0
			if (orig_pos[1] < self.nearby_pred[1]):
				dir2 = self.speed[1] * -1
			elif(orig_pos[1] == self.nearby_pred[1]):
				dir2 = 0
			self.rect = self.rect.move((dir1, dir2))
	
	def check_nearby(self, predator):
		pred_pos = predator.get_pos()
		if (self.check_collision((pred_pos[0], pred_pos[1], 200, 200), self.rect)):
			self.nearby_pred = pred_pos
	
	def check_collision(self, obj1, obj2):
		if((obj1[0] + obj1[2]) > obj2[0] and (obj1[1] + obj1[3]) > obj2[1] and
		obj1[0] < (obj2[0] + obj2[2]) and obj1[1] < (obj2[1] + obj2[3])):
			return True
		return False
	
	def reset(self):
		self.rect = self.origRect.copy()
		self.nearby_pred = (0,0,0,0)
		
	def draw(self, screen):
		screen.blit(self.image, self.rect)
