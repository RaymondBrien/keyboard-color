# Helper functions
def within_range(lower, input, upper) -> bool:
    return lower <= input <= upper

def under_25(input) -> bool:
#    return True if 0 <= input <= 25 else False
    return within_range(0, input, 25)

def under_255(value):
    """Max rgb value is 255"""
    return within_range(0, value, 255)