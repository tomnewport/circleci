"""
Thingy!
"""

def recursive_sum(input_data):
    """
    Recursively sum elements of a list, or return float value of anything else
    """
    value = None
    if isinstance(input_data, list):
        value = sum([recursive_sum(el) for el in input_data])
    else:
        value = float(input_data)
    return value
