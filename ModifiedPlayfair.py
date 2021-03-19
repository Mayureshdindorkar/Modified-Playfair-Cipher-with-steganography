# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:15:52 2021

Topic: Modified Playfair Algorithm using matrix 4 * 19.

@author: 
Shalakha Vijaykumar Bang  BECOC305
Rohit Balasaheb Bang      BECOC306
Piyush Rajendra Chaudhari BECOC311
Mayuresh Rajesh Dindorkar BECOC320

"""
import re


class ModifiedPlayfair:
    def __init__(self):
        self.key = ""
        self.plain_text = ""
        self.cipher_text = ""
        self.decrypted_text = ""
        self.keyTable = [[str(" ") for i in range (0, 19)] for j in range(0, 4)]
        self.consideredSymb = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',' ',',', '.', '!', '?', '"',"'", '&', ':', ';', '%', '@', '-','^']
    
    def getKey(self, paramkey):
        self.key = paramkey.strip()
        self.key = re.sub("[^A-Za-z0-9 ,.!?\"\'&:;%@-]", "", self.key)
        
    def getPlainText(self, paramplaintext):
        self.plain_text = paramplaintext.strip()
        self.plain_text = re.sub("[^A-Za-z0-9 ,.!?\"\'&:;%@-]", "", self.plain_text)
        
    def generateKeyTable(self):
        #4 * 19
        indx = 0
        i = 0
        j = 0

        while (True):
            self.keyTable[i%4][j%19] = self.key[indx]
            j += 1
            if j%19 == 0:
                i += 1
            indx += 1  
            if (indx >= len(self.key)):
                break
            
        indx = 0
        
        remainingConsideredSymb = []
        
        for x in self.consideredSymb:
            if x not in self.key:
                remainingConsideredSymb.append(x)
            
        while (True):
            self.keyTable[i%4][j%19] = remainingConsideredSymb[indx]
            j += 1
            if j%19 == 0:
                i += 1
            indx += 1
            if (indx >= len(remainingConsideredSymb)):
                break
    

    def printKeyTable(self):
        for row in range(0, 4):
            for col in range(0, 19):
                print(self.keyTable[row][col], end = " ")
            print("\n")
            
   
    def preparePairs(self):
        #handling doubles
        indx = 1
        while True:
            if self.plain_text[indx] == self.plain_text[indx - 1]:
                self.plain_text = self.plain_text[:indx] + '^' + self.plain_text[indx:]
            
            indx += 1
            if indx == len(self.plain_text):
                break

        if len(self.plain_text) % 2 != 0:
            self.plain_text += '^'

    def searchPosition(self, num1, num2):
        coordinates = [0, 0, 0, 0]
        
        for row in range(0, 4):
            for col in range(0, 19):
                if self.keyTable[row][col] == num1:
                    coordinates[0] = row
                    coordinates[1] = col
                if self.keyTable[row][col] == num2:
                    coordinates[2] = row
                    coordinates[3] = col
        return coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    
    def encrypt(self):
        
        for indx in range(0, len(self.plain_text), 2):
            x1, y1, x2, y2 = self.searchPosition(self.plain_text[indx], self.plain_text[indx + 1])
            if x1 == x2:
                self.cipher_text += self.keyTable[x1][(y1 + 1) % 19]
                self.cipher_text += self.keyTable[x2][(y2 + 1) % 19]                
            elif y1 == y2:
                self.cipher_text += self.keyTable[(x1 + 1) % 4][y1]
                self.cipher_text += self.keyTable[(x2 + 1) % 4][y2] 
            else:
                self.cipher_text += self.keyTable[x1][y2]
                self.cipher_text += self.keyTable[x2][y1]
    
    def printCipherText(self):
        print("Cipher Text:", self.cipher_text)
    
    def setCipherText(self,paramciphertext):
        self.cipher_text = paramciphertext

    def getCipherText(self):
        return self.cipher_text
    
    def decrypt(self):
        
        for indx in range(0, len(self.cipher_text), 2):
            x1, y1, x2, y2 = self.searchPosition(self.cipher_text[indx], self.cipher_text[indx + 1])
            if x1 == x2:
                self.decrypted_text += self.keyTable[x1][(y1 - 1) % 19]
                self.decrypted_text += self.keyTable[x2][(y2 - 1) % 19]                
            elif y1 == y2:
                self.decrypted_text += self.keyTable[(x1 - 1) % 4][y1]
                self.decrypted_text += self.keyTable[(x2 - 1) % 4][y2] 
            else:
                self.decrypted_text += self.keyTable[x1][y2]
                self.decrypted_text += self.keyTable[x2][y1]
                
        self.decrypted_text = self.decrypted_text.replace('^','')
        return self.decrypted_text
    
    
    def printDecryptedText(self):
        print("Decrypted Text:", self.decrypted_text)    
    
#if __name__ == "__main__":
    
#    objModifiedPlayfair = ModifiedPlayfair()
#    objModifiedPlayfair.getKey()
#    objModifiedPlayfair.getPlainText()
#    objModifiedPlayfair.preparePairs()
#    objModifiedPlayfair.generateKeyTable()
#    objModifiedPlayfair.printKeyTable()
#    objModifiedPlayfair.encrypt()
#    objModifiedPlayfair.printCipherText()
#    objModifiedPlayfair.decrypt()
#    objModifiedPlayfair.printDecryptedText()
    
    
    


