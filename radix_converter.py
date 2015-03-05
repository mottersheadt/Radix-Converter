#!/usr/bin/python

import sys, math, string

if len(sys.argv) < 3:
    print """
This is a program for converting values of a different radix to base10.
However, it does not follow the encoding standards that are defined in RFC 4648 (http://www.rfc-editor.org/rfc/rfc4648.txt)
Every encoding will be converted as 0-9a-z. It is case insensitive.
It's useful for base16 stuff?

Takes two arguments: [radix] [value]
"""
    sys.exit()

radix		= int(sys.argv[1])
value		= sys.argv[2].lower()

letters		= string.ascii_lowercase
conversion	= {}

if radix > 10:
    num		= 10
    for i in letters[ 0:radix-10 ]:
        conversion[i]	= num
        num		+= 1

base10		= 0
idx		= 0
for i in value[::-1]:
    if i.isdigit() == False:
        if i in conversion:
            i	= conversion[i]
        else:
            print "Number given not valid. Character that broke: %s" % i
            sys.exit()
    elif int(i) >= radix:
        print "Number given not valid. Character that broke: %s" % i
        sys.exit()
        
    layer	= float(i) * radix**idx
    print """ {0}	* ({1}^{2})	= {3} """.format( int(i), radix, idx, layer )
    base10	+= layer
    idx		+= 1
print int(base10)
