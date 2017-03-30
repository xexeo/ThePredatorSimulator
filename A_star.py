#This class is designed to handle the A* path finding algorithm

class AStar(object):
	class Node(object):
		def __init__(self, x, y, size):
			self.x = x
			self.y = y
			self.max_x = x + size
			self.max_y = y + size
		
		def get_pos(self):
			return (self.x, self.y)
			
	def __init__(self, window_size):
		# Nothing to initalise yet
		self.behaviour = 0
		self.nodes = []
		self.route = []
		# This should create a grid like basis
		self.diff = 20
		x = 0
		while (x <= window_size[0]):
			y = 0
			while (y <= window_size[1]):
				self.nodes.append(self.Node(x, y, self.diff))
				y += self.diff
			x += self.diff
			
	def new_route(self, orig_pos, behaviour):
		# Generate list of nodes (Route to use)
		self.behaviour = behaviour
		#Switch Behaviour: goal = position
		
		# Use behaviour to determine goal
		print(orig_pos)
		#self.route = self.score_nodes(orig_pos, goal)
		#for node in tempList:
		#	print(node.get_pos())
	
	def score_nodes(self, orig_pos, goal):
		route = []
		nearest_nodes = self.find_nearest_nodes(orig_pos) # Return nearest nodes
		# While not at goal
		return route
		
	def find_nearest_nodes(self, orig_pos):
		tempList = []
		for node in self.nodes:
			pos = node.get_pos()
			# Need to refine below - as incorrect
			if ((orig_pos[0] + self.diff) < pos[0] and (pos[0] - self.diff) > orig_pos[0] and
			(orig_pos[1] + self.diff) < pos[1] and (pos[1] - self.diff) > orig_pos[1]):
				tempList.append(node)
		return tempList
	
	def nearest_prey(self, prey, orig_pos):
		# Find nearest prey in list
		for closest in prey:
			# if closest (Not sure how to do this yet)
			self.route = score_nodes(orig_pos, closest.get_pos())
	
	def move_to_node(self, orig_pos, speed):
		# Return direction to next node
		if (len(self.route) > 0):
			pos = route[0].get_pos()
			if (len(self.route) > 1):
				if (orig_pos[0] == pos[0] and orig_pos[1] == pos[1]):
					self.route.remove(self.route[0])
				pos = route[0].get_pos()
			dir1 = speed[0]
			dir2 = speed[1]
			if (orig_pos[0] < pos[0]):
				dir1 = -speed[0]
			elif(orig_pos[0] == pos[0]):
				dir1 = 0
			if (orig_pos[1] < pos[1]):
				dir2 = -speed[1]
			elif(orig_pos[1] == pos[1]):
				dir2 = 0
			return (dir1, dir2)
		return (0, 0)		