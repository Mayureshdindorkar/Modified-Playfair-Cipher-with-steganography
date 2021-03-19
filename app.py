# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from stegano import lsb
from ModifiedPlayfair import ModifiedPlayfair
import chardet

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import codecs


app = Flask(__name__)

UPLOAD_FOLDER = 'OriginalImages/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


################# Utility Functions #######################
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/senderurl')
def sender():
    return render_template('sender.html')

@app.route('/receiverurl')
def receiver():
    return render_template('receiver.html')

def generate_keys():
   # key length must be a multiple of 256 and >= 1024
   key = RSA.generate(1024)
   publickey = key.publickey()
   return key.exportKey(), publickey.exportKey() #returns privetkey and public key

@app.route('/generate_receiver_keys')
def generate_receiver_keys():
    ######### RSA started #############
        privatekey, publickey = generate_keys()
        print("Public Key: ", publickey)
        print("\n\nPrivate Key: ", privatekey)
        return render_template('display_recvr_keys.html', privatekey=privatekey, publickey=publickey)

@app.route('/receiverside_decrypt')
def receiver_decrypt():
    return render_template('receiver_decrypt.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

###########################################################

@app.route('/accept_sender_data', methods = ['GET', 'POST'])
def accept_sender_data():
    if request.method == 'POST':
        print('line 55')
        ############## SENDER SIDE CODE ###############

        f = request.files['uploaded_image']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return 'File format not supported!!'
        ####### Photo uploded ######
        print('line 58')
        plaintext = request.form['plaintext']
        print('Plaintext : ',plaintext)

        playfairkey = str(request.form['playfairkey'])
        print('Playfairkey : ',playfairkey)

        receiver_publickey = request.form['receiver_publickey']
        #print('Receiver publickey : ',receiver_publickey)
        ### All data collected from front end ########
        print('line 75')
        objModifiedPlayfair = ModifiedPlayfair() #creating obj of modified playfair class
        objModifiedPlayfair.getKey(playfairkey) # passing playfair key to that class
        objModifiedPlayfair.getPlainText(plaintext) # passing plaintext to that class
        objModifiedPlayfair.preparePairs()
        objModifiedPlayfair.generateKeyTable()
        objModifiedPlayfair.encrypt()
        cipher_from_playfair = objModifiedPlayfair.getCipherText()    ####### 1 (string)
        ######### Playfiar completed ############
        print('line 84')

        ########## RSA Started ################
        # encrypt() : Requires plaintext in bytes form only.

        print(type(receiver_publickey))
        print(receiver_publickey.encode('utf-8').replace(b'\\n', b'\n'))

        pobj = RSA.importKey(receiver_publickey.encode('utf-8').replace(b'\\n', b'\n'))
        pobj = PKCS1_OAEP.new(pobj)
        print('RSA Cipher of playfairkey : ',pobj.encrypt(playfairkey.encode('utf-8')))  #print bytes in string form
        rsacipher_for_playfairKey = pobj.encrypt(playfairkey.encode('utf-8'))  #### 2 (rsacipher_for_playfairKey -> unique type che bytes)
        
        ########## RSA completed ############
        print("RSA Cipher: ", rsacipher_for_playfairKey)
        print("\nRSA Cipher Length: ", len(rsacipher_for_playfairKey))
        print('line 100')

        ########## R transposition Started ####
        playfair_rsa_combined_cipher = cipher_from_playfair + "||||" + str(rsacipher_for_playfairKey) # bytes to string
        
        ptl = list(playfair_rsa_combined_cipher)
        fl = []
        bl = []
        # print("Length : ", len(ptl))
        for i in range(0,len(ptl)):
            if i%2 == 0:
                # print("i: ", i)
                fl.append(playfair_rsa_combined_cipher[i])
            else:
                # print("i: ", i)
                bl.insert(0,playfair_rsa_combined_cipher[i])

        templist = fl + bl
        ciphertext = ''.join(templist)
        ciphertext =  ciphertext[::-1]
        print('Combined (RSA + Playfair) Cipher Text:', ciphertext)
        ########## R transposition completed ###########
        print('line 122')

        ########### stegnography Encryption ###############
        imgname = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        secret = lsb.hide( imgname, ciphertext)
        
        imgextension = filename.split('.')[1]
        
        # Downloading final encrypted image
        print('line 137')
        uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
        secret.save('EncryptedImages/'+'EncryptedImg'+'.'+imgextension)
        return send_from_directory(directory= "EncryptedImages/", filename='EncryptedImg'+'.'+imgextension)

        #print('Encrypted image successfully downloaded at sender end!')
        #return render_template('index.html')

@app.route('/accept_receiver_data', methods = ['GET', 'POST'])
def accept_receiver_data():
    filename = ''
    if request.method == 'POST':

        #Reading the encrypted image
        f = request.files['encrypted_image']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join('EncryptedImages/', filename))
            print('Encrypted image successfully uploaded!')
        else:
            return 'File format not supported!!'

        receiver_privatekey = request.form['receiver_privatekey']
        print('receiver_privatekey:',receiver_privatekey)
        print('Line 161')

        ############# Decryption Process Started ##################
        imgextension = filename.split('.')[1]
        img_message = lsb.reveal("EncryptedImages//EncryptedImg"+'.'+imgextension)
        print('Retrived msg from image :',img_message)
        print('Line 163')

        # decrypting rohit transposition #
        ciphertext = img_message
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
        print("\n\nDecrypted Text after Rohit-Transposition : ", decryptedtext)
        print('Line 181')

        # splitting that combined cipher into rsacipher & playfair cipher
        cfpf, rsacfpf = decryptedtext.split("||||")   # Using it to separate rsacipher & playfair cipher
        print("Playfair Cipher: ", cfpf)        #str
        print("\n\n\nRSA Cipher: ", rsacfpf)
        print("Type of csafpf", type(rsacfpf))  #str
        print('Line 188')

        # Getting receiver's private key
        pobj = RSA.importKey(receiver_privatekey.encode('utf-8').replace(b'\\n', b'\n'))
        pobj = PKCS1_OAEP.new(pobj)
        print('Line 193')

        # Getting Playfair's Key
        rsacipher_for_playfairKey = pobj.decrypt(codecs.escape_decode(rsacfpf[2:len(rsacfpf) - 1])[0])
        print('PLayfair key:',rsacipher_for_playfairKey.decode('utf-8'))
        playfairkey = rsacipher_for_playfairKey.decode('utf-8')    #string
        print('Line 202')

        # Using this playfair key to decrypt the playfair cipher
        objModifiedPlayfair = ModifiedPlayfair() #creating obj of modified playfair class
        objModifiedPlayfair.getKey(playfairkey) # passing playfair key to that class
        objModifiedPlayfair.setCipherText(cfpf) # passing ciphertext to that class (cfpf==cipher for playfair)
        objModifiedPlayfair.generateKeyTable()
        decrypted_playfair_plaintext = objModifiedPlayfair.decrypt()
        print('Line 207')
        print('Final Decrypted playfair plaintext :',decrypted_playfair_plaintext)

        return render_template('Decrypted_msg.html', decrypted_playfair_plaintext = decrypted_playfair_plaintext)

#############################################################

if __name__ == '__main__':
   app.run(debug = True)