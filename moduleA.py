pi = 3.1415

def area(r):
    return pi * r**2

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return area(self.radius)

    def circumference(self):
        return 2*pi*self.radius
