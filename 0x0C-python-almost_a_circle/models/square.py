```python
#!/usr/bin/python3

"""
Square Module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the square. Defaults to 0.
            y (int, optional): Y-coordinate of the square. Defaults to 0.
            id (int, optional): Identification number. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): New size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: String representation of the square.
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square object.

        Args:
            *args (int): Variable length argument list.
            **kwargs (int): Arbitrary keyword arguments.
        """
        keys = ("id", "size", "x", "y")
        for key, value in zip(keys, args):
            if key == "id" and not isinstance(value, int):
                continue
            setattr(self, key, value)
        if not args:
            for key, value in kwargs.items():
                if key == "id" and not isinstance(value, int):
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square object.

        Returns:
            dict: Dictionary representation of the square.
        """
        class_dict = {}
        keys = ("id", "size", "x", "y")
        for key in keys:
            class_dict[key] = getattr(self, key)
        return class_dict
```
