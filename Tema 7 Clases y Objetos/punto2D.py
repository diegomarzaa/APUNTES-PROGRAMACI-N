class punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def distancia(self, otro):
        return ((self.x - otro.x)**2 + (self.y - otro.y)**2)**0.5

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y