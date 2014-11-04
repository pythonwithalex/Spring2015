def palindrome(word):
    end = len(word)-1
    beginning = 0
    while beginning < end:
        if word[beginning] != word[end]:
            return False
        end = end - 1
        beginning = beginning + 1
    return True
# open file of words
f = open('words.txt')

# read the file as a list of lines, give it a name
wordlist = f.readlines()

#close the file
f.close()

#determine which substrings you don't care about
insignificant = ["\n",",","-",":","'"," "]

# remove newlines,spaces,apostrophes,dashes,colons
for num,word in enumerate(wordlist):
    for substring in insignificant:
        if substring in word:
            wordlist[num] = wordlist[num].replace(substring,'')

# test each word to see if it's a palindrome
# test method:
# 1) check first letter and last letter of each word
# 2) if they don't match, discard them

print "WORDS:",', '.join(i for i in wordlist)
print ""
for word in wordlist:
    if palindrome(word):
        print word
