def intersection_of_lists(list1, list2):
    """
    This function takes two lists and returns a list that contains the intersection of the two lists.
    
    Parameters:
    list1 (list): The first list.
    list2 (list): The second list.
    
    Returns:
    list: A list containing the intersection of list1 and list2.
    """
    return list(set(list1) & set(list2))

   
print(intersection_of_lists([1, 2, 3, 4], [3, 4, 5, 6]))
