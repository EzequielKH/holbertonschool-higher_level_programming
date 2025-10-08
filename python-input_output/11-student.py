#!/usr/bin/python3
class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr_name in attrs:
                if hasattr(self, attr_name):
                    filtered_dict[attr_name] = getattr(self, attr_name)
            return filtered_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
