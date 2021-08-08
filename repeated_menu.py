def repeated_menu(lst_meal):
    """ Check if a same meal has been served two consecutive days if so return True otherwise False.
    """
            
    return any([lst_meal[i] == lst_meal[i+1] for i in range (0, len(lst_meal)-1)])

lst_meal = ['Pasta', 'Pizza', 'Egg', 'Egg', 'Bacon', 'Fish']
print(repeated_menu(lst_meal))