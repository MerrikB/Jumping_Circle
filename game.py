# Simple pygame program

# Import and initialize the pygame library
import pygame
from threading import Timer
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
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def jump(self):
        def update(t):
            global velocity_y, gravity, onGround
            velocity_y += gravity
            self.y += velocity_y

            if self.y > 400:
                self.y = 400
                velocity_y = 0
                onGround = True
                t.cancel()
            

        def loop():
            print(self.y)
            t = Timer(0.066, loop)
            update(t)
            t.start()

        loop()


def redrawGameWindow():
    screen.fill((255, 255, 255))
    g_circle.draw(screen)

    pygame.display.update()


g_circle = Circle((0, 0, 255), 250, 400, 75)

# Run until the user asks to quit
running = True
while running:
    clock.tick(60)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and onGround:
        velocity_y = -14
        onGround = False
        g_circle.jump()
    if keys[pygame.K_RIGHT] and g_circle.x < 415:
        g_circle.x = g_circle.x + 3
    elif keys[pygame.K_LEFT] and g_circle.x > 85:
        g_circle.x = g_circle.x -3
    
    redrawGameWindow()

# Done! Time to quit.
pygame.quit()