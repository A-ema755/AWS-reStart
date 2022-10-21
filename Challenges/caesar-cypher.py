def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    while True:
      strintToEncrypt = input("Input a message to encrypt: ")
      conf = input("To confirm input: Yes")
      if conf == "Yes":
        return strintToEncrypt
      else:
        print("No confirmation")
    
def getCipherKey():
    while True:
      key = input("Input an encryption key from 1 - 25: ")
      if 0 < int(key) < 26:
        return key
      else:
        print("Non valid key")
        
    
def encryptMessage(message, key, alphabet):
    encryptedMessage=""
    uppercaseMessage=""
    uppercaseMessage= message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        #print(position)
        newPosition = position + int(key)
        #print(newPosition)
        if currentCharacter in alphabet:
          encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
          encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, key, alphabet):
    key = -1 * int(key)
    return encryptMessage(message, key, alphabet)

def runCaesar():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myKey = getCipherKey()
    print(myKey)
    myEncryptedMessage = encryptMessage(myMessage, myKey, myAlphabet2)
    print(myEncryptedMessage)
    myDecriptedMessage = decryptMessage(myEncryptedMessage, myKey, myAlphabet2)
    print(myDecriptedMessage)

runCaesar()