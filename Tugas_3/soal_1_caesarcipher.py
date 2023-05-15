def encryptor(message,s):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if (char.isupper()):
         result += chr((ord(char) + s - ord('A')) % 26 + ord('A'))
        if (char.islower()):
         result += chr((ord(char) + s - ord('a')) % 26 + ord('a'))
    return result.upper()

message = 'Meet me by the rose bushes tonight.'
s = 4

print ("Plain Text : " + message)
print ("Shift pattern : " + str(s))
print ("Cipher: " + encryptor(message,s))
