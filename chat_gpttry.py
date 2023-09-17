import pygame

# Initialize Pygame and set up the game window
pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set the background color to yellow
background_color = (255, 255, 0)  # RGB values for yellow

# Fill the screen with the background color
window.fill(background_color)

# Run the game loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

# Quit Pygame
pygame.quit()
