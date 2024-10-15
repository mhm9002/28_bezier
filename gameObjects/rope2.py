
import pygame
from gameObjects.gameObject import gameObject
from vector import vec2

GRAVITY = vec2(0,-0.1)

class rope2(gameObject):
    def __init__(self, app, color, anchor:vec2, springCount:int, springLength:float, k:float=0.01):
        super().__init__(app, color)

        self.anchor = anchor
        self.springLength = springLength
        self.points  = [vec2(anchor.x, anchor.y+self.springLength * i) for i in range(0, springCount)]
        self.velocity = [vec2(0,0) for i in range(0,springCount)]
        self.k = k

    def setTail(self, tail:vec2):
        self.points[len(self.points)-1] = tail

    def update(self, delta):
        for i in range(1, len(self.points)):
            force = self.points[i].subtract(self.points[i-1])
            displacement = force.mag() - self.springLength
            force = force.normalize().mult(self.k * displacement)

            self.velocity[i] = self.velocity[i].add(force.mult(delta))
            self.velocity[i] = self.velocity[i].add(GRAVITY)

            self.points[i-1] = self.points[i-1].add(self.velocity[i])
            self.points[i] = self.points[i].add(self.velocity[i].mult(-1))
            
            self.velocity[i] = self.velocity[i].mult(0.9)

        self.points[0]=self.anchor

    def render(self):
        for i in range(1, len(self.points)-1):
            pygame.draw.line(self.app._display_surf, self.color, 
                             (self.points[i-1].x, self.points[i-1].y)  , 
                             (self.points[i].x,self.points[i].y),3)
