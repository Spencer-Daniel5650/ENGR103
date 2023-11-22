# Author: Daniel Spencer
# GitHub Username: Spencer-Daniel5650
# Date: 11/21/2023
# Description: Creates Employee dict

class Employee:
    def __init__(self, name, ID_number, salary, email_address):
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        return self._name

    def get_ID_number(self):
        return self._ID_number

    def get_salary(self):
        return self._salary

    def get_email_address(self):
        return self._email_address

def make_employee_dict(names, ids, salaries, emails):
    employee_dict = {}
    for name, ID, salary, email in zip(names, ids, salaries, emails):
        employee = Employee(name, ID, salary, email)
        employee_dict[ID] = employee
    return employee_dict


