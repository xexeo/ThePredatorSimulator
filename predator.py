#This file will maintain the predator class
from case_based_reason import Case_Based_Reasoning
from A_star import AStar

# Uses list of behaviour:
# 1 - Straight, Fast
# 2 - Straight, Slow
# 3 - Left, Fast
# 4 - Left, Slow
# 5 - Right, Fast
# 6 - Right, Slow

class Predator:
	def __init__(self, id, image, pos, window_size):
		## Parameters
		self.id = id
		self.speed = [2, 2]
		self.logic = Case_Based_Reasoning()
		self.route = AStar(window_size)
		## Imagery
		self.image = image
		self.rect = image.get_rect()
		self.rect = self.rect.move(pos)
		self.origRect = self.rect.copy()

	def select_logic(self, predCount, preyCount, match_percentage):
		tempBehaviour = 1
		self.case = self.logic.get_case(match_percentage, tempBehaviour, predCount, preyCount)
		while(self.case == False and tempBehaviour < 7):
			tempBehaviour += 1
			self.case = self.logic.get_case(match_percentage, tempBehaviour, predCount, preyCount)
			if (self.case != False):
				self.match = self.case
				self.case = self.case.get_result()
		if (self.case == True):
			print("Choice A")
			self.route.new_route(self.match.get_behaviour())
		else:
			print("Choice B")
			self.route.new_route(1)
		
	def update_speed(self, x, y):
		self.speed = [x, y]
	
	def move(self):
		self.rect = self.rect.move([0,0])
	
	def reset(self):
		self.rect = self.origRect.copy()
		
	def draw(self, screen):
		screen.blit(self.image, self.rect)
