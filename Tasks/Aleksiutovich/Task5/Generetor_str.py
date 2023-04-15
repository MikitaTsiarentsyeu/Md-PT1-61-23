import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    rand_string = ''.join(random.sample(letters, length))
    return rand_string