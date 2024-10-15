import random
import pygame

from func import recursiceLerp
from gameObjects.gameObject import gameObject
from vector import vec2

GUIDE_COLOR = (40,40,40)

class bezier(gameObject):
    def __init__(self, app, color, points:list[vec2]) -> None:
        super().__init__(app, color)

        self.points= points
        self.movement = [vec2(random.uniform(-3,3),random.uniform(-3,3)) for _p in self.points]

    def update(self, delta):
        for i in range(0, len(self.points)):
            self.points[i] = self.points[i].add(self.movement[i].mult(delta))
           
            self.flipMovement(i)

    def flipMovement(self, index):
        m = self.movement[index]

        mx = m.x
        my = m.y

        if self.points[index].x>=640 or self.points[index].x<0: mx*=-1
        if self.points[index].y>=400 or self.points[index].y<0: my*=-1

        self.movement[index] = vec2(mx,my)

    def getPoints(self)->list[vec2]:
        points = []

        for p in range(0,101, 5):

            t = p*0.01
            points.append(recursiceLerp(self.points, t))

        return points

    def render(self):
        points = self.getPoints()
        
        for i in range(0, len(points)-1):
            p = points[i]
            p2 = points[i+1]
            pygame.draw.line(self.app._display_surf, self.color, (int(p.x),int(p.y)),  (int(p2.x),int(p2.y)),3)


        for i in range(0, len(self.points)):
            p = self.points[i]
            
            if i<len(self.points)-1:
                p2 = self.points[i+1]
            else:
                p2 = self.points[0]
            pygame.draw.circle(self.app._display_surf, GUIDE_COLOR, (int(p.x),int(p.y)), 5)
            pygame.draw.line(self.app._display_surf, GUIDE_COLOR, (int(p.x),int(p.y)),  (int(p2.x),int(p2.y)),1)


