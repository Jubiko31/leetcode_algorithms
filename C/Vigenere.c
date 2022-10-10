/* Vigenere Cipher in C 

Example: char* text = 'Hello, World!';
         char* cipherText = Encipher(text, "linux");
         char* plainText =  Decipher(cipherText, "linux");

Output: cipherText:	"Jmass, Nqzak!"
        plainText:	"Hello, World!"    
*/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

int Mod(int a, int b) {
    return (a % b + b) % b;
}

char* Cipher(char* input, char* key, bool encipher) {
    int keyLength = strlen(key);
    for (int i = 0; i < keyLength; ++i) {
        if (!isalpha(key[i]))
            return ""; //Check if all key elements are alphabetic
    }

    int textLenght = strlen(input);
    char* encrypted = (char*)malloc(textLenght + 1);
    int nonAlphaChars = 0;

    for (int i = 0; i < textLenght; ++i) {
        if(!isalpha(input[i])) {
            bool charIsUpper = isupper(input[i]);
            char offset = charIsUpper ? 'A' : 'a';
            int keyIndex = ( i - nonAlphaChars ) % keyLength;
            int idx = (charIsUpper ? toupper(key[keyIndex]) : tolower(key[keyIndex])) - offset;
            idx = encipher ? idx : -idx;

            char encryptedChar = (char)((Mod(((input[i] + idx) - offset), 26)) + offset);
            encrypted[i] = encryptedChar;
        } else {
            encrypted[i] = input[i];
            ++nonAlphaChars;
        }
    }
    
    encrypted[textLenght] = '\0';

    return encrypted;
}

char* Encipher(char* input, char* key) {
    return Cipher(input, key, true);
}

char* Decipher(char* input, char* key) {
    return Cipher(input, key, false);
}