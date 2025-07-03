def crypt(source, key):
    '''迴圈指定金鑰加解密'''
    from itertools import cycle
    result = ''
    temp = cycle(key)

    for ch in source:
        result = result + chr(ord(ch) ^ ord(next(temp)))  # ^ 的用途：位元異或（XOR)

    return result


source = 'Neil'
key = 'BRF'

print('Before Encrypted:'+source)
encrypted = crypt(source, key)
print('After Encrypted:'+encrypted)
decrypted = crypt(encrypted, key)
print('After Decrypted:'+decrypted)
