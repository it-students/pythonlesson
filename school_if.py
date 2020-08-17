from random import choice
alphabet = [chr(c) for c in range(ord('a'),ord('z') + 1)]
for _ in iter(input, choice(alphabet)):
    print('NG')
print('OK')