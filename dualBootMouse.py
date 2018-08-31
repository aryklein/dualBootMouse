#!/usr/bin/python

import sys, re, configparser

## Regular expressions
pLTK = re.compile('"LTK".+:(.+)')
pERand = re.compile('"ERand".+:(.+)')
pEDIV = re.compile('"EDIV".+:(.+)')
pIRK = re.compile('"IRK".+:(.+)')
pCSRK= re.compile('"CSRK".+:(.+)')

## Opens the source file and gets the values
with open (sys.argv[1], 'r') as f:
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


## Opens the destination file and writes the values
config = configparser.ConfigParser()
# preserve case for letters
config.optionxform = lambda option: option
config.read(sys.argv[2])
config.set('LongTermKey', 'Key', LTK)
config.set('LongTermKey', 'Rand', ERand)
config.set('LongTermKey','EDiv', EDIV)
config.set('IdentityResolvingKey', 'Key', IRK)
config.set('LocalSignatureKey', 'Key', CSRK)

with open(sys.argv[2],'w') as config_file:
   config.write(config_file)


print(LTK)
print(ERand)
print(EDIV)
print(IRK)
print(CSRK)

