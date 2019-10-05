import colorsys
import pygame
from random import shuffle

#mine 
import sorting_algorithms

values = [i for i in range(361)]
shuffle(values)
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (1200, 920)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Drawing Lines")
 
# clock is used to set a max fps
clock = pygame.time.Clock()
 
# create a demo surface 
surface_size = (1200, 920)
test_surface = pygame.Surface(surface_size)
test_surface.fill(BLACK)

# draw a red line across it
max_x = surface_size[0]
max_y = surface_size[1]
# pygame.draw.aaline(test_surface, RED, (0, surface_size[1]), (surface_size[0], 0))
# pygame.draw.aaline(test_surface, RED, (100, max_y - 100), (max_x - 100, max_y
# - 100))

def draw_lines(values: [int]):
    y = surface_size[1] - 100
    for i in range(361):
        # scale = 2
        line_length = 721 - values[i]*2
        line_thickness = 2
        line_color = pygame.Color(0,0,0)
        line_color.hsva = (values[i], 50, 50, 0)

        center_x = int(surface_size[0]/2)
        x = center_x - int(line_length/2)

        pygame.draw.rect(
            test_surface,
            line_color,
            pygame.Rect((x, y), (line_length, line_thickness)),
            0
        )
        y -= line_thickness


n = len(values)
draw_lines(values)
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    # screen.fill(BLACK)
    test_surface.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    sorting_algorithms.selection_sort_step(values, n)
    n -= 1
    draw_lines(values)
    # END MY CODE
    x = (screen_size[0]/2) - (surface_size[0]/2)
    y = (screen_size[1]/2) - (surface_size[1]/2)
    screen.blit(test_surface, (x, y))
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()