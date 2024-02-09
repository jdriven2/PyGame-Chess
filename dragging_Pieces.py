# Python program to move the image
# with the mouse

# Import the library pygame
import pygame
from pygame.locals import *

# Take colors input
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Construct the GUI game
pygame.init()

# Set dimensions of game GUI
w, h = 640, 350
screen = pygame.display.set_mode((w, h))

# Take image as input
img = pygame.image.load(r"C:\Users\AC94359\Downloads\bishop1.png")
img.convert()


img2 = pygame.image.load(r"C:\Users\AC94359\Downloads\bishop1.png")
img2.convert()
# Draw rectangle around the image
rect = img.get_rect()
rect.center = w//2, h//2

rect2 = img2.get_rect()
rect2.center = w//3, h//2

# Set running and moving values
running = True
moving = False
moving2 = False
# Setting what happens when game 
# is in running state
while running:
	
	for event in pygame.event.get():

		# Close if the user quits the 
		# game
		if event.type == QUIT:
			running = False

		# Making the image move
		elif event.type == MOUSEBUTTONDOWN:
			if rect.collidepoint(event.pos):
				moving = True
			elif rect2.collidepoint(event.pos):
				moving2 = True

		# Set moving as False if you want 
		# to move the image only with the 
		# mouse click
		# Set moving as True if you want 
		# to move the image without the 
		# mouse click
		elif event.type == MOUSEBUTTONUP:
			moving = False
			moving2 = False

		# Make your image move continuously
		elif event.type == MOUSEMOTION and moving:
			rect.move_ip(event.rel)
			
		elif event.type == MOUSEMOTION and moving2:
			rect2.move_ip(event.rel)

	# Set screen color and image on screen
	screen.fill(YELLOW)
	screen.blit(img, rect)
	screen.blit(img2, rect2)

	# Construct the border to the image
	pygame.draw.rect(screen, BLUE, rect, 2)
	pygame.draw.rect(screen, RED, rect2, 2)

	# Update the GUI pygame
	pygame.display.update()

# Quit the GUI game
pygame.quit()
