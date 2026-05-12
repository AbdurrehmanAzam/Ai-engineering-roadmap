# remember always keyword argument will override the positional arguments
def power(a, b):
    """
    Calculates 'a' raised to the power of 'b'.
    Uses default arguments (1) to prevent the program from crashing if no values are provided.
    """
    return a**b


print(power(b=2, a=3))
