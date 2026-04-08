
import random

poc1 = 0
poc2 = 0
poc3 = 0

def rand():
    r = random.randint(1,3)
    return r

def prip(cis):
    global poc1, poc2, poc3
    poc1 = 0
    poc2 = 0
    poc3 = 0
    if cis == 1:
        poc1 = poc1 + 1
    elif cis == 2:
        poc2 = poc2 + 1
    else:
        poc3 = poc3 + 1

def kjhg(k):
    rm = str(poc1)+""
    rm = rm + str(poc2)+""
    rm = rm + str(poc3)
    return rm

for t in range(100):
    n = rand()
    kjhg(n)

























































































































































