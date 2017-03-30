#This class is designed to handle the A* path finding algorithm

class AStar(object):
	class Node(object):
		def __init__(self, x, y):
			self.x = x
			self.y = y
		
		def get_pos(self):
			return (self.x, self.y)
			
	def __init__(self, window_size):
		# Nothing to initalise yet
		self.behaviour = 0
		self.nodes = []
		self.route = []
		self.diff = 20
		x = 0
		while (x <= window_size[0]):
			y = 0
			while (y <= window_size[1]):
				self.nodes.append(self.Node(x, y))
				y += self.diff
			x += self.diff
			
	def new_route(self, behaviour):
		# Generate list of nodes (Route to use)
		self.behaviour = behaviour
		
	def move_to_node(self, x, y):
		# Return direction to next node
		if (len(self.route) > 0):
			pos = route[0].get_pos()
			if (len(self.route) > 1):
				if (x == pos[0] and y == pos[1]):
					self.route.remove(self.route[0])
				pos = route[0].get_pos()
			dir1 = 1
			dir2 = 1
			if (x < pos[0]):
				dir1 = -1
			elif(x == pos[0]):
				dir1 = 0
			if (y < pos[1]):
				dir2 = -1
			elif(y == pos[1]):
				dir2 = 0
			return (dir1, dir2)
				