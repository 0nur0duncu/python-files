#data encryption
#-----------------------

#reverse encription
data = input("Please enter a text....: ") #python
encrypt_data = ""
for i in range(len(data),0,-1):
    encrypt_data =encrypt_data +data[i-1]

print(encrypt_data) #nohtyp

#caesar encryption
def encript(message,step):
    result = ""
    for i in range(len(message)):
        char =message[i]
        if char.isupper():
            result += chr((ord(char)+step-65)%26 +65)
        else:
            result +=chr((ord(char)+step-97)%26 +97)
    return result

message = 'KRIPTOLOGY'
step = 5
print(encript(message,step)) #PWNUYTQTLD

array = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(array)):
    transform = ''
    for char in message:
        if char in array:
            num = array.find(char)
            num -= i
            if num<0:
                num +=len(array)
            transform += array[num]
        else:
            transform += char
    print('Brute Force step #%s: %s' % (i,transform)) #Brute Force step #0: KRIPTOLOGY

#ROT13 encryption
import codecs
encript_message = codecs.encode(message,'rot_13')

print(encript_message) #XEVCGBYBTL
decoding = codecs.decode(encript_message,'rot_13')
print(decoding) #KRIPTOLOGY

#BASE64 encryption
import base64

encript_message =base64.b64encode(b'Car') #with b
print(encript_message) #b'S1JJUFRPTE9HWQ=='b'Q2Fy'
decoding =base64.b64decode(encript_message)
print(decoding) #b'Car'
