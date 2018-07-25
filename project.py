import pygame
import time

clock = pygame.time.Clock()
fps = 24
time_passed = clock.tick(fps)

LEFT = 1
magenta = (255, 0, 255)

running = 1
screen = pygame.display.set_mode((500,500))


def make_square(x, y, distance, color):
    # Draw Square in position x, y
    point1 = [x, y]
    point2 = [x + distance, y]
    counter = 0
    while counter < distance:
        pygame.draw.line(screen, color, point1, point2)
        point1[1] = point1[1] + 1
        point2[1] = point2[1] + 1
        counter = counter + 1

def make_rectangle(x1, y1, x2, y2, width, color):
    # Draw Square in position x, y
    point1 = [x1, y1]
    point2 = [x2, y2]
    counter = 0
    while counter < width:
        pygame.draw.line(screen, color, point1, point2)
        point1[1] = point1[1] + 1
        point2[1] = point2[1] + 1
        counter = counter + 1

# def make_rectangle2(x1, y1, x2, y2, width, color):
#     # Draw Square in position x, y
#     point1 = [x1, y1]
#     point2 = [x2, y2]
#     counter = 0
#     while counter < width:
#         pygame.draw.line(screen, color, point1, point2)
#         point1[1] = point1[1] + 1
#         point2[1] = point2[1] + 1
#         counter = counter + 1

#this is where the game code starts
while running:
    blue = (0, 0, 255)
    point1 = (100, 100)
    point2 = (100,200)
    pygame.draw.line(screen, blue, point1, point2)
    screen.fill((0, 0, 0))
    pygame.display.flip()
#this lets you exit the game
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    x_pos = 0
    y1 = 150
    y2 = 150

    pygame.display.flip()
    if x_pos == 0:
        while x_pos < 450:

            x_pos = x_pos + 1
            screen.fill((0, 0, 0))
            make_rectangle(470, y2, 490, y2, 150, blue)  # blue right wall
            make_rectangle(10, y1, 30, y1, 150, blue) #blue left wall
            make_square(x_pos, 200, 50, magenta)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                y2 = y2 - 1
            if keys[pygame.K_DOWN]:
                y2 = y2 + 1
            if keys[pygame.K_w]:
                y1 = y1 - 1
            if keys[pygame.K_s]:
                y1 = y1 + 1

            pygame.display.flip()

    if x_pos == 450:
        while x_pos > 0:
            x_pos = x_pos - 1
            screen.fill((0, 0, 0))
            make_rectangle(470, 150, 490, 150, 150, blue)  # blue right wall
            make_rectangle(10, 150, 30, 150, 150, blue)  # blue left wall
            make_square(x_pos, 200, 50, magenta)
            pygame.display.flip()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                y2 = y2 - 1
            if keys[pygame.K_DOWN]:
                y2 = y2 + 1
            if keys[pygame.K_w]:
                y1 = y1 - 1
            if keys[pygame.K_s]:
                y1 = y1 + 1


    # red = (255, 0, 0)
    # point1 = (200, 200)
    # point2 = (300, 200)
    # pygame.draw.line(screen, red, point1, point2)
    # pygame.display.flip()
    #
    # red = (255, 0, 0)
    # point1 = (300, 100)
    # point2 = (300, 200)
    # pygame.draw.line(screen, red, point1, point2)
    # pygame.display.flip()
    #
    # red = (255, 0, 0)
    # point1 = (200, 100)
    # point2 = (300, 100)
    # pygame.draw.line(screen, red, point1, point2)
    # pygame.display.flip()







