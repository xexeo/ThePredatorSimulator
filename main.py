#The file will hold all the main methods and bring the program together
# Additional files
from predator import Predator
from prey import Prey

# GUI
import sys, pygame
pygame.init()

def run():
	running = True
	#prey1 = Prey(1, pygame.image.load("images/prey.png"))
	prey_test = pygame.image.load("images/prey.png")
	prey_test_rect = prey_test.get_rect()
	
	# Load window
	window_size = width, height = 640, 480
	screen_colour = 34, 177, 76
	screen = pygame.display.set_mode(window_size)
	pygame.display.set_caption('The Predator Simulator')
	pygame.mouse.set_visible(0) #Debateable on whether it's neccesary
	
	while(running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				# Stops the program running
				sys.exit()
				running = False
		
		screen.fill(screen_colour)
		screen.blit(prey_test, prey_test_rect)
		pygame.display.flip()
		
run()