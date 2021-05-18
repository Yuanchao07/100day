import random

all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_code(code_len=4):

    code = ''
    for _ in range(code_len):
        index = random.randrange(0, len(all_chars))
        code += all_chars[index]
    return code

for _ in range(3):
    print(generate_code())

# 方法二
import random
import string

all_chars = string.digits + string.ascii_letters

def generate_code(code_len=6):
    return ''.join(random.choices(all_chars, k= code_len))
print(generate_code())