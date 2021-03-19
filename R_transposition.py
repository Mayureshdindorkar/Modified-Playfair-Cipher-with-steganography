

plaintext = input('Enter the plain text :')
ptl = list(plaintext)
fl = []
bl = []

for i in range(0,len(ptl)):
    if i%2 == 0:
        fl.append(plaintext[i])
    else:
        bl.insert(0,plaintext[i])

templist = fl + bl
ciphertext = ''.join(templist)
ciphertext =  ciphertext[::-1]
print('Cipher Text:',ciphertext)



# ciphertext = input('Enter ciphertext: ')
ciphertext = ciphertext[::-1]
startptr = 0
endptr = len(ciphertext) - 1
decryptedtext = ""

while startptr <= endptr:
    if startptr != endptr:
        decryptedtext = decryptedtext + ciphertext[startptr] + ciphertext[endptr]
    else:
        decryptedtext = decryptedtext + ciphertext[startptr]
    startptr = startptr + 1
    endptr = endptr - 1


print("Decrypted Text: ", decryptedtext)