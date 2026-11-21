# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Creates a Person, given values for name and birth.
        """
        self.name = name
        self.birth = birth

        if not isinstance(name, str):
            raise TypeError("Name has to be a string.")
        
        if len(name) == 0:
            raise ValueError("Name cannot be an empty string.")
        
        if not isinstance(birth, date):
            raise TypeError("Birthday has to be a date.")

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        Return initials of name in uppercase
        """
        return "".join([name[0] for name in self.name.split()]).upper()

    def is_birthday(self):
        """
        Return true if today's month and day matches the person's birthday
        """
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day
