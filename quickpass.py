import string
import random

def p(s = 16, c=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(c) for _ in range(s))
print(p(int(input('Password Length: '))))
