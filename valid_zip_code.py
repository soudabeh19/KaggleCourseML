def valid_zip_code(z_code):
    """Check whether the user's insert string is a valid five_digit zip code.
    """
    pass
    return z_code.isnumeric() and len(z_code)== 5
	
print('''12f34 : {}
123 :{}
12345 :{}'''
.format(valid_zip_code('12f34'), valid_zip_code('123'), valid_zip_code('12345')) )
