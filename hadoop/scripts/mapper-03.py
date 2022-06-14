#!/usr/bin/env python2
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words, and select the 4th field
    key = line.split(";")[3]
    # increase counters
    #for key in keys:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    print '%s\t%s' % (key, 1)
