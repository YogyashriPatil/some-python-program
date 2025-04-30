import random
import string

passlen=int(input("Enter the length you want to generate : "))
'''s=string.digits
s=s+string.ascii_letters
s=s+string.punctuation'''

s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_"
p="".join(random.sample(s,passlen))
print(p)