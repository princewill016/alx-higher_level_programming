#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class;
    otherwise, False.

    Parameters:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    bool: True if obj is an instance of a_class or inherited from it;
          False otherwise.
    """
    return isinstance(obj, a_class)
