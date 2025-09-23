#!/usr/bin/python3
"""Define a class Square with size, position, area, and printing capabilities."""


class Square:
    """Represents a square with private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The (x, y) position offsets. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the private position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the private position attribute with validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(v, int) for v in value)
            or not all(v >= 0 for v in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character, respecting the position.

        If size is 0, prints an empty line.
        position[0] is the horizontal offset (spaces before '#')
        position[1] is the vertical offset (blank lines before square)
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each square line with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
