import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Traffic Racer")

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# Clock
clock = pygame.time.Clock()


# Base class
class Car:
    def __init__(self, x, y, color):
        self.width = 40
        self.height = 60
        self.x = x
        self.y = y
        self.color = color
        self.speed = 5

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))


# Player class (inherits from Car)
class PlayerCar(Car):
    def __init__(self, x, y):
        super().__init__(x, y, BLUE)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
            self.y += self.speed


# Traffic car (inherits from Car)
class TrafficCar(Car):
    def __init__(self):
        x = random.randint(0, WIDTH - 40)
        y = random.randint(-600, -60)
        super().__init__(x, y, RED)
        self.speed = random.randint(3, 7)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-100, -60)
            self.x = random.randint(0, WIDTH - 40)


# ---------------- GAME LOOP ---------------- #
player = PlayerCar(WIDTH // 2, HEIGHT - 100)
traffic = [TrafficCar() for _ in range(5)]

running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw(screen)

    for car in traffic:
        car.update()
        car.draw(screen)

        # Collision check
        if pygame.Rect(car.x, car.y, car.width, car.height).colliderect(
            pygame.Rect(player.x, player.y, player.width, player.height)
        ):
            running = False  # End game on crash

    pygame.display.flip()

pygame.quit()

# ------------------ OOP EXPLANATION ------------------ #
"""
What is the difference between OOP and Procedural coding?

- OOP uses classes and objects to organize code.
- The program is run by the procedural coding with use of functions and steps.

How would your program differ if it were made in procedural coding instead?

- There would be no classes.
- The car will be controlled by both variables and functions in regards to its positions and motions.
- It would be more difficult to maintain numerous cars and recycle code.

What are the benefits of OOP?

- Easier to organize and understand code.
- You can reuse code from classes and by inheritance.
– It’s easy to add new features.

What are the drawbacks?

- It takes more time to set up.
- Might be too much for very small or simple programs.
"""
