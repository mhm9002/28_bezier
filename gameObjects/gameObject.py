from func import getID

class gameObject:
    def __init__(self, app, color):
        self.app = app
        self.color = color
        self.id = getID()

    def update(self, delta):
        pass

    def render(self):
        pass