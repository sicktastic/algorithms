def magitude(self):
    coordinates_squared = [x**2 for x in self.coordinates]
    return sqrt(sum(coordinates_squared))

def normalize(self):
    try:
        magitude = self.magnitude()
        return self.times_scalar(1./magnitude)

    except ZeroDivisionError:
        raise Exception('Cannot normalize the zero vector')

def plus(self, v):
    new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)