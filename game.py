# Simple pygame program

# Import and initialize the pygame library
import pygame

# built in library that we use as a timer
from threading import Timer

# imports all pygame modules for us to use
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

# jump variables
gravity = 1
velocity_y = -14
onGround = True


class Circle(object):
    def __init__(self, color, x, y, radius):
        # contructor function for the Circle class
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        # draws a circle on the window or 'screen' with color, x, y, and radius parameters
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def jump(self):
        def update(t):
            global velocity_y, gravity, onGround
            # the gravity changes the velocity according to the objects force and distance from the ground
            velocity_y += gravity
            self.y += velocity_y

            if self.y > 400:
                # updating variables for grounded state
                self.y = 400
                velocity_y = 0
                onGround = True
                # ends loop
                t.cancel()
            

        def loop():
            # loops through update loop until circle object has touched the ground            
            
            # updates the position of the object every .066th of a second
            # lets us have that jump effect. Without it the object would appear to have not moved
            t = Timer(0.066, loop)
            update(t)
            t.start()

        # starts the jump loop
        loop()


class Platform(object):
    def __init__(self, color, x, y, width, height):


def redrawGameWindow():
    # updating game window
    screen.fill((255, 255, 255))
    g_circle.draw(screen)
    pygame.display.update()

# creating an object from the Circle class
g_circle = Circle((0, 0, 255), 250, 400, 75)

# Run until the user asks to quit
running = True
while running:
    clock.tick(60)

    # click event for quiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # list of pressed keys while game is in action
    keys = pygame.key.get_pressed()

    # press up to jump
    if keys[pygame.K_UP] and onGround:
        # resetting jump variables
        velocity_y = -14
        onGround = False
        # calling custom function from Circle class
        g_circle.jump()

    # press right to move right
    if keys[pygame.K_RIGHT] and g_circle.x < 415:
        g_circle.x = g_circle.x + 3
    
    # press left to move left
    elif keys[pygame.K_LEFT] and g_circle.x > 85:
        g_circle.x = g_circle.x -3
    
    redrawGameWindow()

# Done! Time to quit.
pygame.quit()