import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        # Set angle and radius for the split asteroids
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids from the split
        first_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        second_asteroid = Asteroid(self.position.x,self.position.y,new_radius)

        # Make them go faster (offset them at equidistant angles from the original vector)
        first_asteroid.velocity = self.velocity.rotate(angle) * 1.2
        second_asteroid.velocity = self.velocity.rotate(-angle) * 1.2