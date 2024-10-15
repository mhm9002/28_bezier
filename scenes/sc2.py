import pygame
from func import getColor
from gameObjects.rope2 import rope2
from scene import scene
from vector import vec2

class scene2(scene):
    def __init__(self, app):
        super().__init__(app)
        self.addObject(rope2(self.app,getColor(), vec2(320, 50), 10, 10))

    def handleEvent(self, event):
        mouse = pygame.mouse.get_pressed()
        
        if mouse[0]:
            pos = pygame.mouse.get_pos()
            self.objects[0].setTail(vec2(pos[0],pos[1]))

        #if mouse and event.type==pygame.MOUSEBUTTONUP:
        #    self.objects[0].release()