# Helper functions
def within_range(lower, input, upper) -> bool:
    return lower <= input <= upper

def under_255(input) -> bool:
    """
    Max rgb value is 255.
    """
    return 0 <= input <= 255