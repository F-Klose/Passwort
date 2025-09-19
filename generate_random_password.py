import random
import string
# version 2 mit passenden regelungen versehen das es mit der verschlueselung zusammen passt
def generate_random_password(length=8):
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(length))


print(generate_random_password(8))