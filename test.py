import hashlib
from Crypto.Cipher import AES

key = 'suck my dickhole'
IV = 16*  '\x00'
mode = AES.MODE_CBC
encrypter = AES.new(key, mode, IV=IV)

text = 'hey sherilyn'

l = len(text)
if l%16 != 0:
	text = text + ' '*(16-l%16)

ciphertext = encrypter.encrypt(text)

decryptor = AES.new(key, mode, IV=IV)
plain = decryptor.decrypt(ciphertext)

plain = plain.strip()

print(plain)
