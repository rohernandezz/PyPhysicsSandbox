import pymunk
import pymunk.pygame_util
import pygame
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Create space
space = pymunk.Space()
space.gravity = (0, 981)

# Helper function to convert global to local coordinates
def global_to_local(global_point, body):
    local_x = global_point[0] - body.position.x
    local_y = global_point[1] - body.position.y
    return (local_x, local_y)

# Create two bodies
body_a = pymunk.Body()
body_a.position = (400, 300)
shape_a = pymunk.Circle(body_a, 10)
space.add(body_a, shape_a)

body_b = pymunk.Body()
body_b.position = (600, 300)
shape_b = pymunk.Circle(body_b, 10)
space.add(body_b, shape_b)

# Define global anchor points
global_anchor_a = (450, 300)
global_anchor_b = (550, 300)

# Convert global coordinates to local coordinates
local_anchor_a = global_to_local(global_anchor_a, body_a)
local_anchor_b = global_to_local(global_anchor_b, body_b)

# Create spring with global coordinates
spring_global = pymunk.DampedSpring(body_a, body_b, global_anchor_a, global_anchor_b, 100, 10, 0.5)
space.add(spring_global)

# Create spring with local coordinates
spring_local = pymunk.DampedSpring(body_a, body_b, local_anchor_a, local_anchor_b, 100, 10, 0.5)
space.add(spring_local)

# Run the simulation
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    space.debug_draw(draw_options)
    space.step(1/60.0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
