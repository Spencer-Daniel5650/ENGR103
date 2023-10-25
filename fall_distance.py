# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/23/2023
# Discription: calculates fall distance

def fall_distance(time):
    """
    Calculate the distance an object falls due to gravity.

    :param time: The time in seconds.
    :return: The distance in meters that the object has fallen.
    """
    g = 9.8  # Acceleration due to gravity in m/s^2
    distance = (1/2) * g * time**2
    return distance
