def reverse_integer(x):
    string = str(x)
    
    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])
      
