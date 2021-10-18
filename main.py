import characterChange as _cc_
from cryptography.fernet import Fernet

class sneakyWordsClass:

  def __init__(self, p, crypto, encrypted, decrypted):
    key = Fernet.generate_key()
    self.userpass = p
    self.crypto = Fernet(key)
    self.encrypted = encrypted
    self.decrypted = decrypted

  def changeCharacters(self, userinput):
    addTogether = ""
    input = str(userinput).lower()
    for i in range(0, len(input)):
       addTogether += (_cc_.cc.characters(self,input[i]))

    self.userpass = addTogether

    return self.userpass

  def encrypt(self, c):
    encoded = bytes(c,'UTF-8')

    self.encrypted = self.crypto.encrypt(encoded)
    return self.encrypted

  def decrypt(self):
    message = ""
    decoded = self.crypto.decrypt(self.encrypted)
    decrypted_list = list(sneakyWordsClass.chunk(str(decoded.decode())))


    for i in range(len(decrypted_list)):
      char_value = list(_cc_.cc.getchars(self).values()).index(decrypted_list[i])
      message += list(_cc_.cc.getchars(self).keys())[char_value]
    
    print(f"Changed characters: {decoded.decode()}")
    self.decrypted = message
    return self.decrypted

  def connectEncrypt(self,words):
    values  = sneakyWordsClass.changeCharacters(self, words)

    return sneakyWordsClass.encrypt(self,values)

  def connectDecrypt(self,words):
   

    return self.decrypted
  
  def chunk(word):
    return [word[i:i+3] for i in range(0, len(word), 3)]

  def menu():
    print( "Welcome to the Encoder/Decoder") 

    

  #sneakyWordsClassProperty = property(__init__)

sneakyWords = sneakyWordsClass("","", b"", b"") # sets the class with an empty string
words = "Hello, Im Jarod"

print (sneakyWords.connectEncrypt(words))

print(sneakyWords.decrypt())

