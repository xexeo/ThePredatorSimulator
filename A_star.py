#This class is designed to handle the A* path finding algorithm
import sys

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
		while (x <= (window_size[0]*2)):
			y = 0
			while (y <= (window_size[1]*2)):
				self.nodes.append(self.Node(x, y, self.diff))
				y += self.diff
			x += self.diff
			
	def new_route(self, orig_pos, behaviour):
		# Generate list of nodes (Route to use)
		self.behaviour = behaviour
		#Switch Behaviour: goal = position
		if (behaviour == 1 or behaviour == 2):
			goal = (320, 440, 0, 0) # Depends on pos - may need to move accordingly
		elif (behaviour == 3 or behaviour == 4):
			goal = (40, 220, 0, 0)
		else:
			goal = (600, 220, 0, 0)
		# Use behaviour to determine goal
		self.route = self.find_quickest_route(orig_pos, goal)
		print ("Route contains " + str(len(self.route)-1) + " routes")
		sys.stdout.flush()
	
	def find_quickest_route(self, orig_pos, goal):
		move = 1 
		route = []
		nearest_nodes = self.find_nearest_nodes(orig_pos) # Return nearest nodes
		new_node = self.best_node(goal, move, nearest_nodes) # Add it
		route.append(new_node[1])
		# While dist = 0 (Score = current move)
		while (new_node[0] != move):
			move += 1
			length = (len(route)-1)
			newest_node = (route[length].get_pos()[0], route[length].get_pos()[1], orig_pos[2], orig_pos[3])
			nearest_nodes = self.find_nearest_nodes(newest_node) # Return nearest nodes to latest node
			new_node = self.best_node(goal, move, nearest_nodes) # Add it
			route.append(new_node[1])
		return route
	
	def best_node(self, goal, move, nodes):
		tempList = 0	
		for node in nodes:
			pos = node.get_pos()
			x = (pos[0] - goal[0])
			if (x < 0):
				x = x * -1 # Turn from negative to positive
			y = (pos[1] - goal[1])
			if (y < 0):
				y = y * -1 # Turn from negative to positive
			score = ((x + y) + move)
			if (tempList == 0):
				tempList = ((score, node))
			elif (score < tempList[0]):
				tempList = ((score, node))
		if (tempList == 0):
			print("Major error: No nearby nodes registered for pos " + str(node.get_pos()))
		tempList = self.check_small_dist(goal, move, tempList)
		return tempList
	
	# Check if distance is small
	def check_small_dist(self, goal, move, tempList):
		Yclose = False
		Xclose = False
		x = tempList[1].get_pos()[0]
		y = tempList[1].get_pos()[1]
		if (x - goal[0] < 0):
			if ((x - goal[0])*-1 < (self.diff - 1)):
				Xclose = True
		elif (x - goal[0] < (self.diff - 1)):
			Xclose = True
		if (y - goal[1] < 0):
			if ((y - goal[1])*-1 < (self.diff - 1)):
				Yclose = True
		elif (y - goal[1] < (self.diff - 1)):
			Yclose = True
		if (Xclose and Yclose):
			tempNode = self.Node(goal[0], goal[1], self.diff)
			return ((move, tempNode))
		return tempList
	
	def find_nearest_nodes(self, orig_pos):
		tempList = []
		for node in self.nodes:
			pos = node.get_pos()
			if (check_collision((pos[0], pos[1], 30, 30), orig_pos)):
				tempList.append(node)
		return tempList
	
	def nearest_prey(self, prey, orig_pos):
		print("Arrived at destination! Hunting prey!")
		sys.stdout.flush()
		# Find nearest prey in list
		closest_prey = self.best_node(orig_pos, 0, prey)
		# New route to closest prey
		self.route = self.find_quickest_route(orig_pos, closest_prey[1].get_pos())
		
	def move_to_node(self, orig_pos, speed, prey):
		# Return direction to next node
		if (len(self.route) > 0):
			pos = self.route[0].get_pos()
			if (len(self.route) > 1):
				if (orig_pos[0] == pos[0] and orig_pos[1] == pos[1]):
					print("Reached node " + str(len(self.route)-1) + " " + str(pos))
					sys.stdout.flush()
					self.route.remove(self.route[0])
				pos = self.route[0].get_pos()
			dir1 = speed[0]
			dir2 = speed[1]
			if (orig_pos[0] > pos[0]):
				dir1 = speed[0] * -1
			elif(orig_pos[0] == pos[0]):
				dir1 = 0
			if (orig_pos[1] > pos[1]):
				dir2 = speed[1] * -1
			elif(orig_pos[1] == pos[1]):
				dir2 = 0
			if ((dir1, dir2) == (0, 0) and len(self.route) == 1):
				self.nearest_prey(prey, orig_pos)
				return self.move_to_node(orig_pos, speed, prey) # Re-run for new nodes
			return (dir1, dir2)
		return (0, 0)

def check_collision(obj1, obj2):
	if((obj1[0] + obj1[2]) > obj2[0] and (obj1[1] + obj1[3]) > obj2[1] and
	obj1[0] < (obj2[0] + obj2[2]) and obj1[1] < (obj2[1] + obj2[3])):
		return True
	return False		