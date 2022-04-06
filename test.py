#!/usr/bin/python

# Rename this file to `service`, so info-beamer automatically starts it
# on your device.

import time
from ibquery import InfoBeamerQuery
from datetime import datetime
import random
import string


def randStr(chars=string.ascii_uppercase + string.digits, N=10):
    return ''.join(random.choice(chars) for _ in range(N))


def main():
    while 1:

        print("Hello\nWorld\n%s\n" % (randStr(N=7)))
        time.sleep(1)


if __name__ == "__main__":
    main()
