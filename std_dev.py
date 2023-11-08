# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 11/06/2023
# Description: The `Person` class encapsulates private name and age attributes with a method to retrieve the age, and the `std_dev` function computes the population standard deviation of ages from a list of `Person` instances.

class Person:
    def __init__(self, name, age):
        """
        Initialize the private data members for name and age.
        """
        self.__name = name  # private member for name
        self.__age = age    # private member for age

    def get_age(self):
        """
        Return the age of the person.
        """
        return self.__age

def std_dev(person_list):
    """
    Calculate and return the population standard deviation of ages from a list of Person objects.
    If the list is empty, return None.
    """
    if not person_list:  # Check if the list is empty
        return None

    # Calculate the mean age
    mean_age = sum(person.get_age() for person in person_list) / len(person_list)
    # Calculate the sum of squared differences from the mean
    variance = sum((person.get_age() - mean_age) ** 2 for person in person_list) / len(person_list)
    # Return the square root of variance, which is the standard deviation
    return variance ** 0.5
