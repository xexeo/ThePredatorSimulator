#This file will maintain the predator class
from case_based_reason import Case_Based_Reasoning
from A_star import AStar

import sys

# Uses list of behaviour:
# 1 - Straight, Slow
# 2 - Straight, Fast
# 3 - Left, Slow
# 4 - Left, Fast
# 5 - Right, Slow
# 6 - Right, Fast

class Predator:
	def __init__(self, image, pos, window_size):
		## Parameters
		self.speed = [1,1]
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
		if (self.case):
			self.result = self.case.get_result()
			while(self.result == False and tempBehaviour < 7):
				tempBehaviour += 1
				self.tempCase = self.logic.get_case(match_percentage, tempBehaviour, predCount, preyCount)
				if (self.tempCase == False):
					self.case.behaviour = tempBehaviour
					tempBehaviour = 7
				elif (self.tempCase.get_behaviour() != tempBehaviour):
					self.case.behaviour = tempBehaviour
					tempBehaviour = 7
				elif (self.tempCase.get_result()):
					self.case = self.tempCase
					self.result = self.case.get_result()
			if (self.result == True):
				print("Found a previous case! Behaviour: " + str(self.case.get_behaviour()))
				self.route.new_route(self.rect, self.case.get_behaviour())
				self.behaviour = self.case.get_behaviour()
			else:
				print("Found a previous case but was a fail! Trying behaviour " + str(self.case.get_behaviour()))
				tempBehaviour = (self.case.get_behaviour())
				self.route.new_route(self.rect, tempBehaviour)
				self.behaviour = tempBehaviour
		else:
			print("No case found! Let's see how this goes")
			self.route.new_route(self.rect, 1)
			self.behaviour = 1
		if (self.behaviour == 2 or self.behaviour == 4 or self.behaviour == 6):
			self.update_speed(2, 2)
		else:
			self.update_speed(1, 1)
		sys.stdout.flush()
	
	def get_pos(self):
		return self.rect
	
	def update_speed(self, x, y):
		self.speed = [x, y]

	def add_new_case(self, predCount, preyCount, result):
		self.logic.add_case(self.behaviour, preyCount, predCount, result)
		
	def move(self, prey):
		self.rect = self.rect.move(self.route.move_to_node(self.rect, self.speed, prey))
			
	def reset(self, predLen, preyLen, match_percentage):
		self.rect = self.origRect.copy()
		self.select_logic(predLen, preyLen, match_percentage)
		
	def draw(self, screen):
		screen.blit(self.image, self.rect)
