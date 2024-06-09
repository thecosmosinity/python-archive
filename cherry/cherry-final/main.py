import socket
import base64
import random
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

cwd = os.getcwd()
cwdcrypt = str(cwd)
cwd_crypter = cwdcrypt.encode("ascii")
cwd_bytes = base64.b64encode(cwd_crypter)
cwd_encrypted = (cwd_bytes.decode("ascii"))

string = str(ip)
string_bytes = string.encode("ascii")
base64_bytes = base64.b64encode(string_bytes)
base64_string = base64_bytes.decode("ascii")

captcha = random.randint(1000, 9999)
print("Welcome to Cherry!")
print("Captcha = " + str(captcha))
randominput = int(input("Please enter the captcha: "))

if randominput == captcha:
    print("Captcha is correct!")
    print(base64_string)
    print(cwd_encrypted)
    input("Press enter to continue... ")
else:
    print("Captcha is invalid!")
