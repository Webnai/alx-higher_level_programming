#!/usr/bin/python3
def add_integer(a: int, b: int = 98) -> int:
    """
    Return the sum of two integers a and b.
    
    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98.
    
    Returns:
        int: The sum of a and b.
        
    Raises:
        TypeError: If a or b is not an integer.
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    
    return a + b

