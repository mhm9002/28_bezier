import pygame
from pygame.locals import *

from scenes import sc1, sc2

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

        self.clock = pygame.time.Clock()
        self.time = 0
        self.start_time = 0
        self.delta_time = 0
        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.scene = sc2.scene2(self)
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        self.scene.handleEvent(event)
        
    def get_time(self):
        self.time = pygame.time.get_ticks() * 0.1

    def on_loop(self):
        self.scene.update(self.delta_time)
        
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.scene.render()

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self.get_time()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.delta_time = self.clock.tick(60) * 0.1
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()