import pygame
from gameObjects.bezier import bezier
from gameObjects.spring import spring
from func import getColor, getPoints
from scene import scene
from vector import vec2

class scene1(scene):
    bezier1 = 0
    spring1 = 0
    
    def __init__(self, app):
        super().__init__(app)

        global bezier1
        global spring1

        bezier1 = self.addObject(bezier(self.app, getColor(), getPoints()))
        spring1 = self.addObject(spring(self.app, getColor(), vec2(150,150), 100, 0.015))

        print(bezier1, spring1)

    def handleEvent(self, event):

        global bezier1
        global spring1
        
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_0] and event.type==pygame.KEYUP:
            self.removeObject(self.getObjectByID(bezier1))
            

        if keys[pygame.K_8] and event.type==pygame.KEYUP:
            self.addObject(bezier(self.app, getColor(), getPoints()))

        if mouse[0]:
            pos = pygame.mouse.get_pos()
            self.getObjectByID(spring1).setEnd(vec2(pos[0],pos[1]))

        if mouse and event.type==pygame.MOUSEBUTTONUP:
            self.getObjectByID(spring1).release()
