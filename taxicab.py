def Taxicab(x, y):
    """Defines the Taxicab class."""
    cab = {"x": x, "y": y, "odometer": 0}
    return cab

def get_x_coord(cab):
    """Returns the x-coordinate of the cab."""
    return cab["x"]

def get_y_coord(cab):
    """Returns the y-coordinate of the cab."""
    return cab["y"]

def get_odometer(cab):
    """Returns the odometer reading of the cab."""
    return cab["odometer"]

def move_x(cab, distance):
    """Moves the cab in the x direction."""
    cab["x"] += distance
    cab["odometer"] += abs(distance)

def move_y(cab, distance):
    """Moves the cab in the y direction."""
    cab["y"] += distance
    cab["odometer"] += abs(distance)

# Example usage:
cab = Taxicab(5, -8)
move_x(cab, 3)
move_y(cab, -4)
move_x(cab, -1)
print(get_odometer(cab))
