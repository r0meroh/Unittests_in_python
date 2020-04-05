"""
This file includes the superclass object name. Only consisting of
a first name and last.

"""


class Names:
    """
    The default constructor prevents errors by having default
    values.
    """

    def __init__(self):
        self.first = ""
        self.last = ""

    """
    Optional way of retrieving class variables for reference.
    """
    def fill_in(self):
        return self.first, self.last


    """
    Function string to identify objects when printed.
    """
    def __str__(self):
        stringy = 'The current name object is {self.first} {self.last}'.format(self=self)
        return stringy
