from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot

# Base class for game objects
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0


    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)


    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if  keys[pygame.K_SPACE]:
            self.shoot()


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def shoot(self):
        shoot_position = Shot(self.position.x, self.position.y)
        shoot_vector =  pygame.Vector2(0, 1)
        shoot_rotate =  shoot_vector.rotate(self.rotation)
        shoot_velocity = PLAYER_SHOOT_SPEED * shoot_rotate



        
       



