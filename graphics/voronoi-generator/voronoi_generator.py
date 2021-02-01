# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Voronoi Generator")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((640,480))
     
    # define a variable to control the main loop
    running = True

    # constants
    DOT_COLOR =         (255,255,255)
    BACKGROUND_COLOR =  (  0,  0,  0)
    CIRCLE_SIZE =       3
    BOUNDING_BOX_SIZE = 6

    # globals
    index_of_moved_dot = None
    list_of_points = []
    mouse_released = True
    most_recent_circle_pos = ()
    most_recent_bounding_box = None
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_mouse_pos = pygame.mouse.get_pos()
                print(current_mouse_pos)
                point_exists = False
                for i in range(len(list_of_points)):
                    # print(list_of_points[i], sep=", ")
                    if list_of_points[i].collidepoint(current_mouse_pos):
                        most_recent_bounding_box = list_of_points[i]
                        most_recent_circle_pos = list_of_points[i].center
                        index_of_moved_dot = i
                        point_exists = True
                if not point_exists:
                    # make a new point!
                    most_recent_circle_pos = current_mouse_pos
                    most_recent_bounding_box = pygame.Rect(
                                most_recent_circle_pos[0] - BOUNDING_BOX_SIZE/2,
                                most_recent_circle_pos[1] - BOUNDING_BOX_SIZE/2, 
                                BOUNDING_BOX_SIZE,
                                BOUNDING_BOX_SIZE)
                    pygame.draw.circle(screen, DOT_COLOR, most_recent_circle_pos, CIRCLE_SIZE)
                    pygame.display.flip()
                    mouse_released = False
            if event.type == pygame.MOUSEMOTION:
                if not mouse_released:
                    previous_circle_pos = most_recent_circle_pos
                    most_recent_circle_pos = pygame.mouse.get_pos()
                    # first, clear old location
                    pygame.draw.circle(screen, BACKGROUND_COLOR, previous_circle_pos, CIRCLE_SIZE)
                    # then draw new dot
                    print(most_recent_circle_pos)
                    most_recent_bounding_box.move_ip(most_recent_circle_pos[0] - previous_circle_pos[0],
                                                     most_recent_circle_pos[1] - previous_circle_pos[1])
                    pygame.draw.circle(screen, DOT_COLOR, most_recent_circle_pos, CIRCLE_SIZE)
                    pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONUP:
                if point_exists:
                    list_of_points[index_of_moved_dot] = most_recent_bounding_box
                else:
                    list_of_points.append(most_recent_bounding_box)
                mouse_released = True
                print(list_of_points)
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()