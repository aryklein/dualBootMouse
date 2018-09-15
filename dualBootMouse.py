#!/usr/bin/python

import re, configparser, argparse

## Regular expressions
pLTK = re.compile('"LTK".+:(.+)')
pERand = re.compile('"ERand".+:(.+)')
pEDIV = re.compile('"EDIV".+:(.+)')
pIRK = re.compile('"IRK".+:(.+)')
pCSRK= re.compile('"CSRK".+:(.+)')

inputParser = argparse.ArgumentParser(description='Dual Boot BLT Mouse)')
inputParser.add_argument('-w', '--win-file', dest='winFile', help='Windows Reg File', required=True)
inputParser.add_argument('-l', '--linux-file', dest='linFile', help='Linux BLT File', required=True)

arguments = vars(inputParser.parse_args())


## Opens the source file and gets the values
with open (arguments['winFile'], 'r') as f:
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
config.read(arguments['linFile'])
config.set('LongTermKey', 'Key', LTK)
config.set('LongTermKey', 'Rand', ERand)
config.set('LongTermKey','EDiv', EDIV)
config.set('IdentityResolvingKey', 'Key', IRK)
config.set('LocalSignatureKey', 'Key', CSRK)

with open(arguments['linFile'],'w') as config_file:
   # remove white space delimiters (key=value)
   config.write(config_file, space_around_delimiters=False)


print(LTK)
print(ERand)
print(EDIV)
print(IRK)
print(CSRK)

