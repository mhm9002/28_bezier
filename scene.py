from gameObjects.gameObject import gameObject

class scene:
    def __init__(self, app):
        self.app = app
        self.objects = []

    def addObject(self, object:gameObject):
        self.objects.append(object)
        return object.id
    
    def removeObject(self, object:gameObject):
        self.objects.remove(object)
    
    def getObjectByID(self, id:int):
        obj = [o for o in self.objects if o.id==id]
        return obj[0]

    def handleEvent(self, event):
        pass

    def update(self, delta):
        for obj in self.objects:
            obj.update(delta)

    def render(self):
        for obj in self.objects:
            obj.render()
