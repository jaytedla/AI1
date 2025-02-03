def generate_fibinacci_series_in_range(start, end):
    """
    This function takes two integers and returns a list of Fibonacci numbers between the two integers.
    
    Parameters:
    start (int): The starting integer.
    end (int): The ending integer.
    
    Returns:
    list: A list containing the Fibonacci numbers between start and end.
    """
    fib_series = []
    a, b = 0, 1
    while a < end:
        if a >= start:
            fib_series.append(a)
        a, b = b, a + b
    return fib_series

print(generate_fibinacci_series_in_range(1, 100))

