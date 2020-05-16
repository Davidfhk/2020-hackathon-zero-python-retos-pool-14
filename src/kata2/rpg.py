#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(passLen))

    return password
