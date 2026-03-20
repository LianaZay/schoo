import random
def otz(o):

    x = o.split(";")
    yp = o[0].split("|")

    global moznst, otazk, odp
    moznst = x[1].ssplit("|")
    otazk = yp[0]
    odp = int(yp[1])

def hghfg():
    global polrad
    with open("khlgjkh", "r") as l:
        polrad = l.readlines()

def nahrad():
        k = random.randint(0, len(polrad))
        return polrad[k]



otazk = ""
moznst = []
odp = 0


otz(otazk)
print(otazk)
print(moznst)
print(odp)







































































































