def columnFormat(width,data):
    # prints a correctly formatted line from a sequence
    # using the equation "whitespace buffer equals column size minus string length"
    string_elements = []
    for i in data:
        buffer = (width-len(i))*' '
        string_elements.append(i)
        string_elements.append(buffer)
    return ' '.join(i for i in string_elements)

