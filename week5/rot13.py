# takes in a letter, the caesar shift interval (13 in this case)
# and the size of the alphabet as 'mod_size'. in 'x % y', it's y.
def shift(start_letter,shift_size,mod_size):
    # i'm letting spaces pass through untouched to preserve 'words' of original text
    if start_letter != ' ':
        # note how i'm assigning variables here.  order matters.
        min_letter,max_letter = ord('a'),ord('z')
        alphabet_size = max_letter - min_letter
        resulting_number = ord(start_letter) - min_letter + shift_size
        resulting_number_in_range = min_letter + (resulting_number % mod_size)
        resulting_letter_in_range = chr(resulting_number_in_range)
        return resulting_letter_in_range
    else:
        return start_letter

def process_input(input_string):
    input_string_lc = input_string.lower()
    # can't modify a string, have to make a copy or turn into list
    input_list = list(input_string_lc)
    # using enumerate on input list so I can replace the index
    # of any value i don't want with an empty string, ''
    unwanted_strings = ["'",";",":","(",")","-","+","\\"]
    for index,element in enumerate(input_list):
        for unwanted in unwanted_strings:
            if element in unwanted:
                input_list[index] = ''
    return ''.join(i for i in input_list)

def display_text(processed_string):
    print ''.join(shift(i,SHIFT_SIZE,MOD_SIZE) for i in processed_string)


# convention is CAPS for any vars that are constants
SHIFT_SIZE=13
MOD_SIZE=26

min_letter = ord('a')
max_letter = ord('z')

input_string = raw_input('please enter some input text for encryption with ROT13:\n')
# remember,we need to filter the text before shifting it
processed_string = process_input(input_string)
display_text(processed_string)
