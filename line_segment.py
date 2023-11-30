# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 11/26/2023
# Description: The code defines Point for coordinate handling and LineSegment for line measurements, including length, slope, and parallelism checks.

class Point:
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord

    def distance_to(self, other):
        return ((self._x_coord - other._x_coord) ** 2 + (self._y_coord - other._y_coord) ** 2) ** 0.5


class LineSegment:
    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        return self._endpoint_1

    def get_endpoint_2(self):
        return self._endpoint_2

    def length(self):
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        dx = self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord()
        dy = self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()
        return dy / dx if dx != 0 else float('inf')

    def is_parallel_to(self, other):
        return abs(self.slope() - other.slope()) < 0.000001
