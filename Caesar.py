'''
Caesar cipher program that can handle exceptional cases. 
To do: Add comments
'''



def caesar(key, message):
    import string
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new = ''
    for x in message:
        if x != ' ' and x.isalpha():
            if x.isupper() == True:
                ind = ascii_uppercase.index(x)

                new += ascii_uppercase[(ind + key) % 26]

            elif x.islower() == True:
                ind = ascii_lowercase.index(x)
                new += ascii_lowercase[(ind + key) % 26]
        else: new += x
    return new
