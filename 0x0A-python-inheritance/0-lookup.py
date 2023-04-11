#/usr/bin/python3
def lookup(obj):
    """
    Get a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A sorted list of strings representing the names of the object's attributes and methods.

    Raises:
        TypeError: If the argument is not an object.

    Examples:
        >>> lookup([1, 2, 3])
        ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

    """
    if not isinstance(obj, object):
        raise TypeError("lookup() argument must be an object")
    return sorted(dir(obj))

