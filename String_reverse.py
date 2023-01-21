def str_rev(str_in):
    '''
    This function reverses an entered string
    '''

    str_rev_out = str_in[::-1]
    return str_rev_out

str_in = input("Enter a string to be reversed: ")
print(str_rev(str_in))