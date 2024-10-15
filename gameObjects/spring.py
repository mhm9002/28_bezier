

import pygame
from gameObjects.gameObject import gameObject
from vector import vec2

STEPS = 10
GRAVITY = vec2(0,0.1)

class spring(gameObject):
    def __init__(self, app, color, anchor:vec2, length:float, k:float=0.1):
        super().__init__(app, color)
        
        self.anchor=anchor
        self.k = k
        self.length = length
        self.direction = vec2(0,1)
        self.velocity = vec2(0,0)
        self.end = self.anchor.add(self.direction.mult(self.length))
        self.pressed = False
        
    def setEnd(self, end:vec2):
        self.end = end
        self.direction = self.end.subtract(self.anchor).normalize()
        self.pressed = True
       
    def release(self):
        self.pressed= False

    def update(self, delta):
        if self.pressed:
            return

        difference = self.end.subtract(self.anchor)
        displacement= difference.mag() - self.length
        self.direction = difference.normalize()
        
        force = self.direction.mult(-self.k*displacement)
        self.velocity = self.velocity.add(force)
        self.velocity = self.velocity.add(GRAVITY.mult(10))

        self.end = self.end.add(self.velocity.mult(delta))

        self.velocity = self.velocity.mult(0.9)

    def render(self):
            
        #pygame.draw.line(self.app._display_surf, self.color, (int(self.anchor.x),int(self.anchor.y)),  (int(self.end.x),int(self.end.y)),3)

        perpend = self.direction.perpendicular()
        stepDis = self.end.subtract(self.anchor).mult(1/STEPS)

        p = self.anchor.copy().subtract(perpend.mult(-1*self.length/20))

        for i in range(0, STEPS):
            f=1
            if i%2==0:
                f=-1
            
            nextP = p.add(stepDis.add(perpend.mult(f*self.length/10)))

            pygame.draw.line(self.app._display_surf, self.color, (int(p.x),int(p.y)), (int(nextP.x),int(nextP.y)),3)
            p= nextP.copy()


        pygame.draw.circle(self.app._display_surf, self.color, (int(self.anchor.x),int(self.anchor.y)), 5)
        #pygame.draw.circle(self.app._display_surf, self.color, (int(self.end.x),int(self.end.y)), 5)
         