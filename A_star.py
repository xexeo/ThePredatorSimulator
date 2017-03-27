#This class is designed to handle the A* path finding algorithm

class AStar(object):
	def __init__(self):
		# Nothing to initalise yet
		self.behaviour = 0
	
	def new_route(self, behaviour):
		self.behaviour = behaviour