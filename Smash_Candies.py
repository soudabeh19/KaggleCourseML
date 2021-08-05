#!/usr/bin/env python
def to_smash(total_candies , num_friend = 3 ):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return (total_candies % num_friend)

num_Candies = int(input("Total Number of Candies:"))
print(to_smash(num_Candies))