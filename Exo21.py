def length(lst):
    """Return the number of elements in the list."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    return len(lst)

def mean(lst):
    """Calculate the arithmetic mean of the list."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if not lst:
        raise ValueError("Cannot calculate mean of an empty list.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only numeric values.")
    return sum(lst) / len(lst)

def range_of_list(lst):
    """Return the difference between the maximum and minimum values in the list."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if not lst:
        raise ValueError("Cannot calculate range of an empty list.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only numeric values.")
    return max(lst) - min(lst)

def median(lst):
    """Calculate the median of the list."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if not lst:
        raise ValueError("Cannot calculate median of an empty list.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only numeric values.")
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def standard_deviation(lst):
    """Calculate the standard deviation of the list."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if not lst:
        raise ValueError("Cannot calculate standard deviation of an empty list.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only numeric values.")

    mean_value = mean(lst)
    variance = sum((x - mean_value) ** 2 for x in lst) / len(lst)
    return variance ** 0.5

def list_statistics(lst):
    """Create a dictionary with all list statistics."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    if not lst:
        raise ValueError("Cannot calculate statistics for an empty list.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("List must contain only numeric values.")

    return {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst),
    }

# Test cases
if __name__ == "__main__":
    test_cases = [
        [],
        [42],
        [-10, 0, 10],
        [1.5, 2.5, 3.5],
        [1, 2, 3, 4, 5],
    ]

    for idx, case in enumerate(test_cases):
        try:
            print(f"Test Case {idx + 1}: {case}")
            print(f"Length: {length(case)}")
            print(f"Mean: {mean(case)}")
            print(f"Range: {range_of_list(case)}")
            print(f"Median: {median(case)}")
            print(f"Standard Deviation: {standard_deviation(case)}")
            print(f"All Statistics: {list_statistics(case)}")
            print("-" * 40)
        except Exception as e:
            print(f"Error for test case {idx + 1}: {e}")
            print("-" * 40)
