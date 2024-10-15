import random
from vector import vec2


def recursiceLerp(points:list[vec2], t):
    if len(points)==1:
        return points[0]
    
    p = []

    for i in range(0,len(points)-1):
        p.append(points[i].lerp(points[i+1], t))

    return recursiceLerp(p, t)


def getColor():
    return (random.uniform(100,255),random.uniform(100,255),random.uniform(100,255))

def getPoints(count:int = 5):
    return [vec2(random.uniform(0,640),random.uniform(100,400)) for i in range(1,count)]

def getID():
    return random.uniform(1, 100000)