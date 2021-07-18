import hashlib
import string


string = input( "type the txt to be hashed")

menu = int(input( ''' ## MEN - Choose the HASH type
             1) MD5
             2) SHA1
             3) SHA256
             4) SHA512
             Type the Hash number to be generated:
             '''
             ))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print('MD5 hs for the strin: ', string, 'is: ', result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print('MD5 hs for the strin: ', string, 'is: ', result.hexdigest())
    
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print('SHA256 hash for the string: ', string, 'is: ', result.hexdigest())

elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print('SHA512 hash for: ', string, 'is: ', result.hexdigest())    

else:
    print('Something went worng.')