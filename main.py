#The file will hold all the main methods and bring the program together
# Additional files
from predator import Predator
from prey import Prey

# GUI
import sys 
import pygame
pygame.init()

# Global Variables
window_size = width, height = 640, 480
screen = pygame.display.set_mode(window_size)
screen_colour = 34, 177, 76
my_font = pygame.font.SysFont("monospace", 16)

preyList = [] # List of Prey
predList = [] # List of Predators
labels = [] # List of Labels
buttons = [] # List of Buttons

def init():
	#Load Window
	pygame.display.set_caption('The Predator Simulator')
	pygame.mouse.set_visible(1) #Debateable on whether it's neccesary
	# Load Assets
	## Objects
	preyList.append(Prey(1, pygame.image.load("images/prey.png").convert(), [10, 10]))
	predList.append(Predator(1, pygame.image.load("images/predator.png").convert(), [10, 420]))
	## Labels
	labels.append(Label("#Simulation 1", (480, 380)))
	labels.append(Label("Prey:       " + str(len(preyList)), (480, 400)))
	labels.append(Label("Predators:  " + str(len(predList)), (480, 420)))
	# Buttons
	buttons.append(Button("Start", (480,450)))
	
def logic(simulation):
	# Logic
	for predator in predList:
		predator.move()
	for prey in preyList:
		prey.move()
		
def draw():
	# Render
	## Draw order
	screen.fill(screen_colour)
	### Objects
	for predator in predList:
		predator.draw(screen)
	for prey in preyList:
		prey.draw(screen)
	for label in labels:
		label.draw(screen)
	for button in buttons:
		button.draw(screen)
	## Actual Draw
	pygame.display.update()
	pygame.time.delay(33) # AVG 30FPS
		
def main():	
	running = True
	simulation = 1
	init()
	
	while(running):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if (check_collision((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1), buttons[0].get_pos())):
					# Technically start game
					for prey in preyList:
						prey.update_speed(1, 1)
					predList[0].select_logic(len(predList), len(preyList))
			if event.type == pygame.QUIT: 
				# Stops the program running
				sys.exit()
				running = False
		logic(simulation)
		if(check_end_condition()):
			simulation = next_simulation(simulation)

		draw()

class Label(object):
	def __init__(self, text, pos):
		self.pos = pos
		self.obj = my_font.render(text, 1, (0,0,0))
	
	def update(self, text):
		self.obj = my_font.render(text, 1, (0,0,0))
	
	def draw(self, screen):
		screen.blit(self.obj, self.pos)
		
class Button(object):
	def __init__(self, text, pos):
		size = len(text)*20
		self.text = my_font.render(text, 1, (0,0,0))
		self.pos = (pos[0]+(size/4), pos[1])
		self.rect = (pos[0],pos[1],size,20)
	
	def get_pos(self):
		return self.rect
	
	def draw(self, screen):
		pygame.draw.rect(screen, (212,208,200), self.rect)
		pygame.draw.rect(screen, (0,0,0), self.rect, 2)
		screen.blit(self.text, self.pos)
		
def check_collision(obj1, obj2):
	if((obj1[0] + obj1[2]) > obj2[0] and (obj1[1] + obj1[3]) > obj2[1] and
	obj1[0] < (obj2[0] + obj2[2]) and obj1[1] < (obj2[1] + obj2[3])):
		return True
	return False

def check_end_condition():
	for prey in preyList:
		temp_pos = prey.get_pos()
		if (temp_pos[0] > 0 and temp_pos[1] > 0 and 
		temp_pos[0] < window_size[0] and temp_pos[1] < window_size[1]):
			return False
	return True

def next_simulation(simulation):
	labels[0].update("#Simulation " + str(simulation + 1)) # Move when required
	for prey in preyList:
		prey.reset()
	return simulation + 1
	
main()