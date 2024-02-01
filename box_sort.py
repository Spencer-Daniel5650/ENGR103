# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 1/23/2024
# Description: function that sorts a list of  objects in ascending order of their volumes using the insertion sort algorithm.

class Box:
    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def volume(self):
        return self.__length * self.__width * self.__height

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

def box_sort(boxes):
    for i in range(1, len(boxes)):
        key_box = boxes[i]
        j = i - 1

        # Compare the volumes and insert the box at the correct position
        while j >= 0 and key_box.volume() > boxes[j].volume():
            boxes[j + 1] = boxes[j]
            j -= 1

        boxes[j + 1] = key_box
