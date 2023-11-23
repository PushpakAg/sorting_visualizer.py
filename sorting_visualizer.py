import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ARRAY_SIZE = 50
DELAY = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

# Generate random array
array = [random.randint(50, 500) for _ in range(ARRAY_SIZE)]
bar_width = WIDTH // ARRAY_SIZE

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_array(arr, [j, j + 1], RED)
                time.sleep(DELAY / 1000)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            draw_array(arr, [j, j + 1], RED)
            time.sleep(DELAY / 1000)
        arr[j + 1] = key

def draw_array(arr, highlighted=None, color=BLUE):
    screen.fill(WHITE)
    for i, value in enumerate(arr):
        rect = pygame.Rect(i * bar_width, HEIGHT - value, bar_width, value)
        draw_color = color if highlighted is None or i in highlighted else BLACK
        pygame.draw.rect(screen, draw_color, rect)
    pygame.display.flip()


# Choose a sorting algorithm (uncomment one)
# sorting_algorithm = bubble_sortq
sorting_algorithm = insertion_sort

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sorting_algorithm(array)

    # Draw the final state in green
    draw_array(array, color=GREEN)
    time.sleep(2)

# Quit Pygame
pygame.quit()
