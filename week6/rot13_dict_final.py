
# ROT13 cipher using dictionaries
# To be looked at after 'PWP/week6/rot13_dict.py'

def generateCipherTable(numberGap=97,shift=13, startChar='a',endChar='z'):
    cipherTable = {}
    for num in range(ord(startChar),ord(endChar)+1):
        inputNum = num
        outputNum = (inputNum - numberGap + shift)%26 + numberGap
        cipherTable[chr(inputNum)]  = chr(outputNum)
    return cipherTable

def applyCipher(inputText,cipherTable):
    outputText = []
    for letter in inputText:
        if letter.isalpha():
            encryptedLetter = cipherTable[ letter.lower() ]
            outputText.append(encryptedLetter)
        elif letter is ' ':
                #we want to keep the spacing
                outputText.append(letter.lower())
    return outputText

def getInputText():
    inputText = raw_input("Please enter text to be encrypted or decrypted with ROT13:\n")
    return inputText

def main():
    cipherTable = generateCipherTable()
    inputText = getInputText()
    outputText = applyCipher(inputText,cipherTable)
    print "Your resulting text is:\n%s" % ''.join(i for i in outputText)

main()
