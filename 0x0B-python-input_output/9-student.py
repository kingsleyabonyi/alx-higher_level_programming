#!/usr/bin/python3
"""
    Defines a student class
"""


class Student:
    """
        A class Student
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializes instance variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Retrives the dict representation of the class
        """
        return (self.__dict__)
