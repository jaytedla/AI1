def generate_odd_number_between_range_list(start, end):
    """
    This function takes two integers and returns a list of odd numbers between the two integers.
    
    Parameters:
    start (int): The starting integer.
    end (int): The ending integer.
    
    Returns:
    list: A list containing the odd numbers between start and end.
    """
    return [x for x in range(start, end) if x % 2 != 0]
print(generate_odd_number_between_range_list(1, 100))

