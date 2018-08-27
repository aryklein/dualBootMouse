#!/usr/bin/python

import sys, re

pLTK = re.compile('"LTK".+:(.+)')
pERand = re.compile('"ERand".+:(.+)')
pEDIV = re.compile('"EDIV".+:(.+)')
pIRK = re.compile('"IRK".+:(.+)')
pCSRK= re.compile('"CSRK".+:(.+)')

f = open ('mouse.txt', 'r')

for line in f.readlines():
    if pLTK.search(line):
        LTK = pLTK.search(line).group(1)
        # Lower case to upper case and no comma
        LTK = LTK.replace(',','').upper()

    elif pERand.search(line):
        ERand = pERand.search(line).group(1)
        # Convert to list and revert the order
        ERand = ERand.split(',')[::-1]
        # Convert the list string again
        ERand = ''.join(ERand)
        # Convert to decimal
        ERand = str(int(ERand, 16))

    elif pEDIV.search(line):
        EDIV = pEDIV.search(line).group(1)
        # Convert to decimal
        EDIV = str(int(EDIV, 16))

    elif pIRK.search(line):
        IRK = pIRK.search(line).group(1)
        # Lower case to upper case and no comma
        IRK = IRK.replace(',','').upper()

    elif pCSRK.search(line):
        CSRK = pCSRK.search(line).group(1)
        CSRK = CSRK.replace(',','').upper()

print(LTK)
print(ERand)
print(EDIV)
print(IRK)
print(CSRK)

