#!/usr/bin/python

import re
import configparser
import argparse
import sys

linuxKey = ''

inputParser = argparse.ArgumentParser(description='Dual Boot Bluetooth Mouse)')
inputParser.add_argument('-w', '--win-file', dest='winFile', help='Windows registry file', required=True)
inputParser.add_argument('-l', '--linux-file', dest='linuxFile', help='Linux Bluetooth info file', required=True)
inputParser.add_argument('-m', '--mac', dest='mac', help='Mouse MAC address', required=True)

arguments = vars(inputParser.parse_args())

# validate MAC address format
if not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", arguments['mac'].lower()):
    print('Error: wrong MAC address format')
    sys.exit(1)

## get the Bluetooth key from the Windows registry file
with open (arguments['winFile'], 'r', encoding='utf-16') as f:
    for line in f.readlines():
        if arguments['mac'].replace(':','').lower() in line.lower():
            winKey = re.search('=hex:(.+)', line).group(1)
            linuxKey = winKey.replace(',','').upper()

    if not linuxKey:
        print('Error: Mouse MAC address was not found in the Windows registry file.')
        sys.exit(1)

## write Windows key in the Linux file
config = configparser.ConfigParser()
# preserve case for letters
config.optionxform = lambda option: option
config.read(arguments['linuxFile'])
config.set('LinkKey', 'Key', linuxKey)
with open(arguments['linuxFile'],'w') as linuxFile:
   # remove white space delimiters (key=value)
   config.write(linuxFile, space_around_delimiters=False)
   print('File changed. Restart bluetooth service.')
