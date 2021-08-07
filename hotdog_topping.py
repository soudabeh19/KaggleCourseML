#!/usr/bin/env python

def all_salad_dressings( mustard, onion, ketchup):
    """Return True when the client wants all salad dressings
    """
    pass
    return ketchup and mustard and onion
	
mustard = bool (input("Do you want mustard: "))
onion = bool (input("Do you want onion: "))
ketchup = bool (input("Do you want ketchup: "))

def just_one_sauce(mustard, onion, ketchup):
    """Return if the client wants just ketchup or just mustard, not both of them.
    """
    pass
    return (ketchup != mustard) and onion

print("Result of your all toppings request:", all_salad_dressings(mustard, onion, ketchup))
print("Result of your either ketchup or mustard toppings request:", just_one_sauce(mustard, onion, ketchup))