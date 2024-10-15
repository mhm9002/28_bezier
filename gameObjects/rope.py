
from gameObjects.gameObject import gameObject
from gameObjects.spring import spring
from vector import vec2

class rope(gameObject):
    def __init__(self, app, color, anchor:vec2, springCount:int, springLength:float, k:float=0.4):
        super().__init__(app, color)

        self.anchor = anchor
        
        self.springs:list[spring]=[]
        p=anchor.copy()
        for i in range(0, springCount):
            s = spring(self.app, self.color, p, springLength, k)
            p = p.add(s.direction.mult(springLength))
            self.springs.append(s)

    def setTail(self, tail:vec2):
        self.springs[len(self.springs)-1].end = tail

    def update(self, delta):
        
        for i in range( len(self.springs)-1, -1, -1):
            
            self.springs[i].update(delta)
            self.springs[i].anchor = self.springs[i].anchor.add(self.springs[i].velocity.mult(-delta))
            if (i>0):
                self.springs[i-1].end = self.springs[i].anchor.copy()
                self.springs[i-1].direction = self.springs[i-1].end.subtract(self.springs[i-1].anchor).normalize()
            
        #self.springs[0].anchor = self.anchor
        

    def render(self):
        [s.render() for s in self.springs]
        #pygame.draw.circle(self.app._display_surf, self.color, (int(self.tail.x),int(self.tail.y)), 12)