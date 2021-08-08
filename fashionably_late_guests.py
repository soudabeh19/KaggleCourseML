def fashion_late_guest(guests_list, name):
    """Having a list of guests' name based on they arrivel time, check whether the guest is fashinably late 
	(a person who arrived after half of the guests are already in the party but he/she is not the last person yet. Expect True for the following sample
    """
    len_mid = round(len(guests_list)/2)
    idx_name = guests_list.index(name)
    if len_mid <= idx_name < len(guests_list)-1:
        return True
    return False


print(fashion_late_guest (['Alice', 'Bob', 'Sarah', 'John', 'Ana', 'Scott', 'Eric'] , 'Ana'))