#!/usr/bin/env python2
"""reducer.py"""

from operator import itemgetter
import sys

current_key = None
current_count = 0
word = None
current_values = set()
res = []
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_key == key:
        current_values.add(value)
    else:
        if current_key:
            # write result to STDOUT
            # print '%s\t%s' % (current_key, current_count)
            res.append([current_key, len(current_values)])
            current_values = set()
        current_key = key
        current_values.add(value)

# do not forget to output the last word if needed!
if current_key == key:
    res.append([current_key, len(current_values)])
    current_values = set()

#sort
res.sort(key=lambda x:x[1], reverse=True)
for each in res:
    print '%s\t%s' % (each[0], each[1])

