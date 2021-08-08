def element_wise_comparison(Lst, T_num):
    """Get a list as long as Lst, where the value of it's element would be True if it is greater than T_num otherwise it would get False value.
    
    >>> element_wise_comparison([1, 2, 3, 4, 5], 3)
    [False, False, False, True, True]
    """
    # list comprehensions technique 
    return([elm > T_num for elm in Lst])

print(element_wise_comparison([1, 2, 3, 4, 5], 3))