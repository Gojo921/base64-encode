import base64


def encrypt_pass(userpassword):
    encoded_bytes = base64.b64encode(userpassword.encode())
    print( encoded_bytes)

userpassword = input('Enter your password: ')

encrypt_pass(userpassword)