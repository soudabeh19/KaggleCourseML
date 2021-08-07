#!/usr/bin/env python

def all_salad_dressings( mustard, onion, ketchup):
    """Return if the client wants any salad dressing
    """
    pass
    return ketchup and mustard and onion
	
mustard = bool (input("Do you want mustard: "))
onion = bool (input("Do you want onion: "))
ketchup = bool (input("Do you want ketchup: "))

print("result of your request:", all_salad_dressings(mustard, onion, ketchup))