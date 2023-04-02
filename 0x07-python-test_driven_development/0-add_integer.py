def add_integer(a, b=98):
    """ checks if  and b are intiger or float"""
    if not isinstance (a, (int, float)):
        raise TypeError ("a must be an integer or b must be an integer")
    if not isinstance (b, (int, float)):
        raise TypeError ("a must be an integer or b must be an integer")
    """casts a and b in to int if they are float"""
    if isinstance (a, float):
        a = int(a)
        b = int(b)
    """return the sum of intigers"""
    return a + b


