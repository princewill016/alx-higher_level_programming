#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise, False.

    Parameters:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    bool: True if obj is an instance of a class that inherited
          from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
