def recursive_sum(input_data):
    if isinstance(input_data, list):
        return sum([recursive_sum(el) for el in input_data])
    else:
        return float(input_data)
