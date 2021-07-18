import hashlib

file1 = 'a.txt'
file2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(file2, 'rb').read())

print(f' Hash value of {file1} is:', hash1.hexdigest())
print(f' Hash value of {file2} is:', hash2.hexdigest())

if hash1.digest() != hash2.digest():
    print(f' The file1: {file1} is not equal to {file2}')
    
else:
    print('Files are the same.')