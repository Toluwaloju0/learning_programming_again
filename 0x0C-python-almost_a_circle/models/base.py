#!/usr/bin/python3
"""
A module to create a base class for all models on the application
"""

import json
import csv


class Base:
    """ the base class"""

    __nb_objects = 0  # the private class attribute

    def __init__(self, id=None):
        """
        The initializer of the class
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        A static method to get the JSON representation of objects
        Args:
            list_dictionaries: a list containing dictionaries
        """

        if not list_dictionaries:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A method to write the content of a list to a file
        Args:
            cls: the cls of the object
            list_objs: the list of objs to be written
        """

        list_dictionaries = []
        with open(f"{cls.__name__}.json", "w") as json_file:
            if not list_objs:
                list_objs = []

            # convert each member of the list_objs to a dictionary
            # using the to dictionary method of the class
            for cls_instance in list_objs:
                list_dictionaries.append(cls_instance.to_dictionary())

            json_file.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        A method to get a dictionary from a json string
        Args:
            json_string: the string in json format
        """

        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """
        A method to create a new instance of a class
        Args:
            dictionary: the dictionary to create the class from
        """

        if cls.__name__ == "Rectangle":
            dummy_class = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_class = cls(1)
        dummy_class.update(**dictionary)

        return dummy_class

    @classmethod
    def load_from_file(cls):
        """
        A method to get a class attributes from a file and create a classes
        """

        try:
            with open(f"{cls.__name__}.json", 'r') as cls_file:
                # Create a list of the objects dictionary
                list_dictionaries = cls.from_json_string(cls_file.read())
            instance_list = []
            # create each new instance and store it in instance list
            for obj_dictionary in list_dictionaries:
                instance_list.append(cls.create(**obj_dictionary))
            return instance_list
        except OSError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        A method to save a list of objects to a csv file
        Args:
            list_objs: The list of objects to be saved to csv
        """

        if cls.__name__ == "Rectangle":
            field_name = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            field_name = ["id", "size", "x", "y"]
        # Open the file and write to it using csv writer
        with open(f"{cls.__name__}.csv", 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
            csv_writer.writeheader()   # write the header first
            if not list_objs:
                return
            for instance in list_objs:
                csv_writer.writerow(instance.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        A method to load a class from a csv file
        """

        instance_list = []
        try:
            with open(f"{cls.__name__}.csv", 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    new_dict = {}
                    for key, value in row.items():
                        new_dict[key] = int(value)
                    instance_list.append(cls.create(**new_dict))
            return instance_list
        except OSError:
            return []
