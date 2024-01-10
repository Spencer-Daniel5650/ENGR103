# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 10/08/2023
# Description: Calculates mean, median, and mode of grades from student objects

import statistics

class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

def basic_stats(students):
    grades = [student.get_grade() for student in students]
    mean = statistics.mean(grades)
    median = statistics.median(grades)
    mode = statistics.mode(grades)
    return (mean, median, mode)

# Example usage
students = [
    Student("Alice", 90),
    Student("Bob", 85),
    Student("Charlie", 90),
    Student("Diana", 85)
]

stats = basic_stats(students)
print(stats)  # This will print the mean, median, and mode of the grades
