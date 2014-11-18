#note: try with a deque later!

# PART 1 - The ROT13 Shift

# Note on ROT13 and ciphers in general

# to achieve a ROT13 cipher, we need to move each input letter up 13 characters.
# This means we need to turn letters into numbers. This is a common task in encrypting text:
# You take a word, break it into its letters, and translate them into numbers to do some sort of
# computation on them.  When you're done, you translate each resulting number back into a letter.

# the issues in this problem:
# 1) the alphabet is 26 letters.  we usually number them 1-26 if we have to number them.
#  but here, we give them 0 - 25 to conform to the 0-based notion of position.
# 2) there is no character set that is just a lowercase alphabet, that's wasteful
# we are using an ASCII alphabet, which has everything from the null character (you don't see it)
# to letters, numbers, and meta (control) characters such as '\x7f' (the delete char)

# so: Part of our task is taking into account that the letters we want are just a subset of a 
# larger character set.  we will need to do some 'shifting' between our natural way of thinking of
# 'a' - 'z' in terms of numbers and their real representation in the standard ASCII character set.


# we can use the ord() function to get a letter's corresponding 'number'.
# ord stands for 'ordinal', which means 'positional'

# In our case, we are looking to see where 'a','b','c',etc fall in the character set
# available to us in Python.  Ascii is a 7-bit character set, meaning it can hold a total 
# of 2^7 or 128 characters.  It ranges from 0 to 127.  

#Let's see where 'a' and 'z' fall.

#print ord('a')
# 97
#print ord('z')
# 122

# See? Our first letter is at position 97, and our last letter is at position 122.
# So we need to account for the fact that 'a' isn't 0 and 'z' isn't 25.


# 97 thru 122 is our range ... so get your range function out!

#for i in range(ord('a'),ord('z')+1):
#    print i

# Why don't we think of an equation that expresses the output number, given the input number

# endNum = startNum + 13
# ok, that expresses the basic idea.  

# Q: Why is that not complete?

# We need to keep it in range of the alphabet. If we shift anything after 'm' by 13, we are 
# out of range.  We'll get back characters we don't want, like '{', '|', etc...

# remember the modulo operator? That will help us keep the number in range
# (startNum + 13)%26

# this keeps our numbers in range of the alphabet's span (0-25), but...

# Q: Why is this not our final method?
# well, if we do the following:

#for i in range(ord('a'),ord('z')+1):
#    print (i+13)%26    

# we get 0 - 25.  That's in the 'naturalistic' range we are used to thinking of as 'a-z', 
# but not the range we want.  We need to account for the fact that 'a' is 97, no 0.  

# Let's refer to the gap between the position of the first ASCII character and 'a' as ...
numberGap = 97

# and let's call the ROT13 defined shift ...
rot13Shift = 13

# now, calculating the 'encryption' of each char can be a little tricky.  
# Because it is more natural to think of the alphabet's characters as 
# being 0-25, not 97-122, I will essentially 'normalize' the letters
# to which 'a' - 'z' correspond when figuring out what they map to.

# here's a concrete example.  This is how I, myself, did this problem.
# 'n' is the 13th letter in the alphabet, so we know it should give us 'a'.
# Why? 'n' + the ROT13 shift (+13) is 26. 26%26 gives us 0, which we want to correspond to 'a'.
# so 'n' maps to 'a'.

# 'n' is 110 in ASCII.  if I subtract numberGap from 110, I get 13. 
# 13 is a much more intuitive way of thinking of 'n' than 110. See why i'm using it now?


print "\n%s\n%s\n" % ("Method A","~~~~~~~~")
#now, for each letter between 'a' and 'z', inclusive
for num in range(ord('a'),ord('z')+1):
    #call each num your inputNum
    inputNum = num
    # create a new variable for your input number as if it were in the more 'natural' range, 0-25
    inputNumMinusGap = inputNum - numberGap
    # now shift it by 13 and apply the modulo to keep it between 0 and 25 
    inputAfterROT13Shift = inputNumMinusGap + rot13Shift
    inputAfterROT13ShiftInRange = inputAfterROT13Shift%26
    # remember to add the gap back in so that the output letter is the correct ASCII char
    outputNum = inputAfterROT13ShiftInRange + numberGap
    # print it all out to verify
    print chr(inputNum), " => ", chr(outputNum)

    # The above variable names are hyper-expressive for demonstrative purposes. 
    # Below is how I did this myself.  You may prefer it that way, it's up to you.

print "\n%s\n%s\n" % ("Method B","~~~~~~~~")
for num in range(ord('a'),ord('z')+1):
    inputNum = num
    outputNum = (inputNum - numberGap + rot13Shift)%26 + numberGap
    print chr(inputNum), " => ", chr(outputNum)


### PART 2 - The Encryption and Decryption



# We are going to use dictionaries so that we can use an input letter as a key and ROT13 shifted
# letter as a value

# NOTE: in your reading about ROT13 I hope you came across what is the essential 
# reason for its insecurity as a cipher: 
# it's 'symmetrical' as they say.  The same algorithm to encrypt will decrypt a message.

print "\n%s\n%s\n" % ("Full Program","~~~~~~~~~~")

# our encryption dictionaries
encrypt, decrypt = {},{}

# fill them with the appropriate keys & values
for num in range(ord('a'),ord('z')+1):
    inputNum = num
    outputNum = (inputNum - numberGap + rot13Shift)%26 + numberGap
    encrypt[chr(inputNum)]  = chr(outputNum)
    decrypt[chr(outputNum)] = chr(inputNum)

# let's print them to make sure we did this right
print encrypt 
print decrypt

#huh, they look similar. Let's see if their values are the same (using '==', not 'is') :
if (encrypt == decrypt):
    print "\nThese dictionaries have the same values."
    print "Maybe Caesar used this cipher, but I'm sure not going \nto use it to keep my secrets!"

# so, let's not bother with two dictionaries
# rename encrypt to rot13
rot13 = encrypt
#delete decrypt
del decrypt



# get the inputText to encrypt
inputText = raw_input("Please enter text to be encrypted with ROT13:\n")
outputText = []

for letter in inputText:
    if letter.isalpha():
        encryptedLetter = rot13[ letter.lower() ]
        outputText.append(encryptedLetter)
    elif letter is ' ':
            #we want to keep the spacing
            outputText.append(letter.lower())
    
print "Your encrypted string is:\n %s" % ''.join(i for i in outputText)








