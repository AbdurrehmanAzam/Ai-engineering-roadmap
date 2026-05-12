def power(a=1, b=1):
    """
    Calculates 'a' raised to the power of 'b'.
    Uses default arguments (1) to prevent the program from crashing if no values are provided.
    """
    return a**b


# Positional arguments: The first value (2) goes to 'a', and the second value (5) goes to 'b'.
print(power(2, 5))
