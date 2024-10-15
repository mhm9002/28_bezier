
import math


class vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def lerp(self, vec, t):
        d = vec.subtract(self).mult(t)
        return self.add(d)
    
    def add(self, vec):
        return vec2(self.x+vec.x, self.y+vec.y)
    
    def subtract(self, vec):
        return vec2(self.x-vec.x, self.y-vec.y)
    
    def mult(self, factor:float):
        return vec2(self.x*factor, self.y*factor)
    
    def normalize(self):
        mag= self.mag()
        if mag==0: mag=0.0001
        return self.mult(1/mag)

    def mag(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def perpendicular(self):
        norm = self.normalize()
        return vec2(-norm.y, norm.x)
    
    def copy(self):
        return vec2(self.x, self.y)
    
    def tell(self):
        print(self.x, self.y)