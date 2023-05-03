### This is the Vigenere Cypher in Python
### With advanced validations
### Encrypt and Decrypt strings, lists and tuples
### Made by @Juba31

import re
regex = "^[A-Za-z0-9]*$"

CIPHER = 'abcdefghijklmnopqrstuvwxyz0123456789'

letter_to_index = dict(zip(CIPHER, range(len(CIPHER))))
index_to_letter = dict(zip(range(len(CIPHER)), CIPHER))

def encrypt(message, key):
    #Final encrypted message
    encrypted = ''
    #Split message to the length of the key
    splited = [message[array:array + len(key)] for array in range(0, len(message), len(key))]
    #Loop through splited chunks:
    for splited_chunk in splited:
        iterator = 0
        #Loop through each letter of array
        for letter in splited_chunk:
            #Get letter index in CIPHER
            idx = (letter_to_index[letter] + letter_to_index[key[iterator]]) % len(CIPHER)
            #Convert letters to encrypted dictionary indexes
            encrypted += index_to_letter[idx]
            #Rause iterations
            iterator += 1
    
    return encrypted.upper()

#Do the same but reversed
def decrypt(encrypted, key):
    decrypted = ''
    splited = [encrypted[array:array + len(key)] for array in range(0, len(encrypted), len(key))]
    for splited_chunk in splited:
        iterator = 0
        #Loop through each letter of array
        for letter in splited_chunk:
            #Get letter index in CIPHER
            idx = (letter_to_index[letter] - letter_to_index[key[iterator]]) % len(CIPHER)
            #Convert letters to encrypted dictionary indexes
            decrypted += index_to_letter[idx]
            #Rause iterations
            iterator += 1
            
    return decrypted

#Cypher for Strings
def VIGENERE_CYPHER():
    #Choose whether decrypt or encrypt
    action = input('Do you want to encrypt(E) or decrypt(D) the message? ').lower()
    #Encryption
    if (action == 'e' or action == 'encrypt'):
        message = input('Enter your secret message: ').lower().replace(' ', '')
        key = input("Key to encrypt message: ").lower().replace(' ', '')
        #validation for invalid values
        if (len(message) != 0 and len(key) != 0):
            print('Encrypted message: ', encrypt(message, key))
        else: 
            print('Invalid values. Try better.')
            VIGENERE_CYPHER()
    #Decryption
    elif(action == 'd' or action == 'decrypt'):
        encrypted = input('Enter message you want to decypher: ').lower().replace(' ', '')
        key = input("Key to decypt your message: ").lower().replace(' ', '')
        #validation for invalid values
        if (len(encrypted) != 0 and len(key) != 0):
            print('Decrypted message: ', decrypt(encrypted, key))
        else: 
            print('Invalid values. Try better.')
            VIGENERE_CYPHER()   
    #Invalid parameters
    else:
        print("Please enter valid action")
        VIGENERE_CYPHER()

#Cypher for lists(multiple messages with one key)  
def VIGENERE_FOR_LIST():
    encryptedList = []
    decryptedList = []
    _list = []
    numberOfElements = int(input('Enter number of elements in your list: '))
    if numberOfElements: print("Enter elements. Elements must only contain LATIN letters and numbers:")
    for idx in range(0, numberOfElements):
        element = str(input().lower().replace(' ', ''))
        if element != '' and bool(re.match(regex, element)):
            _list.append(element)
        else:
            print('Invalid input!')
    
    if (len(_list) == numberOfElements):
        print('Your list was saved successfully!')
        key = str(input('Enter a key for cypher: ')).lower().replace(' ', '')
        action = input('Now please choose do you want to encrypt(E) or decrypt(D) the message? ').lower()
    else: 
        print('List is empty or Invalid values. Try again!')
        VIGENERE_FOR_LIST() 
    #Encrypt
    if (action == 'e' or action == 'encrypt'):
        for message in _list:
            encryptedList.append(encrypt(message, key))      
        print(encryptedList)
    #Decryption
    elif(action == 'd' or action == 'decrypt'):
        for message in _list:
            decryptedList.append(decrypt(message, key))  
        print(decryptedList)
    #Invalid parameters
    else:
        print("Please enter valid action.")
        VIGENERE_FOR_LIST()

def VIGENERE_FOR_TUPLE():
    encryptedTuple = ()
    decryptedTuple = ()
    _tuple = ()
    numberOfElements = int(input('Enter number of elements in your tuple: '))
    if numberOfElements: print("Enter elements. Elements must only contain LATIN letters and numbers:")
    for idx in range(0, numberOfElements):
        element = str(input().lower().replace(' ', ''))
        if element != '' and bool(re.match(regex, element)):
            _tuple += element,
        else:
            print('Invalid input!')
    
    if (len(_tuple) == numberOfElements):
        print('Your tuple was saved successfully!')
        key = str(input('Enter a key for cypher: ')).lower().replace(' ', '')
        action = input('Now please choose do you want to encrypt(E) or decrypt(D) the message? ').lower()
    else: 
        print('List is empty or Invalid values. Try again!')
        VIGENERE_FOR_TUPLE()
    #Encrypt
    if (action == 'e' or action == 'encrypt'):
        for message in _tuple:
            encryptedTuple += encrypt(message, key),
        print(encryptedTuple)
    #Decryption
    elif(action == 'd' or action == 'decrypt'):
        for message in _tuple:
            decryptedTuple += decrypt(message, key), 
        print(decryptedTuple)
    #Invalid parameters
    else:
        print("Please enter valid action.")
        VIGENERE_FOR_TUPLE()
    
        
def main():
    _type = input('Do you want to cypher String(S) or List(L) or Tuple(T): ').lower()
    if _type == 's' or _type == 'string':
        VIGENERE_CYPHER()
    elif _type == 'l' or _type == 'list':
        VIGENERE_FOR_LIST()
    elif _type == 't' or _type == 'tuple':
        VIGENERE_FOR_TUPLE()
    else:
        print('Please enter valid type.')
        main()

#Let's Encrypt/Decrypt 
main()