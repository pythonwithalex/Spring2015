import sys

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
if len(sys.argv) == 2:
    f=open(sys.argv[1])
else:
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
# 1) set two indexes, one to the beginning and one to the end of the word
# 2) if those match, increment index of beginning, decrement index of ending
# 3) do this while beginning index is less than ending index, so you don't double count
# 4) if they don't match, return false

print "of the following words:\n\n",', '.join(i for i in wordlist),"\n\nthese are palindromes:\n"

for word in wordlist:
    if palindrome(word):
        print word
