
class Agente():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_vecinos(self, x, y):
        pass

class Casilla():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.padre = [None]

    def get_vecinos(self, x, y):
        pass