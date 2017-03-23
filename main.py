#The file will hold all the main methods and bring the program together
# Additional files
from predator import Predator
from prey import Prey

# GUI
import sys, pygame
pygame.init()

# Global Variables
window_size = width, height = 640, 480
my_font = pygame.font.SysFont("monospace", 16)

def run():	
	# Load window
	running = True
	screen_colour = 34, 177, 76
	screen = pygame.display.set_mode(window_size)
	pygame.display.set_caption('The Predator Simulator')
	pygame.mouse.set_visible(1) #Debateable on whether it's neccesary
	# Load Logic Variables
	simulation = 1
	prey_count = 1
	pred_count = 1
	# Load Assets
	## Objects
	prey1 = Prey(1, pygame.image.load("images/prey.png").convert(), [10, 10])
	predator1 = Predator(1, pygame.image.load("images/predator.png").convert(), [10, 420])
	start = Button("Start", (480,450))
	## Text
	sim_label = my_font.render("#Simulation " + str(simulation), 1, (0,0,0))
	prey_label = my_font.render("Prey:       " + str(prey_count), 1, (0,0,0))
	pred_label = my_font.render("Predators:  " + str(pred_count), 1, (0,0,0))
	
	while(running):
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if (check_collision(pygame.mouse.get_pos(), start.get_pos())):
					# Technically start game
					prey1.update_speed(1, 1)
			if event.type == pygame.QUIT: 
				# Stops the program running
				sys.exit()
				running = False
		
		# Logic
		predator1.move()
		prey1.move()
		# Render
		## Draw order
		screen.fill(screen_colour)
		### Objects
		prey1.draw(screen)
		predator1.draw(screen)
		### Labels
		screen.blit(sim_label, (480, 380))
		screen.blit(prey_label, (480, 400))
		screen.blit(pred_label, (480, 420))
		start.draw(screen)
		## Actual Draw
		pygame.display.update()
		pygame.time.delay(33) # AVG 30FPS
		

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
	if(obj1[0] > obj2[0] and obj1[1] > obj2[1] and
	obj1[0] < (obj2[0] + obj2[2]) and obj1[1] < (obj2[1] + obj2[3])):
		return True
	return False
		
run()