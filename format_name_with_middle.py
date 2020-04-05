from names import Names

"""
This Class inherits from the original Name class but includes a middle
name variable.
"""


class create_with_middle_name(Names):
    """
    Only the middle name is different, so that is the only variable listed.
    """

    def __init__(self):
        self.middle = ""

    """
    Same as original fill in function from the name class but with additional
    variable.
    """

    def fill_in(self):
        return self.first, \
               self.middle, \
               self.last

    """
    The return string for the object is different.
    """

    def __str__(self):
        self.middle = self.middle[0]
        print(self.middle)
        stringo = 'The current name object is {} {}.' \
                  ' {}'.format(self.first, self.middle, self.last)
        return stringo
