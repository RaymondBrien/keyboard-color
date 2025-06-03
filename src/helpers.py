# Helper functions
def within_range(lower, input, upper) -> bool:
    return lower <= input <= upper

def under_25(input) -> bool:
    """less then or equal to 25, returned as bool"""
    return input <= 25

def under_255(input):
    """Max rgb value is 255, Returns bool, less than or equal to 255"""
    return input <= 255