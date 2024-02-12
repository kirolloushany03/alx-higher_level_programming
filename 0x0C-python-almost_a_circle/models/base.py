#!/usr/bin/python3

"""Base Module"""

import json
import turtle

class Base:
    """
    Base class for creating and manipulating objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of Base.

        Args:
            id (int): Identification number.
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation.
        """

        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to save.
        """

        list_dict = ([*map(lambda self: self.to_dictionary(), list_objs)]
                     if list_objs else [])
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Creates a list of objects from a JSON string.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of objects.
        """

        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of Base from a dictionary.

        Args:
            **dictionary: Arbitrary keyword arguments.

        Returns:
            obj: Instance of Base.
        """

        obj = {}
        try:
            obj = cls(1)
        except TypeError:
            obj = cls(1, 1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Loads instances of Base from a JSON file.

        Returns:
            list: List of instances of Base.
        """

        try:
            with open(f"{cls.__name__}.json", "r") as f:
                return [cls.create(**inst) for inst in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects to save.
        """

        r_keys = ("id", "width", "height", "x", "y")
        s_keys = ("id", "size", "x", "y")
        class_name = cls.__name__
        list_dict = ([*map(lambda self: self.to_dictionary(), list_objs)]
                     if list_objs else [])
        csv_list = []
        for inst_dict in list_dict:
            inst_list = []
            keys_list = inst_dict.keys()
            for key in s_keys if class_name == "Square" else r_keys:
                if key in keys_list:
                    inst_list.append(str(inst_dict[key]))
            if inst_list:
                csv_list.append(inst_list)

        with open(f"{class_name}.csv", "w") as f:
            if list_objs:
                if class_name == "Square":
                    f.write(",".join(s_keys) + "\n")
                elif class_name == "Rectangle":
                    f.write(",".join(r_keys) + "\n")
                for row in csv_list:
                    f.write(",".join(row) + "\n")
            else:
                f.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads instances of Base from a CSV file.

        Returns:
            list: List of instances of Base.
        """

        class_name = cls.__name__
        try:
            with open(f"{class_name}.csv", "r") as f:
                inst_list = []
                for line in f:
                    if "id" in line:
                        continue
                    obj = cls(1) if class_name == "Square" else cls(1, 1)
                    obj.update(*map(int, line.split(",")))
                    inst_list.append(obj)
                return inst_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws rectangles and squares using turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle objects.
            list_squares (list): List of Square objects.
        """

        cursor = turtle.Turtle()
        cursor.color("blue", "red")
        cursor.penup()
        cursor.left(180)
        cursor.forward(50)
        cursor.pendown()

        # Draw rectangles
        for rect in list_rectangles:
            width = rect.width
            height = rect.height
            cursor.begin_fill()
            cursor.forward(width)
            cursor.right(90)
            cursor.forward(height)
            cursor.right(90)
            cursor.forward(width)
            cursor.right(90)
            cursor.forward(height)
            cursor.penup()
            cursor.right(180)
            cursor.forward(height + 10)
            cursor.left(90)
            cursor.pendown()
            cursor.end_fill()

        cursor.penup()
        cursor.goto(0, 0)
        cursor.left(180)
        cursor.forward(50)
        cursor.pendown()

        # Draw squares
        for square in list_squares:
            size = square.size
            cursor.begin_fill()
            for _ in range(3):
                cursor.forward(size)
                cursor.left(90)
            cursor.forward(size)
            cursor.penup()
            cursor.right(180)
            cursor.forward(size + 10)
            cursor.right(90)
            cursor.pendown()
            cursor.end_fill()

        cursor.penup()
        cursor.goto(0, 0)
        cursor.left(90)
        turtle.done()
