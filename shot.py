import pygame
from constants import SHOT_RADIUS, LINE_WIDTH
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x:float, y:float):
        super().__init__(x, y, SHOT_RADIUS)


    #override
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            surface = screen,
            color = "white",
            center = self.position,
            radius = self.radius,
            width = LINE_WIDTH
        )


    #override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
