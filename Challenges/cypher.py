def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    strintToEncrypt = input("Input the message to encrypt: ")
    return strintToEncrypt
    
def getCipherKey():
    key = input("Input the encryption key from 1 - 25: ")
    return key
    
def encryptMessage(message, key, alphabet):
    encryptedMessage=""
    uppercaseMessage=""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(key)
        if currentCharacter in alphabet:
          encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
          encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, key, alphabet):
    key = -1 * int(key)
    return encryptMessage(message, key, alphabet)
    


print(encryptMessage("Input", "5", "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(dencryptMessage("NSLWJXJ", "5", "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"))
