import random
import string

# use all letters, digits and special signs as a 'character' variable
characters = string.ascii_letters + string.digits + '!@#$%^&*()~|":<>?[]'
password = ''

# while password lenght is smaller than 14 add random character from 'character' variable
while len(password) < 14:
    password = password + random.choice(characters)
print(password)