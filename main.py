import random

l_case = "abcdefghijklmnopqrstuvwxyz"
u_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*^-_(){}[]"

comp_pass = l_case + u_case + numbers + symbols
length = 8

password = "".join(random.sample(comp_pass, length))
print("Password: {}".format(password))
