import random
import numpy as np

def random_generator(data_type, num_range, num_count):
    if not isinstance(data_type, str) or not isinstance(num_range, tuple) or not isinstance(num_count, int):
        raise TypeError("Invalid input types")
    if data_type not in ["int", "float", "combination"]:
        raise ValueError("Invalid data type")
    if num_range[0] >= num_range[1]:
        raise ValueError("Invalid number range")
    if num_count <= 0:
        raise ValueError("Number of data must be positive")

    if data_type == "int":
        return [random.randint(num_range[0], num_range[1]) for _ in range(num_count)]
    elif data_type == "float":
        return [random.uniform(num_range[0], num_range[1]) for _ in range(num_count)]
    else:
        if num_count > np.math.comb(num_range[1]-num_range[0]+1, num_range[1]-num_range[0]+1):
            raise ValueError("Number of combinations is too large")
        data = list(range(num_range[0], num_range[1]+1))
        result = []
        for _ in range(num_count):
            random.shuffle(data)
            result.append(tuple(sorted(random.sample(data, num_range[1]-num_range[0]+1))))
        return result