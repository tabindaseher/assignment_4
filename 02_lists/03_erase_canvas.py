import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600  # Canvas size
CELL_SIZE = 40  # Size of each cell (rectangles)
ERASER_SIZE = 40  # Size of the eraser (same size as a cell)

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Canvas with Eraser')

# Create the grid of blue cells
grid = [[BLUE for _ in range(WIDTH // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)]

# Create the eraser's initial position (top-left corner)
eraser_rect = pygame.Rect(100, 100, ERASER_SIZE, ERASER_SIZE)

# Function to draw the grid
def draw_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            pygame.draw.rect(screen, grid[row][col], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)  # Cell borders

# Function to update the grid based on the eraser's position
def erase_cells():
    eraser_x, eraser_y = eraser_rect.topleft
    start_col = eraser_x // CELL_SIZE
    start_row = eraser_y // CELL_SIZE
    end_col = (eraser_x + ERASER_SIZE) // CELL_SIZE
    end_row = (eraser_y + ERASER_SIZE) // CELL_SIZE

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
                grid[row][col] = WHITE

# Main loop
running = True
dragging = False
while running:
    screen.fill(WHITE)  # Fill the screen with white background
    
    draw_grid()  # Draw the grid
    pygame.draw.rect(screen, (255, 0, 0), eraser_rect)  # Draw the eraser (red color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if eraser_rect.collidepoint(event.pos):
                dragging = True  # Start dragging the eraser if clicked inside
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False  # Stop dragging the eraser
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                eraser_rect.topleft = event.pos  # Move the eraser with the mouse
                # Ensure the eraser stays within bounds
                if eraser_rect.left < 0:
                    eraser_rect.left = 0
                if eraser_rect.top < 0:
                    eraser_rect.top = 0
                if eraser_rect.right > WIDTH:
                    eraser_rect.right = WIDTH
                if eraser_rect.bottom > HEIGHT:
                    eraser_rect.bottom = HEIGHT
                erase_cells()  # Erase cells under the eraser

    pygame.display.flip()  # Update the screen

# Quit pygame
pygame.quit()
sys.exit()
