def is_word_there(list_docs, keyword):
    """
    search the keyword inside of a list of documents . Each document is a string element of a list.
    desire output should show in which documents the keyword is mentioned. 
	in your search don't consider . and , also it should not be case sensitive. in addition the output should not refelect any words that contains the keyword (keyword without pre or pro fix)

    Example:
    list_docs = ["The is a new document.", "several books are here", "Book in here has a different color"]
    >>> is_word_there(list_docs, 'casino')
    >>> [2]
    """
    out_list=[]
    for element in list_docs:
        lst_words=element.split()
        normal = [word.rstrip('.,').lower() for word in lst_words]
        if keyword in normal:
            out_list.append(list_docs.index(element))
           
    return(out_list)
        
def search_multi_words(list_docs, keywords):
    """
    >>> list_docs = ["The is a new document.", "several books are here", "Book in here has a different color."]
    >>> keywords = ['book','the']
    >>> search_multi_words(list_docs, keywords)
    {'book': [2], 'the': [0]}
    """
    key_dict={}
    for key in keywords:
        key_dict[key]= is_word_there(list_docs,key)
    return key_dict
	
list_docs = ["The is a new document.", "several books are here", "Book in here has a different color."]
print(is_word_there(list_docs, 'book'))
print(search_multi_words(list_docs , ['book','the']))