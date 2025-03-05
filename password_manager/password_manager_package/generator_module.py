# generator module

# import random and string module 

import random as rn
import string  as st

# generate random password

def generate_password():
    random_password = ''.join(rn.choices(st.ascii_letters + st.digits, k=12))
    return random_password

