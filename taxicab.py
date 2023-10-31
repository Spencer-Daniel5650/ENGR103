# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/28/2023
# Description: The code defines a simplified representation of a taxicab on a 2D grid using a dictionary, providing functions to move the cab and retrieve its position and total distance traveled.

class Taxicab:
    """
    Represents a Taxicab in a 2D grid with an odometer to measure the distance traveled.
    """

    def __init__(self, x_coord, y_coord):
        """
        Initializes the Taxicab with given x and y coordinates, and sets the odometer to zero.
        """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """
        Returns the x-coordinate of the Taxicab.
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Returns the y-coordinate of the Taxicab.
        """
        return self._y_coord

    def get_odometer(self):
        """
        Returns the odometer reading of the Taxicab.
        """
        return self._odometer

    def move_x(self, distance):
        """
        Moves the Taxicab left or right based on the provided distance.
        """
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Moves the Taxicab up or down based on the provided distance.
        """
        self._y_coord += distance
        self._odometer += abs(distance)


