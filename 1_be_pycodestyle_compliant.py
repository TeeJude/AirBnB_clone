def add_numbers(numbers):
    """
    Add a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The total sum of the numbers.
    """
    
    total = sum(numbers)
    return total

""" How to Use the function """
number_list = [5,12.4, 23, 7.3, 32, 2]
result = add_numbers(number_list)
print("The sum of this number list is:", result)

