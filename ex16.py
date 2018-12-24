import random

user = input("Choose how strong do you wanna have a password? Type E(easy) M(middle) S(strong)")

password = " "
count = 0

weak = 'abcdefghijklmnopqrstuvwxyz123'
medium = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234'
strong = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-<>";:/?'

if user == "E":
    password = ' '.join(random.sample(weak,6))
elif user == "M":
    password = ' '.join(random.sample(medium,8))
elif user == "S":
    password = ' '.join(random.sample(strong,12))

print("Your password is: ",password)