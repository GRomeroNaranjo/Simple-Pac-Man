# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the game window
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mini Pac-Man")

# Define the player block
player_size = 20
player_pos = [width // 2, height // 2]
player_color = RED

# Define walls (Just a simple example, you can expand this)
wall_color = BLUE
walls = [
    pygame.Rect(0, 0, width, 20),  # Top wall
    pygame.Rect(0, 0, 20, height),  # Left wall
    pygame.Rect(0, height - 20, width, 20),  # Bottom wall
    pygame.Rect(width - 20, 0, 20, height)  # Right wall
]

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Draw game objects
    screen.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(screen, wall_color, wall)
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit the game
pygame.quit()