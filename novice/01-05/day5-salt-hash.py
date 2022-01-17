# import imp
# import os 
# import hashlib
# import imp

# salt = os.urandom(32)
# password = "qwerty123"

# key = hashlib.pbkdf2_hmac(
#     'sha256',
#     password.encode('utf-8'),
#     salt,
#     100000, 
#     dklen=128
# )
# print(key)

# import os
# import hashlib

# # Example generation
# salt = os.urandom(32)
# mypassword = 'ppkmk1m1m1m122'
# new_key = hashlib.pbkdf2_hmac('sha256', mypassword.encode('utf-8'), salt, 100000)

# # Store them as:
# storage = salt + new_key 

# # Getting the values back out
# salt_from_storage = storage[:32] # 32 is the length of the salt
# key_from_storage = storage[32:]

# if new_key == key:
#     print('password is correct')
# else:
#     print('password is incorrect')