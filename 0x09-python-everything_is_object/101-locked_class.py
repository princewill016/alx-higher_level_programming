#!/usr/bin/python3
class LockedClass:
    """
    A class that prevents dynamic attribute creation except for 'first_name'.
    """

    __slots__ = ("first_name",)  # Define allowed attributes with slots

    def __setattr__(self, name, value):
        if name == "first_name":
            object.__setattr__(self, name, value)  # Allow setting first_name
        else:
            raise AttributeError("Can't add new attribute '{}'".format(name))

# Example usage
lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
