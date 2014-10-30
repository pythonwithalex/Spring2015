# a text formatting library in progress

def columnFormat(width,data):
    ''' columnFormat takes in an INT 'width' and a LIST of strings, 'data'
   and formats it for standard output according to the width value.'''
    string_elements = []
    for i in data:
        buffer = (width-len(i))*' '
        string_elements.append(i)
        string_elements.append(buffer)
    return ' '.join(i for i in string_elements)
